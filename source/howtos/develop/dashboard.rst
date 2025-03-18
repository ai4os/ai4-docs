Develop a model from scratch
============================

.. admonition:: Requirements
   :class: info

   🔒 This tutorial requires :ref:`full authentication <getting-started/register:Full authentication>`.

This tutorial explains how to develop a AI4OS module from scratch.

If you are new to Machine Learning, you might want to check some :doc:`useful Machine Learning resources </others/useful-ml-resources>` we compiled to help you getting started.

.. admonition:: Requirements
    :class: info

    * For **Step 1**, to use the Module's template webpage, you need at least :doc:`basic authentication </reference/user-access-levels>`.
    * For **Step 2**, if you plan to use the AI4OS Development environment, you need :doc:`full authentication </reference/user-access-levels>` to be able to access the Dashboard.
      Otherwise you can develop locally.
    * For **Step 4** we recommend having `docker <https://docs.docker.com/install/#supported-platforms>`__ installed (though it's not strictly mandatory).


1. Setting the framework
------------------------

This first step relies on the :doc:`the AI4OS Modules Template </reference/cookiecutter-template>` for creating a template for your new module:

* Access and authenticate in the `Template creation webpage <https://templates.cloud.ai4eosc.eu/>`__.
* Then select the ``minimal`` branch of the template and answer the questions.
* Click on ``Generate`` and you will be able to download a ``.zip`` file with with your project directory. Extract it locally.

2. Prepare your development environment
---------------------------------------

Although it is possible to develop your code locally, we also offer the possibility to develop from our `AI4OS Development Environment <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/ai4os-dev-env>`__.

This offers the benefits of:

* developing on dedicated resources (including GPUs),
* have direct access to your Nextcloud storage,
* develop on Docker image that is already packaged with your favorite Deep Learning framework (eg. Pytorch, Tensorflow),
* develop on your favorite IDE (Jupyterlab or VScode),

Check :ref:`how to configure <dashboard_deployment>` the AI4OS Development Environment.
For example, this is what an AI4OS Development Environment with VScode would look out-of-the-box:

.. dropdown:: :fab:`youtube;youtube-icon` ㅤLaunching a development environment

  .. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; margin-bottom: 2em; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/mod3fwN8wCI" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

.. image:: /_static/images/endpoints/vscode.png


.. admonition:: Use storage-synced folder to develop
   :class: info

   We recommend you make a :ref:`deployment synced with storage <dashboard_storage>`.

   By doing so, you can develop your code inside the ``/storage`` folder and any changes you make will automatically be synced with the :doc:`project's Cloud storage </reference/storage>`.
   This will prevent you from losing your work in the case that a deployment crash occurs.


.. _develop_code:

3. Editing the module's code
----------------------------

Unpack, the zip file created in Step 1.
Install your project as a Python module in **editable** mode (so that the changes you make to the codebase are picked by Python).

.. code-block:: console

    $ cd <project-name>
    $ pip install -e .

Now you can start writing your code.

.. dropdown:: ㅤ 💡 Optimal VScode setup

   **Tip nº1**:
   VScode by default is initialized in ``/srv``.
   For a better coding experience we suggest opening VScode with your folder project *only*.
   This will allow you to ignore other non-related folders under ``/srv`` when doing global searches for example.
   For this, go to ``File > Open Folder > /srv/<project-name>``.

   **Tip nº2**:
   :ref:`Use the AI4OS LLM as coding assistant <reference/llm:Use it as a code assistant with VScode>`.
   We recommend doing this along tip nº1 in order to avoid Continue from freezing when trying to index the whole workspace contents.

.. dropdown:: ㅤ 🛠️ Troubleshooting DEEPaaS installation

    Some users have reported issues in some systems when installing ``deepaas`` (which is always present in the ``requirements.txt`` of your project).
    Those issues have been resolved as following:

    * In `Pytorch Docker images <https://hub.docker.com/r/pytorch/pytorch>`__, making sure ``gcc`` is installed (``apt install gcc``)
    * In other systems, sometimes ``python3-dev`` is needed (``apt install python3-dev``).


To be able to interface with DEEPaaS :ref:`you have to define <deepaas-integrate>`
in ``api.py`` the functions you want to make accessible to the user.
For this tutorial we are going to head to our `official demo module <https://github.com/ai4os-hub/ai4os-demo-app/blob/main/ai4os_demo_app/api.py>`__
and copy-paste its ``api.py`` file.

Once this is done, check that DEEPaaS is interfacing correctly by running:

.. code-block:: console

    $ deepaas-run --listen-ip 0.0.0.0

Your module should be visible in http://0.0.0.0:5000/ui .
If you don't see your module, you probably messed the ``api.py`` file.
Try running it with python so you get a more detailed debug message.

.. code-block:: console

    $ python api.py

Remember to leave untouched the ``get_metadata()`` function that comes predefined with your module,
as all modules should have proper metadata.

In general, you will have the following ports available when making a deployment in the platform:

* ``5000``: default port used for exposing the API (eg. DEEPaaS)
* ``6006``: default port used for exposing a monitoring endpoint (eg. Tensorboard)
* ``8888``: default port used for exposing the IDE (eg. JupyterLab, VScode)
* ``80``: port available to let developers expose their custom endpoint

In order to improve the readability of the code and the overall maintainability of your module,
we enforce some quality standards in tox (including style, security, etc).
Modules that fail to pass style tests won't be able to build docker images.
You can check locally if your module passes the tests:

.. code-block:: console

    $ tox -e .

There you should see a detailed report of the offending lines (if any).
You can always `turn off flake8 testing <https://stackoverflow.com/a/64431741>`__
in some parts of the code if long lines are really needed.

.. dropdown:: ㅤ 🧠 Using code formatters

    If your project has many offending lines, it's recommended using a code formatter tool like
    `Black <https://black.readthedocs.io>`__. It also helps for having a consistent code style
    and minimizing git diffs. Black formatted code will always be compliant with flake8.

    Once `installed <https://black.readthedocs.io/en/stable/getting-started.html#installation>`__,
    you can check how Black would have reformatted your code:

    .. code-block:: console

        $ black <code-folder> --diff

    You can always `turn off Black formatting <https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html?highlight=fmt#code-style>`__
    if you want to keep some sections of your code untouched.

    If you are happy with the changes, you can make them permanent using:

    .. code-block:: console

        $ black <code-folder>

    Remember to have a backup before reformatting, just in case!


4. Editing the module's Dockerfile
----------------------------------

Your ``./Dockerfile`` is in charge of creating a docker image that integrates
your application, along with deepaas and any other dependency.
You can modify that file according to your needs.

If you need to add instructions based on the runtime (eg. perform certain actions depending on whether you detected a GPU), please use the ``ENTRYPOINT`` statement, as ``CMD`` will be overwritten by the platform when you deploying a given service (eg. JupyterLab).

We recommend checking the installation steps are fine.
If your module needs additional Linux packages add them to the Dockerfile.
Check your Dockerfile works correctly by building it **locally** (outside the AI4OS Development Environment) and running it:

.. code-block:: console

    $ docker build --no-cache -t your_project .
    $ docker run -ti -p 5000:5000 -p 6006:6006 -p 8888:8888 your_project

Your module should be visible in http://0.0.0.0:5000/ui .
You can make a POST request to the ``predict`` method to check everything is working as intended.


5. Update your project's metadata
---------------------------------

.. include:: /snippets/edit-metadata.rst


6. Integrating the module in the Marketplace
--------------------------------------------

.. include:: /snippets/integrate-marketplace.rst


.. admonition:: Next steps
    :class: tip

    If to go further, check our tutorials on how to:

    * :doc:`develop a module that support incremental learning </howtos/develop/incremental-learning>`
    * :doc:`develop a module that supports distributed learning </howtos/develop/distributed-learning>`
    * :doc:`develop a module that support MLflow for tracking experiments </howtos/develop/mlflow>`
