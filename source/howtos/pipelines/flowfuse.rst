Composing AI Inference pipelines with Node-RED & Flowfuse
=========================================================

.. dropdown:: :fab:`youtube;youtube-icon` ㅤCreate a pipeline with Flowfuse

   .. raw:: html

      <div style="position: relative; padding-bottom: 56.25%; margin-bottom: 2em; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/9a019SA5GW4" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
      </div>

   :material-outlined:`error;1.5em` Please, be aware that video demos can become quickly outdated. In case of doubt, always refer to the written documentation.

.. admonition:: Deprecation notice
    :class: info

    *  **OSCAR v3.6.5** now provides support for deploying a Node-RED instance. More info regarding this new OSCAR feature can be found `here <https://docs.oscar.grycap.net/latest/integration-node-red/>`__ .
    * The Flowfuse instance of the project is **no longer available**. You can test the examples directly in OSCAR, deploying your own Node-RED instance with OSCAR nodes already integrated.
    * The current version of the tutorial will be updated soon. Stay tuned!


In this document, we will learn about Composing AI Inference pipelines based on OSCAR
services with Node-RED & FlowFuse, specifically:

* how to register on the FlowFuse platform for AI4EOSC,
* how to join a team,
* how to create our first application and Node-RED instance,
* how to deploy a workflow to utilize inference services using OSCAR.

For a complete overview of the Node-RED and FlowFuse examples, please refer to the `GitHub README <https://github.com/ai4os/ai4-compose/blob/main/node-red/README.md>`__.

First of all, let's understand what FlowFuse, Node-RED and OSCAR are:

* `Node-RED <https://nodered.org/>`__ is an open-source visual programming tool.
  Built on Node.js, it allows users to create event-driven systems by connecting nodes
  representing different functionalities. With a user-friendly web interface and a rich
  library of pre-built nodes, Node-RED simplifies the visual composition of pipelines.
* `FlowFuse <https://flowfuse.com/>`__ adds to Node-RED: collaborative development,
  management of remote deployments, support for DevOps delivery pipelines, and the
  ability to host Node-RED applications on FlowFuse. FlowFuse is the DevOps platform
  for Node-RED application development and delivery.
* `OSCAR <https://oscar.grycap.net/>`__ is an open-source serverless platform to support
  scalable event-driven computations.
  See the our documentation on :doc:`how to make an inference in OSCAR </howtos/deploy/oscar>`
  for more information.

In AI4OS, we use Node-Red to visually compose AI model inference pipelines.
A managed instance of FlowFuse is also available for users to self-provision
their Node-Red instances on which they can compose these pipelines.
Specific custom nodes have been created to perform AI model inference on remote
OSCAR clusters.

Let's understand the most relevant concepts in FlowFuse:

* **Teams:** Users are grouped into Teams, which are central to FlowFuse's
  organizational structure.
  Each team can encompass multiple members, and users can be part of multiple teams.
* **Applications:** Teams create Applications, which are collections of one or
  more Node-RED instances.
  There is an application already created in the FlowFuse instance named ``AI4EOSC-Dev``.
* **Instances:** Creating an instance out of the ``OSCAR Node-Red template`` will
  ensure the  dependencies required to interact with OSCAR clusters and the custom
  defined nodes for certain AI models from the AI4OS dashboard.
  Each instance is derived from a Template, providing default settings, and runs on a
  Stack that defines the Node-RED version, memory, and CPU usage.
* **Devices:** The FlowFuse platform can be used to manage Node-RED instances running
  on remote Devices.
  A Device runs a software agent that connects back to FlowFuse in order to receive updates.

These concepts collectively enable efficient management and deployment of Node-RED
instances and applications within the FlowFuse ecosystem. For more information,
check the `FlowFuse official documentation <https://flowfuse.com/docs/user/concepts>`__.


1. How to sign up in FlowFuse for AI4EOSC
-----------------------------------------

First and foremost, we need to access the `FlowFuse instance for AI4EOSC <https://forge.flows.dev.ai4eosc.eu>`__.
Once inside, we have to register and accept the `terms and conditions <https://ai4eosc.eu/platform/acceptable-use-policy/>`__.

.. image:: /_static/images/flows/1.png

Once registered, we will receive a confirmation email to our email address.

.. image:: /_static/images/flows/2.png

The email will contain a link that will help us confirm our email address.

.. image:: /_static/images/flows/3.png

Once we use the link, our email will be confirmed, and we will be able to access the
platform using our credentials.

.. image:: /_static/images/flows/4.png

To change your password you just have to access the user settings, click on the
security option.

.. image:: /_static/images/flows/18.png


2. Joining the Development Team
-------------------------------

After the email verification, we have to wait for the administrator to add us to
the AI4EOSC development team.

For the time being, the AI4EOSC's FlowFuse system administrator does not receive a
notification when a new user registers.
Therefore, you should request access by sending an e-mail to:

.. code::

    To: Diego Aguirre - dieagra@i3m.upv.es
    CC: Amanda Calatrava - amcaar@i3m.upv.es

.. image:: /_static/images/flows/5.png

Once the administrator accepts us into the AI4EOSC team, we will receive an email.
From that point on, we will be able to access the team's applications,
where we can access the existing Node-Red instances and also create our own instances.

.. image:: /_static/images/flows/6.png

Clicking on the invitation will allow us to see more details about the team invitation,
and we can join by clicking ``Accept,`` which will be revealed by clicking on the three
dots on the left of the information

.. image:: /_static/images/flows/7.png

After completing the registration and joining the AI4EOSC Dev team, we should be able
to see the team. If we have the owner role, we can create applications and deploy our
instances. However, if we are a member with the viewer role or a guest who can only
view the dashboards, we will need to inform the team administrator to change our role.
For more details about the roles, you can refer to the following image:

.. image:: /_static/images/flows/8.png
   :width: 600px


3. Creating our first application
---------------------------------

3.1 Configuring the application
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once our owner role is confirmed, we can create applications within the team.
To do so, we will click on the ``Create application`` option.

.. image:: /_static/images/flows/9.png

In the ``Create a New Application and Instance`` menu, we will need to provide a name
for our application, a description to identify its purpose, and then deploy the
first instance of the application.
The instance is given a randomly generated name, but it can be changed.
Please note that instance names cannot be changed once set, so make sure it is correct.

Lastly, ensure to select the OSCAR Node-RED template, which comes pre configured and
installed with modules for following the examples in the document and deploying
future projects using OSCAR.

Once we have finished with the configuration, we can click on the ``Create application``
button.

.. image:: /_static/images/flows/10.png

3.2 Creating new instances
^^^^^^^^^^^^^^^^^^^^^^^^^^

As we've seen, an Node-RED instance is created when we create an application,
but it's also possible to deploy additional instances within a created application.
In this case, we will click on the ``Add Instance`` button.

.. image:: /_static/images/flows/11.png

Once in the menu, you can select the instance name and the template.
Remember that the instance name cannot be changed, so ensure it is correct.
When everything is configured, click on the ``Create Instance`` button to create
and deploy it.

.. image:: /_static/images/flows/12.png

Now that the instance is created, you can monitor the creation process by selecting
it from the application menu.
As shown in the figure, it will be in the ``Starting`` status, indicating that it is
installing modules and other components of the template.
This process may take 1 to 2 minutes to complete.

.. image:: /_static/images/flows/13.png

3.3 Connecting an instance
^^^^^^^^^^^^^^^^^^^^^^^^^^

Once the instance is created, the next step is to join it.
You can do this by selecting the desired instance from the application menu and
then clicking on ``Open Editor``.
Alternatively, you can click on the instance and then select ``Open Editor`` from the
instance menu.

.. image:: /_static/images/flows/14.png

.. image:: /_static/images/flows/15.png

From this point on, the operation is the usual process as using Node-RED.

.. image:: /_static/images/flows/16.png

You will see at the bottom of the Node palette on the left, some custom nodes created to simplify performing the AI model inference on a remote OSCAR cluster. Note that the number of nodes will be updated progressively and according to the models developed in the project.

.. image:: /_static/images/flows/17.png

3.4 How to delete a Node-Red instance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To delete an instance, you have to be the owner of the team, applications,
and instances. Expand the actions menu and click on ``Delete``.

Always ensure that you have backed up any important data or configurations before
deleting an instance. Once deleted, the data associated with that instance may be
irretrievable.

.. image:: /_static/images/flows/36.png


4. Application examples
-----------------------

4.1 Toy workflow: OSCAR Cowsay
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We have now seen how to create an application, deploy a Node-RED instance,
and connect to it. Next, we will proceed to create a workflow to demonstrate the
functionality of the Node-RED tool.

For this first  toy example, we will use a module that takes text as input and returns an
ASCII art of a cow repeating the same text as output.

To set up this example, we will essentially need three nodes:
the Inject node, the OSCAR Cowsay node, and the Debug node.
The Debug node is used to visualize the result in the debug log.

To place the modules in the workspace, simply drag them from the left-hand side menu.
And finally, we connect the inputs and outputs of the modules as shown in the figure.

.. image:: /_static/images/flows/20.png

Once we have deployed the workflow, we need to configure each module.

For the Inject node, as shown in the figure, there are default parameters.
For the cowsay example, it is necessary to remove the topic since it will not be used.
Additionally, change the type of `msg.payload` to string and enter the desired text in
the box, in this case: ``Hello World!``

.. image:: /_static/images/flows/21.png
   :width: 800px

For the OSCAR Cowsay node, we need to select the endpoint of the OSCAR cluster we will
use and enter it in the ``Server`` section.
Additionally, we will select the name of the service in the cluster and enter the token.

.. image:: /_static/images/flows/22.png
   :width: 800px

For this example, we will use the endpoint ``https://inference.cloud.ai4eosc.eu``.
Additionally, to locate the service token, we just need to expand the details of
the service. (Remember: to access the platform, you need to have an :doc:`EGI account </reference/user-access-levels>`.)

.. image:: /_static/images/flows/23.png

Finally, the Debug node does not require any additional configurations,
so we can click on the ``Deploy`` button.
This will save the workflow, and it will be possible to start it.

.. image:: /_static/images/flows/24.png

Now, to start the workflow after deploying, you need to click on the small square next
to the Inject node on the left side. This will initiate the workflow and input the
string into the next node. After invoking the cowsay service, it will return the
modified cowsay string as output, which can be viewed in the debug window thanks to
the Debug node.

We have finished implementing the first workflow using an OSCAR node.

.. image:: /_static/images/flows/25.png

4.2 Plant Classification workflow with input preprocessing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this section, we will compose an example workflow for AI inference where
we will convert the color image of a plant to black and white and then classify
the plant to determine its species.

.. image:: /_static/images/flows/26.png
   :width: 600px

If we have started an instance with the OSCAR Node-RED template, we can use the
preconfigured modules of some OSCAR services.
To find them, we just need to go to the OSCAR section in the left side menu of Node-RED.

* **Node HTTP Request** is designed to execute an HTTP request to retrieve an image
  from a specified URL, which is provided as input. Once the image is downloaded,
  it becomes the output of this node.
* **Node OSCAR Grayify**, receives the image from the previous node as its input.
  Its primary function is to process the image to convert it into grayscale.
  After this, the processed image is sent to the OSCAR cluster for appropriate processing.
  The result from this node is the original image converted to grayscale, which is provided as output.
* **Node OSCAR Plants Classification** takes the grayscale image processed by Node 2 as
  input. This node is responsible for classifying the plant in the image using the OSCAR
  cluster. After processing, the node produces an output in JSON format, containing
  detailed information about the plant classification.

This processing sequence ensures a coherent and efficient workflow, optimizing image
classification through the integration of advanced technologies in each node.

Once the pipeline is organized, we will start configuring the components. To begin:

* The inject node does not need to be modified, since it is used to start the pipeline.
* The image preview nodes and the debug node should also not be modified.
* The http request node: set the method to GET, enter the image URL (for
  example: ``https://blog.agroterra.com/wp-content/uploads/2013/09/trigo-570x288.jpg``),
  configure the payload to be sent as a request body, and set the return to be a binary buffer.

.. image:: /_static/images/flows/27.png
   :width: 600px

Finally, we need to edit the OSCAR nodes, which have three fields, in the same way
we did in the Cowsay example.

.. image:: /_static/images/flows/28.png

If the result of Plant Classification appears as a buffer, you just need to select
the option to view the result in raw, allowing you to read the information correctly.

.. image:: /_static/images/flows/29.png
   :width: 600px


5. Importing to our instance
----------------------------------

5.1 Importing flows from Github
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now we will explain how to, step by step, recreate usage examples for OSCAR by
importing them from the GitHub repository.
In this case we will look up for the cowsay example.

First install the dependencies `described here <https://github.com/ai4os/ai4-compose/tree/main/node-red>`__.
Then, access to the `node-red repo <https://github.com/ai4os/ai4-compose/tree/main/node-red/modules>`__ and,
in this example, look for the ``grayify.json``.

.. image:: /_static/images/flows/30.png

.. image:: /_static/images/flows/31.png

.. image:: /_static/images/flows/32.png

.. image:: /_static/images/flows/33.png

Then, to import flows/subflows/nodes/examples in our node red instance, we can expand
the hamburger menu located in the top right corner and look for the fourth option:
``Import``.
Once this option is selected, a floating menu will appear where we can paste the JSON.

.. image:: /_static/images/flows/34.png

5.2 Importing modules via node red palette
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the case of importing other types of modules or nodes, we can expand the same menu,
but now we will go to the ``Manage palette`` option, which allows us to import from
the module installation menu.

Once in the ``Manage palette`` menu, you can search for the desired modules or nodes
and install them directly.
Ensure that the modules or nodes you're installing are compatible with your version of
Node-RED and come from trusted sources to maintain the integrity and security of your
environment.

After installation, it's good practice to test the new modules or nodes to ensure they
work as expected.

.. image:: /_static/images/flows/35.png
