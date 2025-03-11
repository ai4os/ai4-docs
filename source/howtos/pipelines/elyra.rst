Composing AI Inference pipelines based on OSCAR services with Elyra in EGI Notebooks
====================================================================================

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; margin-bottom: 2em; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/AP396k5t8WA" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
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

2.1 Using OSCAR in Your Workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To use nodes that rely on OSCAR, you need to invoke a service through an OSCAR client.  
First, create your own OSCAR client, configuring it with the necessary credentials and parameters to interact with an OSCAR cluster.

2.2 Setting Up an OSCAR Client
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /_static/images/elyra/creating_client.png

To set up an OSCAR client, obtain the OSCAR endpoint. For AI4EOSC, the endpoint is:

`https://inference.cloud.ai4eosc.eu <https://inference.cloud.ai4eosc.eu>`__

The ID parameter is optional.

By default, the EGI notebook assigns a token automatically. However, if you cannot retrieve a token from an EGI notebook, you need to generate a refresh token from the EGI token page:

`EGI Check-in Token Portal <https://aai.egi.eu/token>`__

Follow these steps to generate a refresh token:

1. Authenticate on the EGI portal.
   
   .. image:: /_static/images/elyra/egi_token_1.png

2. Click the button to create a refresh token.
   
   .. image:: /_static/images/elyra/egi_token_2.png

3. Copy the generated refresh token.
   
   .. image:: /_static/images/elyra/egi_token_3.png
      
Once the client is set up, you can seamlessly integrate OSCAR nodes into your workflow.

2.3 Configuring the OSCAR Client
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before running any example, ensure your OSCAR client is properly configured. You may need to set environment variables such as:

- **Endpoint**: The URL of the OSCAR inference service.
- **ID (optional)**: The identifier for the OSCAR service.
- **Token file path**: The location of the refresh token, if applicable.

Once configured, you can execute workflows and use OSCAR nodes within your pipeline.



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
