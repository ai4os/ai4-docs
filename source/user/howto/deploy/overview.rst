Deployment options in AI4OS
===========================

This page serves a guide, summarizing the pros and cons of each deployment option.
With this information in mind, users can make the best decision on where to deploy their models.

.. list-table:: AI4OS deployment options
    :header-rows: 1

    * - Option
      - ✅ Pros
      - ❌ Cons
    * - :doc:`Deploy as AI4OS serverless </user/howto/deploy/oscar>` (model is loaded on demand)
      - - You are not consuming resources when you are not using the model,
        - Deployments can auto-scale to fit peaks in user queries,
        - Zero configuration needed as the model is deployed in the AI4OS stack.
      - - Predictions can have some latency, due to the AI model being loaded at each prediction.
    * - :doc:`Deploy with AI4OS dedicated resources </user/howto/deploy/nomad>` (model is always loaded)
      - - Low latency in predictions,
        - Zero configuration needed as the model is deployed in the AI4OS stack.
      - - You are consuming resources even when not actively making predictions.
    * - :doc:`Deploy in your own cloud resources </user/howto/deploy/cloud>`
      - - You control where you deploy (no need to be an AI4OS member).
      - - More work to configure the deployment,
        - You are consuming resources even when not actively making predictions (if not deployed as serverless).

Given the above specifications, we recommend the following typical workflows:

* :doc:`Deploy as AI4OS serverless </user/howto/deploy/oscar>` if you plan expect your service to receive lots of user queries and low latency is not critical.
  This is the *recommended option* by default for all users.
* :doc:`Deploy with AI4OS dedicated resources </user/howto/deploy/nomad>` if you need your service to handle few user queries with low latency.
* :doc:`Deploy in your own cloud resources </user/howto/deploy/cloud>` if you do not belong to the project.