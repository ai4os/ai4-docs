Deploy a model in production
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you have trained your model, you can deploy it in production. This section
provides several guides in how to deploy your model in different environments.


.. grid:: 1
    :gutter: 3

    .. grid-item-card::  Overview
        :link: overview
        :link-type: doc

        Start here to get an overview of the different deployment options.

    .. grid-item-card::  Deploy in the platform (serverless)
        :link: oscar
        :link-type: doc

        Deploy your model in the platform using the serverless option, using a shared
        serverless environment.

    .. grid-item-card::  Deploy in the platform (dedicated)
        :link: nomad
        :link-type: doc

        Deploy your model in the platform using a dedicated deployment and a load
        balancer.

    .. grid-item-card::  Deploy in your cloud
        :link: cloud
        :link-type: doc

        Deploy your model in your cloud using the provided Docker image.

    .. grid-item-card::  Manual serverless deployment
        :link: oscar-manual
        :link-type: doc

        Deploy your model in the platform using the serverless option, but manually
        configuring the deployment. This is an advanced option.


.. toctree::
   :maxdepth: 1
   :titlesonly:
   :hidden:

   Overview <overview>
   Deploy in AI4OS (serverless) <oscar>
   Deploy in AI4OS (dedicated) <nomad>
   Deploy in your cloud <cloud>
   Manual serverless deployment <oscar-manual>
