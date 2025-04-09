Data drift detection with Frouros
=================================

.. admonition:: Requirements
   :class: info

   🔒 This tutorial requires :ref:`full authentication <getting-started/register:Full authentication>`.


The AI4OS Platform allows to `detect drift <https://frouros.readthedocs.io/en/latest/concepts.html>`__ in your data at inference during production.
This is a useful warning that the inference results might not be reliable anymore and that some action should be taken.

In this tutorial, we are going to demonstrate how to implement drift detection in an image object detection pipeline.
Specially we are going to use the `OBSEA Fish Detection module <https://dashboard.cloud.ai4eosc.eu/catalog/modules/obsea-fish-detection>`__, where the drift detector will signal that the underwater camera is dirty and needs cleaning.

Prepare the tools for drift detection in your module
--------------------------------------

.. TODO: (borja) explain
  - creation of config file with reference/test data:
   - you need to define the data that is going to be defined used as reference for data drift detection
     This data defines which statistical properties ar in the boundaries of normality)

   - Choose the correct detection methods according to your problem.
    In our example, we are going to follow the information at https://github.com/IFCA-Advanced-Computing/frouros?tab=readme-ov-file#%EF%B8%8F%EF%B8%8F-drift-detection-methods
    to decide which is the best method to our problem.

    We want to analyze changes on the data properties, we are not going to evaluate a model performance. Therefore we need to choose a "Data drift" detection method.
    Our service will work providing our "inference" method with a unique image per call (for example an image taken each day). With only one image per call, so we need to choose an Streaming method.
    Additionally, when working with images, we need to choose a method that is able to work with multiple features, so we need to pick a Multivariate method.
    Our data input is numerical (not categorical), so we need to choose a method that is able to work with numerical data.

    After this analysis the best (only) method for our problem is the `Maximum Mean Discrepancy` Gretton et al. (2012) https://dl.acm.org/doi/10.5555/2188385.2188410
    This method is implemented in the `frouros` library as `MMDStreaming`.

  - train an autoencoder (and why)
    The dimensionality of the data in images is very high, for example (224x224x3), so we need to reduce the dimensionality of the data before applying the drift detection method
    in order to reduce the computational cost and complexity of the drift detection method.
    To do this we need to train an autoencoder with the data (and if available, with the test data with pictures of a dirty camera).
    This will allow us to reduce the dimensionality of the data and to learn a representation of the data that is more suitable for the drift detection method.
    There are multiple online examples on how to to train an autoencoder with "Tensorflow <https://www.tensorflow.org/tutorials/generative/autoencoder>"__ or "PyTorch <https://pytorch.org/tutorials/beginner/blitz/autoencoder_tutorial.html>"__, 
    therefore we are not going to explain how to do it here.
    The most important is to check that the autoencoder correctly encodes the dimensionality that represents the different states of the camera (clean/dirty).
    It is not so important that the fishes around are correctly encoded/decoded as we do not plan to detect drift in the fishes but rather on the background colors or the camera lens.
       
  - where to save clean/dirty embeddings, where to save model weights
    Once the autoencoder is trained, we need to save the model weights and the clean embeddings in the module storage.
    The autoencoder model weights are recommended to be saved in the module storage in the path `/storage`.
    The clean embeddings are recommended to be saved in the module storage in the path `/storage`.



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