Composing AI Inference pipelines with Node-RED
===============================================

.. (ignacio): Comment Flowfuse video tutorial until we record the new one with Node-Red.

.. .. dropdown:: :fab:`youtube;youtube-icon` ㅤCreate a pipeline with Flowfuse

..    .. raw:: html

..       <div style="position: relative; padding-bottom: 56.25%; margin-bottom: 2em; height: 0; overflow: hidden; max-width: 100%; height: auto;">
..         <iframe src="https://www.youtube.com/embed/9a019SA5GW4" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
..       </div>

..    :material-outlined:`error;1.5em` Please, be aware that video demos can become quickly outdated. In case of doubt, always refer to the written documentation.


In this document, we will learn about Composing AI Inference pipelines based on OSCAR
services with Node-RED, specifically:

* how to create inference services in OSCAR,
* how to create a new "Flows" instance (based on Node-RED) in the OSCAR platform for AI4EOSC,
* how to access the instance and create our first application workflow,
* how to deploy a workflow to call inference services deployed in OSCAR,
* how to delete the Node-RED instance.

For a complete overview of the Node-RED examples, please refer to the `AI4Compose GitHub README <https://github.com/ai4os/ai4-compose/blob/main/node-red/README.md>`__.

First of all, let's understand the key technologies involved in this tutorial:

* `Node-RED <https://nodered.org/>`__ is an open-source visual programming tool.
  Built on Node.js, it allows users to create event-driven systems by connecting nodes
  representing different functionalities. With a user-friendly web interface and a rich
  library of pre-built nodes, Node-RED simplifies the visual composition of pipelines.
* `OSCAR <https://oscar.grycap.net/>`__ is an open-source serverless platform to support
  scalable event-driven computations. From **OSCAR v3.6.5**, it provides support for deploying
  a Node-RED instance. More info regarding this new OSCAR feature can be found `here <https://docs.oscar.grycap.net/latest/integration-node-red/>`__ .

In AI4OS, we use Node-Red to visually compose AI model inference pipelines.
Specific custom nodes have been created to perform AI model inference on remote
OSCAR clusters.

1. Creating inference services in OSCAR
---------------------------------------
Let's start by creating an OSCAR service to use it from Node-RED.

1.1. Deploy YOLOv8 service
^^^^^^^^^^^^^^^^^^^^^^^^^^

Go to `OSCAR Dashboard <https://inference.cloud.ai4eosc.eu/ui/>`__ and,
in the ``Services`` panel, select ``Create service`` → ``FDL``. Use the
following configuration:

FDL:

.. code:: yaml

   functions:
     oscar:
     - oscar-cluster:
         name: yolov8-node-red
         memory: 4Gi
         cpu: '2.0'
         image: ai4oshub/ai4os-yolov8-torch:latest
         script: script.sh
         log_level: CRITICAL

Script:

.. code:: bash

   #!/bin/bash
   RENAMED_FILE="${INPUT_FILE_PATH}.png"
   mv "$INPUT_FILE_PATH" "$RENAMED_FILE"
   OUTPUT_FILE="$TMP_OUTPUT_DIR/output.png"
   deepaas-cli --deepaas_method_output="$OUTPUT_FILE" predict --files "$RENAMED_FILE" --accept image/png 2>&1
   echo "Prediction was saved in: $OUTPUT_FILE"

See the our documentation on :doc:`how to make an inference in OSCAR </howtos/deploy/oscar>`
for more information about creating OSCAR services.

2. Creating our Node-RED instance in OSCAR
------------------------------------------
1. In the `OSCAR Dashboard <https://inference.cloud.ai4eosc.eu/ui/>`__,
   go to the ``Flows`` panel and then click ``New``.

   .. image:: /_static/images/flows/node-red-deployed.png
      :alt: node-red-deployed.png

2. Enter the **admin** password that you will be asked to access later
   on this instance of Node-RED, and select or create a Bucket.

   .. image:: /_static/images/flows/node-red-dashboard.png
      :alt: node-red-dashboard.png

3. After deploying Node-RED, we access its user interface.

   .. image:: /_static/images/flows/node-red-dashboard-visit.png
      :alt: node-red-dashboard-visit.png


3. Accessing the Node-RED instance
----------------------------------
Once the Node-RED instance is up and running, you can log in with your credentials
(the user is always ``admin``).

.. image:: /_static/images/flows/node-red-login.png
   :alt: node-red-login.png


4. Creating a workflow in Node-Red
----------------------------------
We are going to showcase the usage of Node-RED with a simple example that uses the YOLO model. However, if you want to see some other examples, visit the `AI4Compose <https://github.com/ai4os/ai4-compose/tree/main>`__ repository.

4.1. Designing and creating the workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Let’s create a workflow that fetches an image from the Internet, makes a
request to the YOLO service and visualizes the result.

We need the following list of components from the Node-RED sidebar menu:

- **Common** → ``inject`` node
- **Network** → ``HTTP request`` node
- **Output** → ``image`` node
- **OSCAR** → ``OSCAR YOLO8`` node

.. figure:: /_static/images/flows/node-red-nodes.png
   :alt: node-red-nodes.png

Drag and drop the boxes to the canvas and then connect the components as
shown:

.. figure:: /_static/images/flows/node-red-workflow.png
   :alt: node-red-workflow.png

Now we need to configure the components. To configure the ``HTTP request
node`` double-click on it:

- ``URL``: URL of an image you want to analyze with YOLO (for example,
  you can use this
  `image <https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Cat_August_2010-4.jpg/640px-Cat_August_2010-4.jpg>`__)
- ``Payload``: ``Send as request body``
- ``Return``: *A binary buffer*

.. figure:: /_static/images/flows/node-red-node-http-request.png
   :alt: node-red-http-request.png

Configure the ``OSCAR YOLO8`` node:

- ``Server``: URL of the OSCAR cluster. You can get it from
  `OSCAR Dashboard <https://inference.cloud.ai4eosc.eu/ui/>`__ → ``Info``
  (Sidebar panel) → ``Endpoint``
- ``Service Name``: ``yolov8-node-red``
- ``Token``: Obtain the token from
  `OSCAR Dashboard <https://inference.cloud.ai4eosc.eu/ui/>`__ → ``Info``
  (Sidebar panel) → ``Access token``

.. figure:: /_static/images/flows/node-red-node-oscar-yolo.png
   :alt: node-red-node-oscar-yolo.png

4.2. Testing the workflow
^^^^^^^^^^^^^^^^^^^^^^^^^
After configuring your workflow, you can test it in the Node-RED Editor:
click ``Deploy`` (top right corner) and then click on the ``inject`` node:

.. figure:: /_static/images/flows/node-red-workflow-run.png
   :alt: node-red-workflow-run.png

You should see the result as indicated below.

.. figure:: /_static/images/flows/node-red-workflow-result.png
   :alt: node-red-workflow-result.png


5. How to delete a Node-Red instance
------------------------------------

To delete an instance, you have to click on the ``Delete`` button and confirm the operation.

   .. image:: /_static/images/flows/node-red-dashboard-delete.png
      :alt: node-red-dashboard-delete.png


   .. image:: /_static/images/flows/node-red-delete.png
      :alt: node-red-delete.png

The MinIO bucket remains available; however, it is a good practice to ensure that you have backed up any important data or configurations before
deleting an instance.
