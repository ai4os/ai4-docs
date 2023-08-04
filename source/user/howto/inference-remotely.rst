Try a service remotely
======================

.. TODO: Replace with Oscar instructions when ready

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; margin-bottom: 2em; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/FyELMIr5Wbo" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>


1. Choose your module and deploy
--------------------------------

The first step is to choose a module from the :doc:`Dashboard</user/overview/dashboard>`.
There you will be able to find all the modules ready to be used under the tag ``Inference``.

For educational purposes we are going to use a `general model to identify images <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/deep-oc-image-classification-tf>`__.
This will allow us to see the general workflow.
Select that module and :ref:`follow the instructions <user/overview/dashboard:Making a deployment>`
to deploy it, making sure to select ``DEEPaaS`` as the ``Service`` in the configuration.

2. Accessing the module and make predictions
--------------------------------------------

Go to the ``Deployments`` tab and select the ``deepaas`` endpoint in your newly deployed module.
It will open the Swagger UI with the API documentation,
where you can test the module's functionality, as well as perform other actions.

.. image:: /_static/images/deepaas.png
  :width: 500

Go to the  ``predict()`` function and upload the file/data you want to predict (in the case of the image classifier
this should be an image file). The appropriate data formats of the files you have to upload are often discussed
in the module's Marketplace page.

The response from the ``predict()`` function will vary from module to module but usually consists on a JSON dict
with the predictions. For example the image classifier return a list of predicted classes along with predicted accuracy.
Other modules might return files instead of a JSON.
