Data drift detection with Frouros
=================================

.. admonition:: Requirements
   :class: info

   🔒 This tutorial requires :ref:`full authentication <getting-started/register:Full authentication>`.

The AI4OS Platform allows to detect **data drift** in your data at inference time.
This is a useful warning that the inference results might not be reliable anymore and
that some action should be taken.

In this tutorial, we are going to demonstrate how to implement drift detection
in an image object detection pipeline. Specifically, we are going to use the
`OBSEA Fish Detection module <https://dashboard.cloud.ai4eosc.eu/catalog/modules/obsea-fish-detection>`__,
where the drift detector will signal that the underwater camera is dirty and
needs cleaning.

You can find a the full code of this tutorial `here <https://github.com/ai4os-hub/obsea-fish-detection/tree/drift-camera>`_, as well as `reference notebooks <https://github.com/ai4os-hub/obsea-fish-detection/tree/drift-camera/notebooks>`__.

In this tutorial, we use `Frouros`_ as the main drift detection library, but the tutorial still applies to other
popular drift detection libraries like `Alibi-detect <https://github.com/SeldonIO/alibi-detect>`__, `Evidently <https://github.com/evidentlyai/evidently>`__, `Eurybia <https://github.com/MAIF/eurybia>`__, etc.

.. _Frouros: https://frouros.readthedocs.io/en/latest

What is drift detection?
------------------------

In drift detection, we monitor a model at inference time to detect when the input data
starts to deviate from the training data distribution: we call this **data drift**.
There could be many reasons causing data drift:

* the sensor taking the images is dirty, so we need to clean it,
* the distribution of data has really changed, so the model needs to be retrained,

In any case, the predictions are no longer reliable and an action has to be taken by the user.

To achieve drift monitoring, we take the inference data vector and compare it with a reference
training dataset. We compute a **p-value** that summarizes what is the likelihood that the inference vector
could come from the training data. If the p-value is below a threshold, we can confidently assert
that the data has indeed drifted.

In the case of images, the pure pixels values are not a good summarizer of the image statistics.
So we typically train an **autoencoder model** that is able to summarize the pixel values into a smaller
vector that more accurately describes the image. We then use this vector to compute the p-values, as before.

Find more information on the `fundamentals of drift detection <https://frouros.readthedocs.io/en/latest/concepts.html>`__.


Create your drift detector
--------------------------

1. Define your reference data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo: reread again this section

Use `torchvision <https://docs.pytorch.org/vision>`__ (or your preferred library) to load the images and convert
them to tensors. It is recommended to resize the images to a smaller size
(e.g., 216x384) to reduce computational cost and complexity. This can be
done using the ``torchvision.transforms`` module.

.. dropdown:: ㅤㅤ 📄 Preprocess your images (Python)

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

Ideally, you might want to use a configuration file to define the images
that will be used for reference and test. In our example, we use the ``toml``
format to define the configuration file.

.. dropdown:: ㅤㅤ 📄 Configuration file (TOML)

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

.. dropdown:: ㅤㅤ 📄 Load the configuration file (Python)

    .. code-block:: python

        import tomllib

        with open("config.toml", "rb") as f:
            settings = tomllib.load(f)

        image_names = settings["camera_state"]["clean"]
        image_paths = [images_parent / name for name in image_names]
        dataset = ImageDataset(image_paths, transform=transform)

Once the pipeline to load the images and convert them to tensors is defined,
we can proceed to the next step.

2. Choose the detection method
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It's time to select the appropriate detection method for our usecase, based
on the `Frouros table`_ of available methods:

* In our task, we want to analyze changes in data properties, not to evaluate
  a model's performance, so we need to select a **Data drift** detection method.
* Since our service processes one image per call (e.g., one image per day), we
  need a **Streaming** method.
* For image data with multiple features, a **Multivariate method** is required.
* As the input data is numerical, the method must support **numerical** data.

Based on this analysis, the best method is *Maximum Mean Discrepancy* (``MMDStreaming()``).

.. _Frouros table: https://github.com/IFCA-Advanced-Computing/frouros?tab=readme-ov-file#%EF%B8%8F%EF%B8%8F-drift-detection-methods

3. Train an autoencoder
^^^^^^^^^^^^^^^^^^^^^^^

.. tip::

   If you module does not involve image data, you can skip this step.
   You change the references in the text below from *clean embeddings* to *clean data*.

Drift detection struggles to understand images because of their high
dimensionality (e.g. 224x224x3). To reduce computational cost and
complexity, we can train an autoencoder to lower the dimensionality of
the image data before feeding them to the drift detector.

.. image:: /_static/images/driftwatch/drift-autoencoder.png

This tutorial will not cover the details of training an autoencoder, but you
can find many online tutorials on how to do it using `TensorFlow <https://www.tensorflow.org/tutorials/generative/autoencoder>`__
or `PyTorch <https://frouros.readthedocs.io/en/latest/examples/data_drift/MMD_advance.html#autoencoder-definition>`_. What is important is to train the autoencoder
with images, so that it learns to encode the clean (and ideally dirty)
states of the camera.

.. image:: /_static/images/driftwatch/clean_decoded.png

.. image:: /_static/images/driftwatch/dirty_decoded.png

At inference time, you will need to to create the embeddings of the incoming images to pass them to the drift detector model.
So you need to save the autoencoder weights in the
:doc:`AI4OS Storage </reference/storage>` to be able to load them at inference time.

Optionally, you can also save the embeddings of clean camera images to warm the the drift detector at inference time.

.. dropdown:: ㅤㅤ 📄 Saving autoencoder and clean embeddings (Python)

    .. code-block:: python

        # Load the autoencoder model
        autoencoder = Autoencoder()  # define your autoencoder architecture
        train(autoencoder, dataset)  # train the autoencoder on the dataset
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


4. Create and train the data drift detector
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using the `Frouros`_ library, we can create a drift detector that will
monitor the incoming data and compare it with the reference data
(clean embeddings). As defined in the previous step, we will use the
``MMDStreaming()`` method to detect drift in the data.

This method compares the distribution of incoming data with the reference
data in real-time by using a sliding window approach. The first calls to
``update()`` will be used to fill the sliding window, and then the detector will
start to compare the incoming data with the reference data. Due to this
process, the first 12 calls to ``update()`` will not be used to detect drift and
will return ``None``. Optionally, we can warm up the detector by calling ``update()`` with the
clean embeddings defined in the previous section.

Finally we define a threshold for the drift detection metric. If the metric exceeds the
threshold, it indicates potential drift.

.. dropdown:: ㅤㅤ 📄 Implementing the detection (Python)

    .. code-block:: python

        from functools import partial
        from frouros.detectors.data_drift import MMDStreaming
        from frouros.utils.kernels import rbf_kernel

        detector = MMDStreaming(window_size=12, kernel=partial(rbf_kernel, sigma=0.3))
        clean_embeddings = load_encodings(...)
        detector.fit(clean_embeddings.cpu().numpy())  # Frouros expects numpy arrays

        # Warm up the detector with clean embeddings
        for embedding in clean_embeddings:
            detector.update(embedding.cpu().numpy())

        # Now you can start monitoring incoming data
        for image in incoming_images:
            with torch.no_grad():
                embedding = autoencoder.encoder(image.unsqueeze(0))
            drift_score, _ = detector.update(embedding.cpu().numpy())
            print(f"Drift score: {drift_score.distance}")

        # Define a threshold for drift detection
        warning_threshold = 0.05  # Adjust this value based on your requirements
        drift_threshold = 0.10  # Adjust this value based on your requirements

        # Check for drift
        if drift_score.distance > drift_threshold:
            print("Drift detected!")
        elif drift_score.distance > warning_threshold:
            print("Warning: Drift score is approaching the threshold.")

We recommend simulating different scenarios (e.g., clean vs. dirty camera images) to
validate the drift detection. Ensure that it correctly identifies drift
and triggers appropriate alerts.


Integrate the drift detector with the DEEPaaS API
-------------------------------------------------

Now that you have your detector ready you need to integrate it with the :doc:`DEEPaaS API </reference/api>` so that it will be used at inference time.

If you followed the steps in :ref:`Develop a model (tutorial) <develop_code>`, you should have a model the basic DEEPaaS functions, including: ``warm()``, ``get_predict_args()`` and ``predict()``.

Once this is done, you need to perform the following updates:

1. Update the warm function
^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the ``warm()`` function, you need to initialize the drift detector and load
the clean embeddings and autoencoder model weights from the module storage.

The function is called when the module is started and will be used to
initialize the drift detector with the clean embeddings. Note that the
state of the detector is restarted every time the module is restarted.

.. code-block:: python

    def warm():
        # Warm up the detector with clean data
        clean = load_encodings("/storage/clean_embeddings.pth")
        utils.detector.fit(clean.cpu().numpy())
        for sample in clean[:utils.detector.window_size]:
            utils.detector.update(sample.cpu().numpy())


2. Update the predict function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the ``predict()`` function, you need to define the logic to monitor incoming
data and check for drift. To do so, first, we need to define a schema that
will be used to define and validate the incoming data.

.. dropdown:: ㅤㅤ 📄 Implementing predict schema (Python)

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

The ``predict()`` function is called when the module is used to make predictions
about the data drift status. The function will load the image, encode it
using the autoencoder, and then use the drift detector to check if the image
is clean or dirty. The function returns whether drift exists or not.

.. code-block:: python

  def predict(input_file, drift_distance):
      # Load the image and encode it
      image = load_image(input_file.filename)
      normalized = transform(image).to(config.device)
      encoded = autoencoder.encoder(normalized.unsqueeze(0))[0]

      # Check if the image is clean
      result, _ = utils.detector.update(encoded.detach().cpu().numpy())
      return {
          "drift": bool(result.distance > drift_distance),
      }


Monitor drift with Driftwatch
-----------------------------

The previous section has showed how we could compute drift inside our predict function.

But for a better user experience, we have developed `DriftWatch`_ to visualize the drift over time.
It allows to save the drift metrics for each inference call and visualize them over time. It also
provides a web interface to visualize the data (eg. images) that was were used for the predictions.

To connect your module with DriftWatch, follow these steps:


1. Obtain a MyToken to authenticate to the service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To store data into DriftWatch server, users need to authenticate. To do so,
DriftWatch offers compatibility with federated authentication via
`mytoken`_, a service which allows the use of OIDC based tokens with
enhanced security and long life extensions.

To obtain your token:

1. Login into `mytoken`_ selecting the ``AI4EOSC`` provider
2. Go to ``Create MyToken``:

   - Provide a ``Token name``
   - Set ``Audiences`` to https://drift-watch.cloud.ai4eosc.eu/
   - Click on ``Create new Mytoken``

.. TODO: where to retrieve the token value ?

.. image:: /_static/images/driftwatch/mytoken-audiences.png


2. Install DriftWatch in your module
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create an environment variable ``DRIFT_MONITOR_MYTOKEN`` and assign your mytoken to it.

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


3. Integrate the DriftWatch client to your module
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Final step is to extend the `predict` function with the functionality to
upload your drift jobs to the `DriftWatch`_ server. To do so, you simply
need to open a python context with `DriftMonitor` defining a model id and
the tags you want to use to identify your results on the experiment.

.. code-block:: python

  def predict(input_file, drift_distance):
      model_id, tags = config.data_version, config.tags
      parameters = {"some_parameter": "value"}
      ...
      # Check if the image using drift detection
      result, _ = utils.detector.update(encoded.detach().cpu().numpy())
      with dw.DriftMonitor("obsea-camera", model_id, tags) as monitor:
          result, _ = utils.detector.update(encoded.detach().cpu().numpy())
          parameters["distance"] = result.distance
          monitor(result.distance > drift_distance, parameters)
      ...
      return ... # format and return the results as before

Every time the inference calls the predict function, a new job is opened at
`DriftWatch`_. If an exception is raised during the execution of the code
under the `DriftMonitor` context, the job will be closed with `Failed`
status. Otherwise, normal exit of the context will close the job as
`Completed`.

.. _MyToken: https://mytok.eu/
.. _MyToken docs: https://mytoken-docs.data.kit.edu/
.. _DriftWatch: https://drift-watch.cloud.ai4eosc.eu/
.. _drift-monitor: https://pypi.org/project/drift-monitor/
.. _drift-watch example: https://github.com/ai4os-hub/obsea-fish-detection/blob/drift-camera/notebooks/drift-watch.ipynb


4. Add links and additional context data to your drift
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

.. todo: needs to be connected to storage to retrieve modelweights

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

.. _DriftWatch: https://drift-watch.cloud.ai4eosc.eu/


If links are correctly configured, you will be able to see then in the row
`View` button of the drift job together with the rest of the saved parameters.

   .. image:: /_static/images/driftwatch/parameters_popup.png


.. TODO: (ignacio)
   In the future we should allow users to input env variables in the Dashboard configuration, to avoid using terminal
