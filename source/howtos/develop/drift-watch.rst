Data drift detection with Frouros
=================================

.. admonition:: Requirements
   :class: info

   🔒 This tutorial requires :ref:`full authentication <getting-started/register:Full authentication>`.

The AI4OS Platform allows to `detect drift <https://frouros.readthedocs.io/en/latest/concepts.html>`__ in your data at inference during production.
This is a useful warning that the inference results might not be reliable anymore and that some action should be taken.

In this tutorial, we are going to demonstrate how to implement drift detection in an image object detection pipeline.
Specially we are going to use the `OBSEA Fish Detection module <https://dashboard.cloud.ai4eosc.eu/catalog/modules/obsea-fish-detection>`__, where the drift detector will signal that the underwater camera is dirty and needs cleaning.

You can find a full code example at this `Repository example`_ and specific demonstrations at `Notebooks`_.

.. _Repository example: https://github.com/ai4os-hub/obsea-fish-detection/tree/drift-camera
.. _Notebooks: https://github.com/ai4os-hub/obsea-fish-detection/tree/drift-camera/notebooks

Prepare the tools for drift detection in your module
----------------------------------------------------

To prepare the tools for drift detection in your module, follow these steps:

1. **Define a configuration file to handle reference/  test data**:

Use torchvision (or your preferred library) to load the images and convert them to tensors.
It is recommended to resize the images to a smaller size (e.g., 216x384) to reduce computational cost and complexity.
This can be done using the `torchvision.transforms` module.

   .. code-block:: python

    from PIL import Image
    from torch.utils.data import Dataset
    from torchvision import transforms

    from obsea import config


    class ImageDataset(Dataset):
        def __init__(self, image_paths, transform=None):
            self.image_paths = image_paths
            self.transform = transform

        def __len__(self):
            return len(self.image_paths)

        def __getitem__(self, idx):
            image = Image.open(self.image_paths[idx]).convert("RGB")
            if self.transform:
                image = self.transform(image)
            return image.to(config.device)

    transform = transforms.Compose(
            [
                transforms.Resize(settings["resize"]),
                transforms.ToTensor(),
                transforms.Normalize(mean=settings["mean"], std=settings["std"]),
            ]
        )


Additionally, you need to define which images from your dataset will be used for reference
and ideally, which ones will be used for testing. In our case, we will use the images from the OBSEA dataset
and define the clean (for clean camera state) and dirty (for bad camera state).
The clean images will be used as reference to train the detector and determine which are the statistical properties of the data under normal conditions.

   .. code-block:: python

    image_names = settings["camera_state"]["clean"]
    image_paths = [images_parent / name for name in image_names]
    dataset = ImageDataset(image_paths, transform=transform)


Ideally you might want to use a configuration file to define the images that will be used for reference and test.
In our example we use the `toml` format to define the configuration file.

   .. code-block:: toml

      [transform]
      resize = [216, 384]
      mean = [0.00, 0.00, 0.00]
      std = [1.00, 1.00, 1.00]

      [camera_state]
      clean = [
          "20230728-083036-IPC608_8B64_165.jpg",
          # ...
      ]
      dirty = [
          "20230720-073036-IPC608_8B64_165.jpg",
          # ...
      ]

   .. code-block:: python

      import tomllib

      with open("config.toml", "rb") as f:
          settings = tomllib.load(f)

Once the pipeline to load the images and convert them to tensors is defined, we can proceed to the next step.


2. **Choose the appropriate detection method**:

In our task, we want to analyze changes in data properties, not to evaluate a model performance, so we need to select a "Data drift" detection method.
Since our service processes one image per call (e.g., one image per day), we need a Streaming method.
For image data with multiple features, a Multivariate method is required. As the input data is numerical, the method must support numerical data.
Based on this analysis, the best method is `Maximum Mean Discrepancy` (MMDStreaming) as implemented in the `frouros` library (see `Gretton et al. 2012`_).

You can check this `Frouros table`_` to see and select between the available methods in `Frouros`_.

3. **Train an autoencoder**:

Machine learning and drift detection problems with images have a high dimensionality (e.g., 224x224x3).
To reduce computational cost and complexity, we can train an autoencoder to lower the dimensionality of the data.

    .. image:: /_static/images/driftwatch/drift-autoencoder.png

This tutorial will not cover the details of training an autoencoder, but you can find many online tutorials on how to do it using `TensorFlow autoencoder`_ or `PyTorch autoencoder`_.
What is important is to train the autoencoder with images, so that it learns to encode the clean (and ideally dirty) states of the camera.

    .. image:: /_static/images/driftwatch/clean_decoded.png
    
    .. image:: /_static/images/driftwatch/dirty_decoded.png


4. **Save clean embeddings and model weights**:

The autoencoder will be used to generate embeddings for the images.
These embeddings will be used as reference data for the drift detection and as input to the MMDStreaming method, therefore we need to save it in the module storage
so that it can be used later in the inference process (to encode the uploaded images).

Additionally, we need to use the autoencoder to generate the embeddings for the clean camera images used for the training of our drift detector.

    .. code-block:: python
  
      # Load the autoencoder model
      autoencoder = Autoencoder()  # Define your autoencoder architecture
      train(autoencoder, dataset)  # Train the autoencoder on the dataset
      autoencoder.eval()
  
      # Generate embeddings for clean images
      clean_embeddings = []
      for image in dataset:
          with torch.no_grad():
              embedding = autoencoder.encoder(image.unsqueeze(0))
              clean_embeddings.append(embedding)
  
      # Save the model weights and clean embeddings
      torch.save(autoencoder.state_dict(), "/storage/autoencoder.pth")
      torch.save(clean_embeddings, "/storage/clean_embeddings.pth")


> Save the trained autoencoder model weights and the clean embeddings in the module storage at `/storage`. These embeddings will serve as the baseline for drift detection.

5. **Create and train the data drift detector**:

Using the library `frouros`, we can create a drift detector that will monitor the incoming data and compare it with the reference data (clean embeddings).
As defined in the previous step, we will use the MMDStreaming method to detect drift in the data.

    .. code-block:: python
  
      from functools import partial
      from frouros.detectors.data_drift import MMDStreaming
      from frouros.utils.kernels import rbf_kernel

      detector = MMDStreaming(window_size=12, kernel=partial(rbf_kernel, sigma=0.3))
      clean_embeddings = load_encodings(...)
      detector.fit(clean_embeddings.cpu().numpy())  # Frouros expects numpy arrays


This method compares the distribution of incoming data with the reference data in real-time by using a sliding window approach.
The first calls to `update` will be used to fill the sliding window, and then the detector will start to compare the incoming data with the reference data.
Due to this process the first 12 calls to `update` will not be used to detect drift and will return `None`. We can warm up the detector by calling `update` with the clean embeddings.

    .. code-block:: python
  
      # Warm up the detector with clean embeddings
      for embedding in clean_embeddings:
          detector.update(embedding.cpu().numpy())
  
      # Now you can start monitoring incoming data
      for image in incoming_images:
          with torch.no_grad():
              embedding = autoencoder.encoder(image.unsqueeze(0))
          drift_score, _ = detector.update(embedding.cpu().numpy())
          print(f"Drift score: {drift_score.distance}")

Configure the drift detector to monitor the embeddings generated by the autoencoder.
This ensures that the drift detection focuses on the most relevant features of the data.

The last step, due to the properties of the MMD method, is to define a threshold for the drift detection metric.
If the metric exceeds the threshold, it indicates potential drift.

    .. code-block:: python
  
        # Define a threshold for drift detection
        warning_threshold = 0.05  # Adjust this value based on your requirements
        drift_threshold = 0.10  # Adjust this value based on your requirements
  
        # Check for drift
        if drift_score.distance > drift_threshold:
            print("Drift detected!")
        elif drift_score.distance > warning_threshold:
            print("Warning: Drift score is approaching the threshold.")
        
Simulate different scenarios (e.g., clean vs. dirty camera images) to validate the drift detection.
Ensure that correctly identifies drift and triggers appropriate alerts.


.. _config_files: https://github.com/ai4os-hub/obsea-fish-detection/tree/drift-camera/obsea/config-files
.. _Frouros: https://frouros.readthedocs.io/en/latest
.. _Frouros table: https://github.com/IFCA-Advanced-Computing/frouros?tab=readme-ov-file#%EF%B8%8F%EF%B8%8F-drift-detection-methods
.. _Gretton et al. 2012: https://jmlr.org/papers/volume13/gretton12a/gretton12a.pdf
.. _PyTorch autoencoder: https://frouros.readthedocs.io/en/latest/examples/data_drift/MMD_advance.html#autoencoder-definition
.. _TensorFlow autoencoder: https://www.tensorflow.org/tutorials/generative/autoencoder
.. _notebook_examples: https://github.com/ai4os-hub/obsea-fish-detection/tree/drift-camera/notebooks


Integrate the drift detector in the DEEPaaS API
-----------------------------------------------

.. TODO: (borja) explain
  - how to get token with mytoken
  - how to save token as env
  - how to register driftwatch instance
  - how to prepare the warm function
  - how to send (p-values, data_url, ...) to Driftwatch during the predict step
  - how to save data in /storage/ai4os-drift-watch/<uuid> for later visualization
  - how to make /storage/ai4os-drift-watch/ public to allow for visualization inside Driftwach

Deploy your module in production
--------------------------------

In the module page, click on the option ``Codespaces > Jupyter``.
You will be show a :ref:`configuration page <dashboard_deployment>` where the option ``Jupyter`` is selected.
You can directly click on ``Quick submit`` as you don't need to configure anything else.

In the ``Deployments`` tab, go to the ``Modules`` table and find your created deployment.
Click the :material-outlined:`terminal;1.5em` ``Quick access`` to access the JupyterLab terminal.

.. TODO: (borja) explain
  - how to copy env variables using terminal

Now we need to deploy the DEEPaaS API to start monitoring:

.. code-block:: console

    $ deepaas-run --listen-ip 0.0.0.0


.. TODO: (borja) explain
  - mention that you made 50 prediction calls (just to generate a nice time series), no need to show code for this
  - explain how to visualize drift in Driftwatch (time series, image preview)
  - show nice pictures showing the drift

.. TODO: (ignacio)
   In the future we should allow users to input env variables in the Dashboard configuration, to avoid using terminal
