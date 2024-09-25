Develop a model from scratch
============================

This tutorial explains how to develop a AI4OS module from scratch.

If you are new to Machine Learning, you might want to check some :doc:`useful Machine Learning resources </user/others/useful-ml-resources>` we compiled to help you getting started.

.. admonition:: Requirements
    :class: info

    * For **Step 1**, to use the Module's template webpage, you need at least :ref:`basic authentication <user/overview/auth:Basic authentication>`.
    * For **Step 2**, if you plan to use the AI4OS Development environment, you need :ref:`full authentication <user/overview/auth:Full authentication>` to be able to access the Dashboard.
      Otherwise you can develop locally.
    * For **Step 4** we recommend having `docker <https://docs.docker.com/install/#supported-platforms>`__ installed (though it's not strictly mandatory).


1. Setting the framework
------------------------

This first step relies on the :doc:`the AI4OS Modules Template </user/overview/cookiecutter-template>` for creating a template for your new module:

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

Check :ref:`how to configure <user/overview/dashboard:Making a deployment>` the AI4OS Development Environment.
For example, this is what an AI4OS Development Environment with VScode would look out-of-the-box:

.. image:: /_static/images/endpoints/vscode.png


3. Editing the module's code
----------------------------

Unpack, the zip file created in Step 1.
Install your project as a Python module in **editable** mode (so that the changes you make to the codebase are picked by Python).

.. code-block:: console

    $ cd <project-name>
    $ pip install -e .

Now you can start writing your code.

.. tip::

    Some users have reported issues in some systems when installing ``deepaas`` (which is always present in the ``requirements.txt`` of your project).
    Those issues have been resolved as following:

    * In `Pytorch Docker images <https://hub.docker.com/r/pytorch/pytorch>`__, making sure ``gcc`` is installed (``apt install gcc``)
    * In other systems, sometimes ``python3-dev`` is needed (``apt install python3-dev``).


To be able to interface with DEEPaaS :ref:`you have to define <user/overview/api:Integrate your model with the API>`
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

You can also use port ``6006`` to expose some training monitoring tool, like Tensorboard.

In order to improve the readability of the code and the overall maintainability of your module,
we enforce some quality standards in tox (including style, security, etc).
Modules that fail to pass style tests won't be able to build docker images.
You can check locally if your module passes the tests:

.. code-block:: console

    $ tox -e .

There you should see a detailed report of the offending lines (if any).
You can always `turn off flake8 testing <https://stackoverflow.com/a/64431741>`__
in some parts of the code if long lines are really needed.

.. tip::

    If your project has many offending lines, it's recommended using a code formatter tool like
    `Black <https://black.readthedocs.io>`__. It also helps for having a consistent code style
    and minimizing git diffs. Black formatted code will always be compliant with flake8.

    Once `installed <https://black.readthedocs.io/en/stable/getting_started.html#installation>`__,
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

.. include:: /user/snippets/edit-metadata.rst


6. Integrating the module in the Marketplace
--------------------------------------------

.. include:: /user/snippets/integrate-marketplace.rst


.. admonition:: Next steps
    :class: tip

    If to go further, check our tutorials on how to:

    * :doc:`develop a module that support incremental learning </user/howto/develop/incremental-learning>`
    * :doc:`develop a module that supports distributed learning </user/howto/develop/distributed-learning>`
    * :doc:`develop a module that support MLflow for tracking experiments </user/howto/develop/mlflow>`