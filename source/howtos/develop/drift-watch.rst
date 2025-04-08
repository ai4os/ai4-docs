Data drift detection with Frouros
=================================

.. admonition:: Requirements
   :class: info

   🔒 This tutorial requires :ref:`full authentication <getting-started/register:Full authentication>`.


The AI4OS Platform allows to `detect drift <https://frouros.readthedocs.io/en/latest/concepts.html>`__ in your data at inference during production.
This is a useful warning that the inference results might not be reliable anymore and that some action should be taken.

In this tutorial, we are going to demonstrate how to implement drift detection in an image object detection pipeline.
Specially we are going to use the `OBSEA Fish Detection module <https://dashboard.cloud.ai4eosc.eu/catalog/modules/obsea-fish-detection>`__, where the drift detector will signal that the underwater camera is dirty and needs cleaning.

Create a drift detector in your module
--------------------------------------

.. TODO: (borja) explain
  - creation of config file with clean/dirty data
  - how to train autoencoder
  - where to save clean/dirty embeddings, where to save model weights


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