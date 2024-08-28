Develop a model from scratch
============================

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; margin-bottom: 2em; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/Ajgz51Sd1SU" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

This tutorial explains how to develop a AI4OS module from scratch on your local machine.

You could also use the **AI4OS Development environment** from the :doc:`AI4OS Dashboard </user/overview/dashboard>`
if you want to develop your code in a ready made environment based on some predefined Docker container
(eg. official Tensorflow or Pytorch containers). The tutorial still applies the same.
You only need to go to the Dashboard, select the **AI4OS Development environment** and
configure the Docker image and resources you want to use
(see `video demo <https://www.youtube.com/watch?v=J_l_xWiBGNA&list=PLJ9x9Zk1O-J_UZfNO2uWp2pFMmbwLvzXa&index=3>`__).

If you are new to Machine Learning, you might want to check some
:doc:`useful Machine Learning resources </user/others/useful-ml-resources>` we compiled to help you getting started.

.. admonition:: Requirements

    * If you plan to use the **AI4OS Development environment**, you need :doc:`Authentication </user/overview/auth>` to be able to access the Dashboard.
    * For **Step 7** we recommend having `docker <https://docs.docker.com/install/#supported-platforms>`__ installed (though it's not strictly mandatory).


1. Setting the framework
------------------------

This first step relies on the
:doc:`the AI4OS Modules Template </user/overview/cookiecutter-template>`
for creating a template for your new module:

* Go to the `Template creation webpage <https://templates.cloud.ai4eosc.eu/>`__.
  You will need an :doc:`authentication </user/overview/auth>` to access to this webpage.
* Then select the ``minimal`` branch of the template and answer the questions.
* Click on ``Generate`` and you will be able to download a ``.zip`` file with
  with your project directory. Extract it locally.


2. Editing the module's code
----------------------------

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


To be able to interface with DEEPaaS :ref:`you have to define <user/overview/api:1. Define the API methods for your model>`
in ``api.py`` the functions you want to make accessible to the user.
For this tutorial we are going to head to our `official demo module <https://github.com/ai4os-hub/ai4os-demo-app/blob/master/demo_app/api.py>`__
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

In order to improve the readability of the code and the overall maintainability of the project,
we enforce proper Python coding styles (``pep8``) to all modules added to the Marketplace.
Modules that fail to pass style tests won't be able to build docker images.
If you want to check if your module pass the tests, go to your project folder and type:

.. code-block:: console

    $ flake8

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


3. Editing the module's Dockerfile
----------------------------------

Your ``./Dockerfile`` is in charge of creating a docker image that integrates
your application, along with deepaas and any other dependency.
You can modify that file according to your needs.

We recommend checking the installation steps are fine.
If your module needs additional Linux packages add them to the Dockerfile.
Check your Dockerfile works correctly by building it locally and running it:

.. code-block:: console

    $ docker build --no-cache -t your_project .
    $ docker run -ti -p 5000:5000 -p 6006:6006 -p 8888:8888 your_project

Your module should be visible in http://0.0.0.0:5000/ui .
You can make a POST request to the ``predict`` method to check everything is working as intended.


4. Editing the module's metadata
--------------------------------

.. include:: /user/snippets/edit-metadata.rst


5. Integrating the module in the Marketplace
--------------------------------------------

.. include:: /user/snippets/integrate-marketplace.rst


.. tip::

    If you run into problems you can always check the :doc:`Frequently Asked Questions (FAQ) </user/support/faq>`.
