:orphan:

.. _dashboard:

AI4EOSC Dashboard
=================

The Dashboard allows users to access computing resources to deploy, perform inference,
and train modules hosted at the Marketplace.
The Dashboard simplifies the deployment and hides some of the technical parts that most
users do not need to worry about.

.. admonition:: Where can I access the Dashboard?
   :class: info

   Currently, the following platforms have deployed a version of the Dashboard.
   You should access one of those Dashboards depending on the project you are a member of:

   * `AI4EOSC Dashboard <https://dashboard.cloud.ai4eosc.eu>`__ 👈 *(use this one if you are unsure which one to use)*
   * `iMagine Dashboard <https://dashboard.cloud.imagine-ai.eu>`__
   * `AI4Life Dashboard <https://ai4life.cloud.ai4eosc.eu>`__
   * `KMD4EOSC Dashboard <https://kmd4eosc.cloud.ai4eosc.eu/>`__
   * `Tutorials Dashboard <https://tutorials.cloud.ai4eosc.eu>`__

The Dashboard has a two views:

* a **public view** that let's you browse through the modules
* a **private view** that additionally allows you to make deployments based on those
  modules and check the statistics.
  To access this view you need :doc:`authentication </reference/user-access-levels>`.

In the remaining part of this section we will assume you have access to this private view.

.. grid:: 2
    :gutter: 3

    .. grid-item-card:: :material-outlined:`storefront;1.5em` Catalog
        :link: /dashboard/catalog
        :link-type: doc

        Browse the Modules, Tools and LLM catalogs in the Marketplace.

    .. grid-item-card:: :material-outlined:`rocket_launch;1.5em` Deployments
        :link: /dashboard/deployments
        :link-type: doc

        Learn how to make deployments, configure hardware, and connect storage.

    .. grid-item-card:: :material-outlined:`bar_chart;1.5em` Statistics
        :link: /dashboard/statistics
        :link-type: doc

        View platform usage metrics, datacenters, and footprint information.

    .. grid-item-card:: :material-outlined:`account_circle;1.5em` Profile & more
        :link: /dashboard/profile
        :link-type: doc

        Manage your profile details, linked services, authorizations, and Ask AI.
