Deploy a model on your own cloud resources
==========================================

.. admonition:: Requirements
   :class: info

   🔓 You need a :doc:`platform account </getting-started/register>` with :ref:`basic access level <reference/user-access-levels:Basic access level>`.

As every module available in the Marketplace is open-source, we offer the possibility
to automatically deploy it in your custom cloud resources using the
`EGI Infrastructure Manager <https://im.egi.eu>`__.
This feature is available to any registered user (:doc:`/reference/user-access-levels`).

.. list-table::
    :header-rows: 1

    * - ✅ Pros
      - ❌ Cons
    * - - You control where you deploy (no need to be an AI4OS member).
      - - More work to configure the deployment,
        - You are consuming resources even when not actively making predictions (if not deployed as serverless).

For this, :ref:`select a module in the Marketplace <dashboard_marketplace>` and click on ``Deploy ▼ IM``.

.. image:: /_static/images/dashboard/module.png

This will forward you to the Infrastructure Manager, with the module already selected.

.. image:: /_static/images/im/configure.png

If you are not logged in, you will be prompted to log in with your EGI Check-in account.

If you do not have any cloud provider configured, you will be prompted to configure them.
You can do so by clicking on the ``Add`` button.

.. image:: /_static/images/im/configure_no_cloud.png

You can then select any of the cloud providers supported by the IM,
and fill in the required information (e.g. Access and Secret Key in case of AWS).

.. image:: /_static/images/im/providers.png

Finally, you can select the cloud provider you want to use,
and the base image you want to use for the deployment.

.. image:: /_static/images/im/configure_cloud.png

After clicking on ``Submit``, the deployment will start.
Then afther a few minutes, the VM will be deployed and the AI4EOSC module
configured and you will be able to use it.

.. image:: /_static/images/im/inf_list.png

When the status changes to ``Configured``, you can click on ``Outputs`` button
to see the endpoint of DEEPaaS API UI of the module.

.. image:: /_static/images/im/outputs.png

Click on the link and you will see the API documentation, where you can test the module's
functionality, as well as perform other actions.

.. image:: /_static/images/im/deepaas_api.png