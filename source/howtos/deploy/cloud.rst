Deploy a model on your own cloud resources
==========================================

As every module available in the Marketplace is open-source, we offer the possibility
to automatically deploy it in your custom cloud resources using the
`EGI Infrastructure Manager <https://im.egi.eu>`__.
This feature is available to any registered user (:doc:`/reference/user-access-levels`.

.. list-table::
    :header-rows: 1

    * - ✅ Pros
      - ❌ Cons
    * - - You control where you deploy (no need to be an AI4OS member).
      - - More work to configure the deployment,
        - You are consuming resources even when not actively making predictions (if not deployed as serverless).

For this, :ref:`select a module in the Marketplace <dashboard_marketplace>` and click on ``Deploy ▼ IM``.

.. image:: /_static/images/dashboard/module.png

This will forward you to the Infrastructure Manager, where you will be able to
select your own cloud resources to deploy.

.. image:: /_static/images/im/configure.png

.. image:: /_static/images/im/providers.png
