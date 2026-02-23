Deployment options
==================

This page serves a guide, summarizing the pros and cons of each deployment option.
With this information in mind, users can make the best decision on where to deploy their models.

.. list-table:: Deployment options from the Dashboard
    :header-rows: 1

    * - Option
      - ✅ Pros
      - ❌ Cons
    * - :doc:`Deploy as serverless </howtos/deploy/oscar>` (model is loaded on demand)
      - - You are not consuming resources when you are not using the model,
        - Deployments can auto-scale to fit peaks in user queries,
        - Supports both sync and async calls
        - Supports predictions via default UI (Oscar)
        - Zero configuration needed as the model is deployed internally,
        - Can be manually customized for specific needs (like historical data batch prediction).
      - - Predictions can have some latency, due to the AI model being loaded at each prediction.
    * - :doc:`Deploy persistently </howtos/deploy/nomad>` (model is always loaded)
      - - Low latency in predictions,
        - Supports sync calls
        - Supports predictions via dedicated UI (Gradio)
        - Zero configuration needed as the model is deployed internally.
      - - You are consuming resources even when not actively making predictions.
    * - :doc:`Deploy in your own cloud resources </howtos/deploy/cloud>`
      - - You control where you deploy (no need to be a project member).
        - Supports sync calls
      - - More work to configure the deployment,
        - You are consuming resources even when not actively making predictions (if not deployed as serverless).
    * - :doc:`Deploy in the EOSC node </howtos/deploy/eosc-node>`
      - - You control where you deploy (no need to be a project member). Free limited resources for any European researcher.
        - Supports sync calls
      - - More work to configure the deployment,
        - You are consuming resources even when not actively making predictions (if not deployed as serverless).

Given the above specifications, we recommend the following typical workflows:

* :doc:`Deploy as serverless </howtos/deploy/oscar>` if your service does not need low latency and expects to either (1) receive lots of concurrent user queries or (2) receive user queries that are spaced-out in time.
  This is the *recommended option* by default for all users.
* :doc:`Deploy persistently </howtos/deploy/nomad>` if your service needs to handle, with low latency, few concurrent user queries that are close in time.
* :doc:`Deploy in your own cloud resources </howtos/deploy/cloud>` if you do not belong to the project and have access to private cloud resources.
* :doc:`Deploy in the EOSC node </howtos/deploy/eosc-node>` if you are a European researcher who does not belong to the project and don't have access to private cloud resources.

If you need to generate one-off predictions on a given dataset but not maintain a running service, you have two options:

* :doc:`Deploy persistently </howtos/deploy/nomad>` with a GPU, make your predictions and delete the deployment.
* :doc:`Deploy as serverless </howtos/deploy/oscar>` and upload your dataset files to a bucket to perform :ref:`async predictions <howtos/deploy/oscar:Asynchronous predictions>`. If your dataset is really big, you can :doc:`contact support </help/index>` to create a custom batch processing pipeline tailored to your usecase.

In addition to the above deployment options from the Dashboard, there are several additional deployment methods:

* :doc:`Deploy a model manually in the Inference Platform (serverless) </howtos/deploy/oscar-manual>`
* :doc:`Deploy a model locally </howtos/try/locally>`
