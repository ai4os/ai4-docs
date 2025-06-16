Deploy a model in production
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you have trained your model, you can deploy it in production. This section
provides several guides in how to deploy your model in different environments.


.. grid:: 1
    :gutter: 3

    .. grid-item-card:: :material-outlined:`list;1.5em`    Overview
        :link: overview
        :link-type: doc

        Start here to get an overview of the different deployment options.

    .. grid-item-card:: :material-outlined:`dns;1.5em`  Deploy in the platform (serverless)
        :link: oscar
        :link-type: doc

        Deploy your model in the platform using the serverless option, using a shared
        serverless environment.

    .. grid-item-card:: :fas:`server;fa-lg sd-mr-2`  Deploy in the platform (dedicated)
        :link: nomad
        :link-type: doc

        Deploy your model in the platform using a dedicated deployment and a load
        balancer.

    .. grid-item-card:: :material-outlined:`cloud;1.5em`  Deploy in your cloud
        :link: cloud
        :link-type: doc

        Deploy your model in your cloud using the provided Docker image.

    .. grid-item-card:: :material-outlined:`exit_to_app;1.5em`  Deploy external models
        :link: external
        :link-type: doc

        Deploy models from external marketplaces (BioImage Model Zoo).

    .. grid-item-card:: :fas:`brain;fa-lg sd-mr-2`  Deploy your own LLM
        :link: llm
        :link-type: doc

        Deploy your own LLM from a selection of open-source models (DeepSeek, Qwen, LLama, etc),
        using vLLM and Open-WebUI.


.. toctree::
   :maxdepth: 1
   :titlesonly:
   :hidden:

   Overview <overview>
   Deploy in AI4OS (serverless) <oscar>
   Deploy in AI4OS (dedicated) <nomad>
   Deploy in your cloud <cloud>
   Deploy external models <external>
   Deploy your own LLM <llm>
