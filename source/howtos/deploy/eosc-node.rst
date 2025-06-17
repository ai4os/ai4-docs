Deploy a model on the EOSC EU Node
==================================

.. admonition:: Requirements
   :class: info

   * This tutorial requires access to the EOSC EU Node and the usage of available credits in your account.


This tutorial summarizes how to deploy a pre-trained AI model from the AI4EOSC Marketplace in the `EOSC EU Node <https://open-science-cloud.ec.europa.eu/>`__, to be used for inference via the :doc:`DEEPaaS API </reference/api>`.

For this, we will use the **Tools Hub** functionality of the EOSC EU Node, which allows us to deploy customized virtual infrastructures via TOSCA Templates on the available Cloud resources.
The Tools Hub currently supports two deployment options:

.. list-table::
    :header-rows: 1

    * - Option
      - ✅ Pros
      - ❌ Cons
    * - :ref:`Container <howtos/deploy/eosc-node:Option 1: Deploy in a Container>` (OKD-based)
      - - Fast deployment times,
        - Endpoint exposed in a DNS name.
      - - No access to the execution environment (managed platform).
        - Does not support deployments with GPUs
    * - :ref:`Virtual Machine <howtos/deploy/eosc-node:Option 2: Deploy in a Virtual Machine>` (Openstack-based)
      - - Full access to the execution environment (via SSH login).
        - Supports deployments with GPUs
      - - Longer deployment time,
        - Endpoint exposed in an IP, without a DNS name.

Based on your requirements, you can select the one who best fits your usecase.

.. TODO: when all changes are applied, rerecord and upload to youtube
.. https://drive.google.com/file/d/1232s6kfq2jcDnTv_kMv7rC1Zx1Axb7GX/view?resourcekey
.. https://drive.google.com/file/d/1DU4sHYtFvscr5dp1V6NYZ3mBwhzRXvnR/view?resourcekey__

.. check names of static images

Option 1: Deploy in a Container
-------------------------------

1.1. Allocate the computing resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You need to create your *“Default Personal Project”*. For this:

* Login into the `EOSC EU Node <https://open-science-cloud.ec.europa.eu/>`__,
* In the :material-outlined:`cloud;1.5em` ``Cloud Container Platform`` section (left panel), chose the **Small** environment by clicking ``Run``. OKD reserves the corresponding quota for your user,
* Choose the time period and press ``Submit``.

Notice that in this step what you do is to allocate the resources (quota), but you are not actually deploying them.

.. image:: /_static/images/eosc-node/container-allocate.png

1.2. Deploy your tool
^^^^^^^^^^^^^^^^^^^^^

In the :material-outlined:`account_tree;1.5em` ``Tools Hub`` section (left panel), search for ``AI4EOSC`` and select the **AI4EOSC Module Containers** (uploaded by platform developer *Miguel Caballer*).

.. image:: /_static/images/eosc-node/tools-hub.png

Clicking the :material-outlined:`map;1.5em` ``Show details`` button, you will be able to see additional information about the tool.

.. image:: /_static/images/eosc-node/tools-details.png

Deploy it using the :material-outlined:`play_circle;1.5em` ``Play`` button.

You can set custom input values by selecting :material-outlined:`check_box;1.5em` ``customize input values and save to new tool`` checkbox. This allows to configure the deployment parameters, in particular:

* the docker **model image** (available in the :fab:`docker` **Docker** value in the :ref:`Marketplace module details <reference/dashboard:Making a deployment>`)
* the amount of **resources** (CPU and RAM)
* the **endpoint** where the model will be exposed

.. image:: /_static/images/eosc-node/container-config.png
   :width: 400px

Then click on ``Save and Select Project``. This will create a new tool in your private ``My Tools`` tab, that you can use for new deployments.
Next, you need to select the *“Default Personal Project”* :ref:`created in Step 1 <howtos/deploy/eosc-node:1.1. Allocate the computing resources>`, which is linked to the allocated OKD project, and click on the ``Proceed`` button.

.. image:: /_static/images/eosc-node/container-deploy.png
   :width: 400px


1.3. Access the tool
^^^^^^^^^^^^^^^^^^^^

Once ready, the new deployment will available in the ``Deployments`` tab of the :material-outlined:`account_tree;1.5em` ``Tools Hub`` section.

.. image:: /_static/images/eosc-node/new-container-toolshub.png

Clicking the :material-outlined:`map;1.5em` ``Show details`` button, you will find the deployment endpoint (similar to ``https://yolo-ai4eosc-9ina.eu-1.open-science-cloud-user-apps.eu/ui``). In the endpoint, you will find the :doc:`DEEPaaS API </reference/api>` UI, which you can use to run inference calls on the model.

.. image:: /_static/images/endpoints/deepaas.png
   :width: 400px

1.4. Managing the resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Optionally, you can get additional information about your container. For that, go to the :material-outlined:`cloud;1.5em` ``Cloud Container Platform`` section in the EOSC EU Node dashboard, select your allocated environment and click on :material-outlined:`open_in_new;1.5em` ``View externally``.

.. image:: /_static/images/eosc-node/container-external.png

By clicking on this option, you will have access to your allocated environment in the EOSC EU Node Container provider, based in OKD.

.. image:: /_static/images/eosc-node/container-details.png

Finally, once you have finished using the AI model, you can delete the deployment and release the resources. For that, go to the ``Deployments`` section in the :material-outlined:`account_tree;1.5em` ``Tools Hub`` section and remove it by clicking on the :material-outlined:`delete;1.5em` ``Trash`` button.

If you no longer want to deploy additional containers, you should release the allocated project, to avoid using credits. For that, go back again to the :material-outlined:`cloud;1.5em` ``Cloud Container Platform`` section and release your allocated environment by clicking on the ``Release`` button. A notification will be sent by the system once the resources have been released.


Option 2: Deploy in a Virtual Machine
-------------------------------------

2.1. Allocate the computing resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You need to create your *“Default Personal Project”*. For this:

* Login into the `EOSC EU Node <https://open-science-cloud.ec.europa.eu/>`__,
* In the :material-outlined:`token;1.5em` ``Virtual Machines`` section (left panel), chose the **Small** environment. OpenStack creates the corresponding project with the selected quota,
* Click ``Run``, choose the time period and press ``Submit``.

Notice that in this step what you do is to allocate the resources (quota), but you are not actually deploying them.

.. image:: /_static/images/eosc-node/vm-allocate.png

2.2. Deploy your tool
^^^^^^^^^^^^^^^^^^^^^

In the :material-outlined:`account_tree;1.5em` ``Tools Hub`` section (left panel), search for ``AI4EOSC`` and select the **AI4EOSC Module VM** (uploaded by platform developer *Miguel Caballer*).

.. image:: /_static/images/eosc-node/tools-hub.png

Deploy it using the :material-outlined:`play_circle;1.5em` ``Play`` button.

You can set custom input values by selecting :material-outlined:`check_box;1.5em` ``customize input values and save to new tool`` checkbox. This allows to configure the deployment parameters, in particular:

* the docker **model image** (available in the :fab:`docker` **Docker** value in the :ref:`Marketplace module details <reference/dashboard:Making a deployment>`)
* the amount of **resources** (CPU and RAM)
* the **GPU** support, if needed

.. image:: /_static/images/eosc-node/vm-config.png

Then click on ``Save and Select Project``. This will create a new tool in your private **My Tools** list, that you can use for new deployments.
Next, you need to select the *“Default Personal Project”* :ref:`created in Step 1 <howtos/deploy/eosc-node:2.1. Allocate the computing resources>`, which is linked to the allocated OpenStack project.

.. image:: /_static/images/eosc-node/tools-deploy.png
   :width: 500px

Press the ``Proceed`` blue button and you will get a confirmation message about the deployment.

2.3. Access the tool
^^^^^^^^^^^^^^^^^^^^

The new deployment is available in the ``Deployments`` tab of the  :material-outlined:`account_tree;1.5em` ``Tools Hub`` section.

Clicking the :material-outlined:`map;1.5em` ``Show details`` button, you will find the deployment endpoint (similar to ``https://62.3.174.94/ui``)

.. image:: /_static/images/eosc-node/tool-output.png
   :width: 400px

.. warning::

  Please note that, in the case of Virtual Machines, it will take up to 10 minutes to deploy and configure the VM for the endpoint to be ready. You can periodically try to connect until you'll eventually have access to the Swagger DEEPaaS UI.

In the endpoint, you will find the :doc:`DEEPaaS API </reference/api>` UI, which you can use to run inference calls on the model.

.. image:: /_static/images/endpoints/deepaas.png
   :width: 400px

2.4. Managing the resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Optionally, you might want to get additional information about your VM. For that, go to the :material-outlined:`token;1.5em` ``Virtual Machines`` section in the EOSC EU Node dashboard, select your allocated environment and click on :material-outlined:`open_in_new;1.5em` ``View externally``.

.. image:: /_static/images/eosc-node/vm-allocated.png

By clicking on this option, you will have access to your allocated environment in the OpenStack cloud. Go to the ``Instances`` section to see your VM up and running:

.. image:: /_static/images/eosc-node/vm-details.png

You can obtain further information of your VM by clicking on the ``Instance Name`` of your resource.

Finally, once you have finished using the AI model, you can delete the deployment and release the resources. For that, go to the ``Deployments`` tab in the :material-outlined:`account_tree;1.5em` ``Tools Hub`` section and remove it by clicking on the :material-outlined:`delete;1.5em` ``Trash`` button.

.. image:: /_static/images/eosc-node/tools-delete.png

If you no longer want to deploy additional VMs, you should release the allocated project, to avoid using credits. For that, go back again to the :material-outlined:`token;1.5em` ``Virtual Machines`` section and release your allocated environment by clicking on the ``Release`` button. A notification will be sent by the system once the resources have been released.

More
----

.. dropdown:: ㅤ 💡 Further customize the Tool deployment

  If you need to further customize the AI4EOSC model deployments, you can modify the reference TOSCA templates that were used to create the Tools in the Tool Hub:

  * `TOSCA VM example <https://github.com/grycap/tosca/blob/eosc_lot1/templates/ai4eoscvm.yaml>`__.
  * `TOSCA Container example <https://github.com/grycap/tosca/blob/eosc_lot1/templates/ai4eosc_app.yaml>`__.

  To register this new tool, create a new Tool inside the ``Tools Hub`` section of the EOSC EU Node portal.

  .. image:: /_static/images/eosc-node/register-tool.png

  Fill the form and register the tool. Once registered, you can make it public and share it among the community. Notice the TOSCA Template needs to undergo a security assessment before it appears in the public catalog of Tools. This security assessment is periodically reassessed.
