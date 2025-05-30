Deploy a model on the ESOC EU Node
==================================

.. admonition:: Requirements
   :class: info

   🔒 This tutorial requires access to the EOSC EU Node and the usage of available credits in your account. `More information <https://open-science-cloud.ec.europa.eu/>`__.

This tutorial summarizes how to deploy a pre-trained AI model from the AI4EOSC Marketplace in the EOSC EU Node to be used for inference via the DEEPaaS API. For this, we will use the Tools Hub functionality of the EOSC EU Node, which allows us to deploy customized virtual infrastructures via TOSCA Templates on the available Cloud resources.

The Tools Hub provides a catalog of TOSCA templates for the Application Workflow Manager (based on the `Infrastructure Manager <https://im.egi.eu/>`__ technology) to deploy customized virtual infrastructures on the available Cloud resources. Two kind of deployments are supported in the EOSC EU Node: *Virtual Machines* (VMs), which run on OpenStack-based Clouds and *containers*, which run on managed OKD-based platforms. Let's analyze both options in the next tables.

.. list-table::
    :header-rows: 1

    * - ✅ VMs Pros
      - ❌ VMs Cons
    * - - You can login via SSH to the VM and, therefore, have full access to the execution environment.
      - - Longer deployment time,
        - Endpoint exposed in an IP, without a DNS name.


.. list-table::
    :header-rows: 1

    * - ✅ Containers Pros
      - ❌ Containers Cons
    * - - Fast deployment times,
        - Endpoint exposed in a DNS name.
      - - Managed platform, no access to the execution environment.

This page describes the procedures to support both approaches. It also includes the instructions to register an AI4EOSC Model as a tool in the EOSC EU Node and the instructions on how to deploy those previously registered tools to be used for AI inference in the resources of the EOSC EU Node. 

1. Procedure to Register the AI4EOSC Model as a Tool in the EOSC EU Node
------------------------------------------------------------------------
Step 0. Create the TOSCA template
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There has to be a TOSCA Template for each AI4EOSC Model to be deployed. The TOSCA template depends on the kind of resources you want to deploy the model (VM or container). You can find two examples here:

 * `TOSCA VM example <https://github.com/grycap/tosca/blob/eosc_lot1/templates/ai4eoscvm.yaml>`__. 
 * `TOSCA Container example <https://github.com/grycap/tosca/blob/eosc_lot1/templates/ai4eosc_app.yaml>`__.  

Step 1. Register the TOSCA template in the Tools Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Create a new Tool inside the ``Tools Hub`` section of the EOSC EU Node portal.

.. image:: /_static/images/eoscnode/register-tool.png

Fill the form and register the tool. Once registered, you can make it public and share it among the community. Notice the TOSCA Template needs to undergo a security assessment before it appears in the public catalog of Tools. This security assessment is periodically reassessed.


2. Procedure to Deploy the Model in a Virtual Machine in the EOSC EU Node
-------------------------------------------------------------------------

The next subsections are a tutorial to learn how to deploy an AI model of the AI4EOSC Marketplace in the EOSC EU Node. 

Step 0. Log into the EOSC EU Node and allocate the computing resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Start by logging in to the EOSC EU Node `here <https://open-science-cloud.ec.europa.eu/>`__.
Then, you need to allocate your Virtual Machine. Go to the **Virtual Machines** section for that. We reccomend you to choose a *Small* VM.
What happens underneeth is that OpenStack creates the corresponding project with the selected quota for your user. This is called your “Default Personal Project”.
Allocate the environment by clicking the ``Run`` button.

.. image:: /_static/images/eoscnode/allocate-vms.png

Notice that in this step what you do is to allocate the resources (quota), but you are not actually deploying them. 

Step 1. Choose the tool to deploy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now, go to the Tools Hub and select the Tool from the ``All Tools`` section. You can use the searcher to find the AI4EOSC tools already created. If you want, you can flag them as favourite. 

.. image:: /_static/images/eoscnode/tools-hub.png

Choose the desired tool. You can see the details with the ``Show details`` button.

.. image:: /_static/images/eoscnode/tools-details.png

Step 2. Deploy the tool
^^^^^^^^^^^^^^^^^^^^^^^

Deploy the desired tool by using the :material-outlined:`play;1.5em` ``Play`` button. 
You can set custom input values by clicking on the “customize input values and save to new tool” checkbox. This enables the modification of the AI4EOSC model to deploy and the amount of computational resources to assing to the VM. So this is the way to **easily deploy any of the AI models available in the marketplace**.
If selected, the next fields appear:

.. image:: /_static/images/eoscnode/tool-vmcustom.png

Modify them as desired and then click on the ``Save and Select Project`` button. It will create a new tool in your private **My Tools** list, that you can use for new deployments.
Next, you need to select the Default Personal Project created in Step 0, which is linked to the allocated OpenStack project.

.. image:: /_static/images/eoscnode/tools-deploy.png

Press the ``Proceed`` blue button and you will get a confirmation message about the deployment.
Once deployed, in the ``Deployments`` tab (inside the Tools Hub), it will appear a new entry corresponding with your new Deployment.

Step 3. Access the tool
^^^^^^^^^^^^^^^^^^^^^^^

You will see the endpoint of the deployed tool in the ``additional information`` option.

.. image:: /_static/images/eoscnode/tool-output.png

For the AI4EOSC AI models, if you access the endpoint provided, you will get a Swagger interface to use the model.
Please note that, in the case of Virtual Machines, it will take up to 10 minutes to deploy and configure the VM for the endpoint to be ready. You can periodically try to connect until you’ll eventually have access to the Swagger DEEPaaS UI.

.. image:: /_static/images/eoscnode/example-deepaasui.png

Once you can access the Swagger interface in your browser, you can trigger the inference of the model by uploading the proper input (for example, for the YOLO model, you have to upload the image where you want to detect objects).

Step 4. Managing the resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Optionally, you might want to get additional information about your VM. For that, go to the ``Virtual Machines`` section in the EOSC EU Node dashboard, select your allocated environment and click on ``View externally``.

.. image:: /_static/images/eoscnode/resource-details.png

By clicking on this option, you will have access to your allocated environment in the OpenStack cloud. Go to the ``Instances`` section to see your VM up and running:

.. image:: /_static/images/eoscnode/vm-details.png

You can obtain further information of your VM by clicking on the ``Instance Name`` of your resource.

Finally, to **terminate** the resources, you can go to the ``Deployments`` section in the Tools Hub and remove it by clicking on the :material-outlined:`trash;1.5em` ``Trash`` button. Eventually, the entry will disappear.
If you no longer want to deploy additional VMs, you should release the allocated project. For that, go back again to the ``Virtual Machines`` section and release your allocated environment by clicking on the ``Release`` button. A notification will be sent by the system once the resources have been released.

3. Procedure to Deploy the Model in a Container in the EOSC EU Node
-------------------------------------------------------------------

Now let's have a look on the steps to deploy an AI model from the AI4EOSC Marketplace in **Cloud Container Platform** offered by the EOSC EU Node.
You can see a video demo `here <https://drive.google.com/file/d/1232s6kfq2jcDnTv_kMv7rC1Zx1Axb7GX/view?resourcekey>`__. You will that the process is very similar to the previous one, let's detail the steps!

Step 0. Log into the EOSC EU Node and allocate the computing resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the case of **Containers**, OKD reserves the corresponding quota for your user. In the ``Cloud Container Platform`` section, chose the *Small* environment and click ``Run``. You will have to choose the time period and press *Submit*.

.. image:: /_static/images/eoscnode/allocate-container.png

This creates your “Default Personal Project”.

Step 1. Choose the tool to deploy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the ``Tools Hub`` section, a publicly available tool has been created named *AI4EOSC Plants specifies classifier* to deploy the AI model in OKD. This tool corresponds with the `Plants Species Classifier AI model <https://dashboard.cloud.ai4eosc.eu/catalog/modules/plants-classification>`__.
Remember that you can see the details of the tool with the ``Show details`` button.

Step 2. Deploy the tool
^^^^^^^^^^^^^^^^^^^^^^^

As with the VMs, you can deploy the tool by using the :material-outlined:`play;1.5em` ``Play`` button. 
Again, you can set custom input values by clicking on the “customize input values and save to new tool” checkbox. This enables the modification of the AI4EOSC model to deploy and the amount of computational resources to assing to the container. So this is the way to **easily deploy any of the AI models available in the marketplace**.
You can see a video demo on how to modify the tool with other AI model `here <https://drive.google.com/file/d/1DU4sHYtFvscr5dp1V6NYZ3mBwhzRXvnR/view?resourcekey>`__.

.. image:: /_static/images/eoscnode/tool-containercustom.png

Modify them as desired and then click on the ``Save and Select Project`` button. It will create a new tool in your private **My Tools** list, that you can use for new deployments.
Next, you need to select the Default Personal Project created in Step 0, which is linked to the allocated OKD project.

Step 3. Access the tool
^^^^^^^^^^^^^^^^^^^^^^^
The new deployment is available in the ``Deployments`` tab of the **Tools Hub** section. You can access the outputs of this deployment to get the endpoint (for example ``https://plants-ai4eosc-9ina.eu-1.open-science-cloud-user-apps.eu/ui``).
In containers, the deployment should be very fast compared with VMs. Indeed, if a user recently deployed the same model (same Docker image) the deployment will be even faster. 

If you paste the endpoint of the deployment in your browser, you will get the Swagger interface of the AI model's DEEPaaS API, so you can easily trigger the inference of the model. 

Step 4. Managing the resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Optionally, you can get additional information about your container. For that, go to the ``Cloud Container Platform`` section in the EOSC EU Node dashboard, select your allocated environment and click on ``View externally``.
By clicking on this option, you will have access to your allocated environment in the EOSC EU Node Container provider, based in OKD.

.. image:: /_static/images/eoscnode/container-details.png

Finally, once you have finished using the AI model, you can delete the deployment and release the resources. For that, go to the ``Deployments`` section in the Tools Hub and remove it by clicking on the :material-outlined:`trash;1.5em` ``Trash`` button. Eventually, the entry will disappear (and so the container from the OKD platform).
If you no longer want to deploy additional containers, you should release the allocated project, to avoid using credits. For that, go back again to the ``Cloud Container Platform`` section and release your allocated environment by clicking on the ``Release`` button. A notification will be sent by the system once the resources have been released.

