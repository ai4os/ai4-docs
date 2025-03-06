Composing AI Inference pipelines based on OSCAR services with Elyra in EGI Notebooks
====================================================================================

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; margin-bottom: 2em; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/watch?v=AP396k5t8WA" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

.. image:: /_static/images/elyra/elyra_icon.png
    :width: 500
    :align: center

In this documentation, we provide a hands-on guide to using
`Elyra <https://elyra.readthedocs.io/en/latest/>`__ ,
an AI-centric extension for `Jupyter Notebooks <https://jupyter.org/>`__ ,
within `EGI Notebooks <https://notebooks.egi.eu/hub/welcome>`__.

This tutorial will focus on:

* how to use Elyra in EGI Notebooks
* how to clone repositories using Elyra
* how to interact with `OSCAR <https://github.com/grycap/oscar>`__,  using the EGI Notebook Token.
* how to deploy a pipeline to utilize inference services using OSCAR.

.. image:: /_static/images/elyra/cowsay_example.png

We will walk through the entire process, from setting up the initial environment to
running specific OSCAR services like the Cowsay and others.


1. Setting up the environment
-----------------------------

1.1 Accessing EGI notebooks
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The first step is to access the `EGI Notebooks service <https://notebooks.egi.eu>`__.
Then choose the preferred server option. We will select ``Default EGI environment``:

.. image:: /_static/images/elyra/egi_notebooks_server_options.png

For additional information on using EGI Notebooks, refer to the
`official documentation <https://docs.egi.eu/users/dev-env/notebooks/>`__.

1.2 Importing OSCAR Elyra from Github
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To get started, you will need to clone the repository that contains the example files
for Elyra and OSCAR services: https://github.com/ai4os/ai4-compose

You can use the Elyra git tool on the left side panel to clone the repository in the
EGI Notebooks environment.
This repository contains various examples, including those for Elyra, such as Cowsay,
Grayify, and Plants-Theano.

.. image:: /_static/images/elyra/elyra-git.png

.. image:: /_static/images/elyra/cloning_repo_elyra.png


2. Prerequisites for all the examples
-------------------------------------

2.1 Types of recipes
^^^^^^^^^^^^^^^^^^^^

To use the nodes that employ OSCAR, it is necessary to invoke a service.
This service has two recipes:

1. The first recipe solely uses an EGI Check-in token.
   This is the best option if you use the `AI4EOSC OSCAR cluster <https://inference.cloud.ai4eosc.eu>`__
   authenticating :doc:`with your EGI account </reference/user-access-levels>`.

2. The second recipe uses our own credentials: node ID, endpoint, username, and password.
   This is an alternative for when you want to use your own OSCAR clusters.

2.2 How to use the EGI Token
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you wish to use the EGI token, there's no need to use or create a script that saves
credentials. To access your token:

1. Open the notebook node named ``oscar_cowsay.ipynb``.
2. Add a new cell immediately after the library import cell.

.. image:: /_static/images/elyra/get_egi_token.png

3. Enter the following code into the new cell:

.. code:: python

    with open("/var/run/secrets/egi.eu/access_token") as f:
        access_token = f.read()

2.3 How to create our own credentials
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before running any example, we need to create a credentials node in Elyra,
required to invoke a service in an OSCAR cluster.
For this example, we already have a node that assists in generating credentials,
named ``generate_credentials.py``. This node will handle the environment variables
necessary to interact with your OSCAR cluster.

Here's how to use it:

1. Open the cowsay example, searching it in the left panel, inside the ``ai4-compose``
   folder that we have previously cloned.

   The path is: ``ai4-compose/elyra/examples/cowsay/cowsay.pipeline``

2. Right click on the node ``Generate Credentials``, and select the ``Open Properties``
   option. This opens a right side panel.

3. In this panel, you need to set up the environment variables:
   ``ID``, ``ENDPOINT``, ``USERNAME``, and ``PASSWORD``.

.. image:: /_static/images/elyra/creating_credentials_1.png

4. Save these as a JSON file and name it ``credentials.json``.

.. image:: /_static/images/elyra/creating_credentials_2.png

This JSON file will be sent as an environment variable to the subsequent nodes in your
workflow.


3. Deploying a pipeline
-----------------------

3.1 Running the Cowsay Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now let's get our cow to talk! Follow these steps to set up the workflow in Elyra:

1. Use the cowsay service node and connect it to the previous node (if the node is
   not already connected).
2. Pass the ``credentials.json`` and the text for the cow (eg. ``moo``) as environment
   variables.

.. image:: /_static/images/elyra/cowsay_variables.png

3. Use the start button to execute the pipeline

.. image:: /_static/images/elyra/how_to_start_elyra_pipeline.png

4. After setting up the environment variables, proceed to the notebook within this
   node. Once executed, the notebook should display the cow uttering the text you
   provided.

.. image:: /_static/images/elyra/cowsay_output.png


3.2 Additional Examples: Grayify and Plants-Theano
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /_static/images/elyra/others_examples.png

You have more examples available in the Github repo to test the composing of functions
for inference with OSCAR.

For all the examples, you'll again need the credentials node to send the necessary
variables.
Additionally, other nodes will be involved to perform tasks like converting images to
and from Base64 format.
