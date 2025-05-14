Data drift detection with Frouros
=================================

.. admonition:: Requirements
   :class: info

   🔒 This tutorial requires :ref:`full authentication <getting-started/register:Full authentication>`.

The AI4OS Platform allows to `detect drift <https://frouros.readthedocs.io/en/latest/concepts.html>`__
in your data at inference during production. This is a useful warning that the
inference results might not be reliable anymore and that some action should be
taken.

In this tutorial, we are going to demonstrate how to implement drift detection
in an image object detection pipeline. Specifically, we are going to use the
`OBSEA Fish Detection module <https://dashboard.cloud.ai4eosc.eu/catalog/modules/obsea-fish-detection>`__,
where the drift detector will signal that the underwater camera is dirty and
needs cleaning.

You can find a full code example at this `Repository example`_ and specific
demonstrations at `Notebooks`_.

.. _Repository example: https://github.com/ai4os-hub/obsea-fish-detection/tree/drift-camera
.. _Notebooks: https://github.com/ai4os-hub/obsea-fish-detection/tree/drift-camera/notebooks

Prepare the tools for drift detection in your module
----------------------------------------------------

To prepare the tools for drift detection in your module, follow these steps:

1. **Define a configuration file to handle reference/test data**:

   Use torchvision (or your preferred library) to load the images and convert
   them to tensors. It is recommended to resize the images to a smaller size
   (e.g., 216x384) to reduce computational cost and complexity. This can be
   done using the `torchvision.transforms` module.

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
              transforms.Normalize(
                mean=settings["mean"], 
                std=settings["std"]
            ),
          ]
      )

   Additionally, you need to define which images from your dataset will be
   used for reference and ideally, which ones will be used for testing. In our
   case, we will use the images from the OBSEA dataset and define the clean
   (for clean camera state) and dirty (for bad camera state). The clean images
   will be used as reference to train the detector and determine the
   statistical properties of the data under normal conditions.

   .. code-block:: python

      image_names = settings["camera_state"]["clean"]
      image_paths = [images_parent / name for name in image_names]
      dataset = ImageDataset(image_paths, transform=transform)

   Ideally, you might want to use a configuration file to define the images
   that will be used for reference and test. In our example, we use the `toml`
   format to define the configuration file.

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

   Once the pipeline to load the images and convert them to tensors is defined,
   we can proceed to the next step.

2. **Choose the appropriate detection method**:

   In our task, we want to analyze changes in data properties, not to evaluate
   a model's performance, so we need to select a "Data drift" detection method.
   Since our service processes one image per call (e.g., one image per day), we
   need a Streaming method. For image data with multiple features, a
   Multivariate method is required. As the input data is numerical, the method
   must support numerical data. Based on this analysis, the best method is
   `Maximum Mean Discrepancy` (MMDStreaming) as implemented in the `frouros`
   library (see `Gretton et al. 2012`_).

   You can check this `Frouros table`_ to see and select between the available
   methods in `Frouros`_.

3. **Train an autoencoder**:

   Machine learning and drift detection problems with images have a high
   dimensionality (e.g., 224x224x3). To reduce computational cost and
   complexity, we can train an autoencoder to lower the dimensionality of
   the data.

   .. image:: /_static/images/driftwatch/drift-autoencoder.png

   This tutorial will not cover the details of training an autoencoder, but you
   can find many online tutorials on how to do it using `TensorFlow autoencoder`_
   or `PyTorch autoencoder`_. What is important is to train the autoencoder
   with images, so that it learns to encode the clean (and ideally dirty)
   states of the camera.

   .. image:: /_static/images/driftwatch/clean_decoded.png
   
   .. image:: /_static/images/driftwatch/dirty_decoded.png

4. **Save clean embeddings and model weights**:

   The autoencoder will be used to generate embeddings for the images. These
   embeddings will be used as reference data for the drift detection and as
   input to the MMDStreaming method. Therefore, we need to save it in the
   module storage so that it can be used later in the inference process
   (to encode the uploaded images).

   Additionally, we need to use the autoencoder to generate the embeddings for
   the clean camera images used for the training of our drift detector.

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

   > Save the trained autoencoder model weights and the clean embeddings in the
   module storage at `/storage`. These embeddings will serve as the baseline
   for drift detection.

5. **Create and train the data drift detector**:

   Using the library `frouros`, we can create a drift detector that will
   monitor the incoming data and compare it with the reference data
   (clean embeddings). As defined in the previous step, we will use the
   MMDStreaming method to detect drift in the data.

   .. code-block:: python

      from functools import partial
      from frouros.detectors.data_drift import MMDStreaming
      from frouros.utils.kernels import rbf_kernel

      detector = MMDStreaming(window_size=12, kernel=partial(rbf_kernel, sigma=0.3))
      clean_embeddings = load_encodings(...)
      detector.fit(clean_embeddings.cpu().numpy())  # Frouros expects numpy arrays

   This method compares the distribution of incoming data with the reference
   data in real-time by using a sliding window approach. The first calls to
   `update` will be used to fill the sliding window, and then the detector will
   start to compare the incoming data with the reference data. Due to this
   process, the first 12 calls to `update` will not be used to detect drift and
   will return `None`. We can warm up the detector by calling `update` with the
   clean embeddings.

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

   Configure the drift detector to monitor the embeddings generated by the
   autoencoder. This ensures that the drift detection focuses on the most
   relevant features of the data.

   The last step, due to the properties of the MMD method, is to define a
   threshold for the drift detection metric. If the metric exceeds the
   threshold, it indicates potential drift.

   .. code-block:: python

      # Define a threshold for drift detection
      warning_threshold = 0.05  # Adjust this value based on your requirements
      drift_threshold = 0.10  # Adjust this value based on your requirements

      # Check for drift
      if drift_score.distance > drift_threshold:
          print("Drift detected!")
      elif drift_score.distance > warning_threshold:
          print("Warning: Drift score is approaching the threshold.")

   Simulate different scenarios (e.g., clean vs. dirty camera images) to
   validate the drift detection. Ensure that it correctly identifies drift
   and triggers appropriate alerts.

.. _config_files: https://github.com/ai4os-hub/obsea-fish-detection/tree/drift-camera/obsea/config-files
.. _Frouros: https://frouros.readthedocs.io/en/latest
.. _Frouros table: https://github.com/IFCA-Advanced-Computing/frouros?tab=readme-ov-file#%EF%B8%8F%EF%B8%8F-drift-detection-methods
.. _Gretton et al. 2012: https://jmlr.org/papers/volume13/gretton12a/gretton12a.pdf
.. _PyTorch autoencoder: https://frouros.readthedocs.io/en/latest/examples/data_drift/MMD_advance.html#autoencoder-definition
.. _TensorFlow autoencoder: https://www.tensorflow.org/tutorials/generative/autoencoder
.. _notebook_examples: https://github.com/ai4os-hub/obsea-fish-detection/tree/drift-camera/notebooks

Integrate the drift detector in the DEEPaaS API
-----------------------------------------------

To integrate your drift detector in the DEEPaaS API, you need to follow these
steps:

1. **Set up the framework and prepare the environment**:

   Follow the steps in :ref:`Develop Code <develop_code>` example
   to create a new module based on your preferences. You should have a nice
   base project with the basic `get_metadata`, `warm`, and `predict` functions.

   Try to run the dummy module locally to check that everything is working
   before starting to add the drift detector.

2. **Update the warm function to initialize the drift detector**:

   In the `warm` function, you need to initialize the drift detector and load
   the clean embeddings and autoencoder model weights from the module storage.

   .. code-block:: python

      def warm():
          try:  # Warm up the detector with clean data
              logger.info("Warming up the detector with local data")
              clean = load_encodings("/storage/clean_embeddings.pth")
              utils.detector.fit(clean.cpu().numpy())  # Warm up with clean data
              for sample in clean[: utils.detector.window_size]:
                  utils.detector.update(sample.cpu().numpy())
          except Exception as err:
              logger.error("Error when warming up: %s", err, exc_info=True)
              raise  # re-raise the exception after logging

   This process implements the steps to train and warm up the drift detector.
   The function is called when the module is started and will be used to
   initialize the drift detector with the clean embeddings. Note that the
   state of the detector is restarted every time the module is restarted.

3. **Update the predict function to monitor incoming data**:

   In the `predict` function, you need to define the logic to monitor incoming
   data and check for drift. To do so, first, we need to define a schema that
   will be used to define and validate the incoming data.

   .. code-block:: python

      import marshmallow
      from marshmallow import fields, validate

      class PredArgsSchema(marshmallow.Schema):
          """Prediction arguments schema for api.predict function."""

          class Meta:  # Keep order of the parameters as they are defined.
              ordered = True

          input_file = fields.Field(
              metadata={
                  "description": "Image used to evaluate the data drift.",
                  "type": "file",
                  "location": "form",
              },
              required=True,
          )
          drift_distance = fields.Float(
              metadata={
                  "description": "Minimum distance to consider data drift.",
              },
              load_default=0.125,
              validate=validate.Range(min=0.0),
          )

      def get_predict_args():
          return PredArgsSchema().fields()

   As the arguments for inference are defined, we can proceed to implement the
   logic to monitor the incoming data.

   .. code-block:: python

      def predict(input_file, drift_distance):
          try:  # Load the image and encode it
              logger.debug("Loading image from input_file: %s", input_file.filename)
              image = load_image(input_file.filename)
              normalized = transform(image).to(config.device)
              encoded = autoencoder.encoder(normalized.unsqueeze(0))[0]
          except Exception as err:
              logger.error("Error loading image: %s", err, exc_info=True)
              raise  # re-raise the exception after logging
          try:  # Check if the image is clean
              logger.debug("Detecting drift with options: %s", options)
              result, _ = utils.detector.update(encoded.detach().cpu().numpy())
          except Exception as err:
              logger.error("Error detecting drift: %s", err, exc_info=True)
              raise  # re-raise the exception after logging
          logger.debug("Return results as format: %s", accept)
          return {
              "distance": float(result.distance),
              "drift": bool(result.distance > drift_distance),
          }

   The `predict` function is called when the module is used to make predictions
   about the data drift status. The function will load the image, encode it
   using the autoencoder, and then use the drift detector to check if the image
   is clean or dirty. The function will return the drift score and a link to
   the image that was used for the prediction.

   Once the module is running, you can use the `POST` method to send an image
   to the module and check if it is clean or dirty. Follow the steps in
   :ref:`Develop Code <develop_code>` to see how to deploy the module and test
   it.


Add monitoring to your module with Driftwatch
---------------------------------------------

After deploying the module, you can use `DriftWatch`_ to monitor the drift
distance and visualize the drift over time. DriftWatch is a tool that allows
you to monitor the drift distance and visualize the drift over time. It
provides a web interface to visualize the drift distance and the images that
were used for the predictions.

To add monitoring to your module with DriftWatch, follow these steps:


1. **Obtain a MyToken to authenticate to the service**:

   To store data into DriftWatch server, users need to authenticate. To do so,
   the service offers compatibility with federated authentication via 
   `mytoken`_, an service which allows the use of OIDC based tokens with
   enhanced security and long life extensions.

   Follow the following `drift-watch example`_ or the `MyToken docs`_ for
   details on how to use this service.

   The important details are that you obtain a long term MyToken which only
   allowed audiences are the DriftWatch server.

   .. image:: /_static/images/driftwatch/mytoken-audiences.png

   Once you obtain the token, create an environment variable **DRIFT_MONITOR_MYTOKEN**
   and assign your token to it.


2. **Install and register to DriftWatch**:

   To add the DriftWatch library to your module, you need to add the
   `drift-monitor`_ package to the requirements file. This package is used to
   connect your modules with DriftWatch and send the drift distance and data
   to be monitored.

   .. code-block:: console

      $ pip install -U drift-monitor

   Once the package is installed, you need to accept the license agreement and
   register to use the package. You can do this by running the code:

   .. code-block:: python

    import drift-monitor as dw
    dw.register(accept_terms=True)

   This will register the owner of the previously obtained token and assigned
   to **DRIFT_MONITOR_MYTOKEN**. You can run this code at the start of the
   `api.py` or separately if the owner of the tokens is going to be the same.

   Once registered, you will be authorized to create experiments in the `DriftWatch`_
   service with the following code:

   .. code-block:: python

    description = "This is an experiment to track camera status on OBSEA project."
    try:
        dw.new_experiment("obsea-camera", description, public=True)
    except ValueError:
        print("Experiment already exists. Skipping creation.")

   Similar to the registration process this code needs to be executed only once
   so feel free to integrate it into the code. Simply make sure you catch the
   exception if you include it into your `warm` function.


3. **Integrate the DriftWatch client to your module**

   Final step is to extend the `predict` function with the functionality to
   upload your drift jobs to the `DriftWatch`_ server. To do so, you simply
   need to open a python context with `DriftMonitor` defining a model id and
   the tags you want to use to identify your results on the experiment.

   .. code-block:: python

    def predict(input_file, drift_distance):
        model_id, tags = config.data_version, config.tags # Define model id and tags
        parameters = {"some_parameter": "value"} # Define your parameters
        ...
        try:  # Check if the image usign drift detection
            logger.debug("Detecting drift with options: %s", options)
            result, _ = utils.detector.update(encoded.detach().cpu().numpy())
            with dw.DriftMonitor("obsea-camera", model_id, tags) as monitor:
                result, _ = utils.detector.update(encoded.detach().cpu().numpy())
                parameters["distance"] = result.distance
                monitor(result.distance > drift_distance, parameters)
       except Exception as err:
            logger.error("Error detecting drift: %s", err, exc_info=True)
            raise  # re-raise the exception after logging
        logger.debug("Return results as format: %s", accept)
        ...
        return ... # format and return the results as before

   Every time the inference calls the predict function, a new job is opened at
   `DriftWatch`_. If an exception is raised during the execution of the code
   under the `DriftMonitor` context, the job will be closed with `Failed`
   status. Otherwise, normal exit of the context will close the job as
   `Completed`.

.. _MyToken: https://mytok.eu/
.. _MyToken docs: https://mytoken-docs.data.kit.edu/
.. _DriftWatch: https://drift-watch.dev.ai4eosc.eu/
.. _drift-monitor: https://pypi.org/project/drift-monitor/
.. _drift-watch example: https://github.com/ai4os-hub/obsea-fish-detection/blob/drift-camera/notebooks/drift-watch.ipynb


4. **Add links and additional context data to your drift**

   As you might have notice, the second parameter of the `monitor` function
   is a dictionary with the parameters you want to add to your drift job. You
   can add any additional information you want to include in the job. For
   example, you can add a link to the image that was used for the prediction, the
   drift distance, and any other information that you want to include in the
   job.

   To create the link to the image, you can use the `/storage` folder of the server
   where the module is running. This folder can be configured to mount your storage
   service from next cloud, see :ref:`Accessing storage from inside your deployment <storage_access>`.
   First you need to define the environment variables that will be used to
   configure the sorage location and the url. 

   .. code-block:: python

    # in ./api/config.py or similar
    # e.g. /storage/ai4os-your-application-folder/
    store_dir = os.getenv("DRIFT_MONITOR_STORE_DIR", None) 
    # e.g. https://share.services.ai4os.eu/remote.php/webdav/
    store_url = os.getenv("DRIFT_MONITOR_STORE_URL", None) 

   Next use the `store_dir` and `store_url` to store and create the link to the
   image. You can use the `os.makedirs` function to create the directory where the
   image will be stored. The `shutil.copy` function can be used to copy the image
   to the directory. We create one directory per image to simplify the url generation
   in `nextcloud`. The link to the image will be added to the parameters dictionary
   that will be passed to the `monitor` function.

   .. code-block:: python

    def predict(input_file, drift_distance):
        ...
        time = dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        if config.store_dir:  # Copy to permanent storage
            logger.debug("Saving image to store: %s", config.store_url)
            image_dir = f"{config.store_dir}/{time}"
            os.makedirs(image_dir, exist_ok=True)
            shutil.copy(input_file.filename, f"{image_dir}/image.jpg")
        ...
        if config.store_url:  # Add link to parameters
            logger.debug("Adding link to parameters: %s", link)
            parameters["link"] = f"{config.store_url}?path={time}"
        ...
        return ... # format and return the results as before

   Additionally, you can return the link to the image in the response of the
   `predict` function.
    

Deploy your module in production
--------------------------------

In the module page, click on the option ``Codespaces > Jupyter``. You will be 
shown a :ref:`configuration page <dashboard_deployment>` where the option
``Jupyter`` is selected. You can directly click on ``Quick submit`` as you
don't need to configure anything else.

In the ``Deployments`` tab, go to the ``Modules`` table and find your created
deployment. Click the :material-outlined:`terminal;1.5em` ``Quick access`` to
access the JupyterLab terminal.

Now we need to deploy the DEEPaaS API to start monitoring, but make sure you
have configured the environment variables that your application requires. You can
use the terminal to set the environment variables. For example, you can set
the `DRIFT_MONITOR_MYTOKEN` variable to the token you obtained in the previous
step. You can also set the `DRIFT_MONITOR_STORE_DIR` and `DRIFT_MONITOR_STORE_URL`
variables to the directory where you want to store the images and the URL of
the storage service.
You can set the environment variables using the following command:

.. code-block:: console

    $ export DRIFT_MONITOR_MYTOKEN=<your_token>
    $ export DRIFT_MONITOR_STORE_DIR=/storage/ai4os-obsea-fish-detection
    $ export DRIFT_MONITOR_STORE_URL=https://share.services.ai4os.eu/remote.php/webdav/

and then run the following command to deploy the module:

.. code-block:: console

    $ deepaas-run --listen-ip 0.0.0.0


Once the module is running, you can use the `POST` method to send an image
to the module and check if it is clean or dirty. Follow the steps in
:ref:`Develop Code <develop_code>` to see how to deploy the module and test
it.

Access to `DriftWatch`_ in order to visualize the uploaded drift in
the dashboard. 

   .. image:: /_static/images/driftwatch/experiments_page.png

Click on your experiment and you will be shown a list of the
drift jobs that have been uploaded. You can select the desired jobs and
configure the visualization options. To see the drift distance over time.

   .. image:: /_static/images/driftwatch/drifts_page.png

.. _DriftWatch: https://drift-watch.dev.ai4eosc.eu/


If links are correctly configured, you will be able to see then in the row
`View` button of the drift job together with the rest of the saved parameters.

   .. image:: /_static/images/driftwatch/parameters_popup.png


.. TODO: (ignacio)
   In the future we should allow users to input env variables in the Dashboard configuration, to avoid using terminal
