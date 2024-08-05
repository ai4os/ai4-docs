AI4OS Modules Template
======================

To simplify the development of new modules, and make the integration of your model with the
:doc:`DEEPaaS API <api>` easier, we provide a `standard template <https://github.com/deephdc/cookiecutter-deep>`__
for modules.

There are different versions of this template:

* `minimal <https://github.com/ai4os/ai4-template>`__:
  this is what 99% of users are probably looking for. Simple, minimal template,
  with the minimum requirements to integrate your code in the AI4OS catalog.
* `child-module <https://github.com/ai4os/ai4-template-child>`__:
  this is a fork of the ``minimal`` branch specifically tailored to users performing a
  retraining of an existing module. It only creates a Docker repo whose container is
  based on an existing module's Docker image.
* `advanced <https://github.com/ai4os/ai4-template-adv>`__:
  this is a more advanced template.
  It makes more assumptions on how to structure projects and adds more files than those
  strictly needed for integration.
  Unless you are looking for some specific feature, you are probably safer using ``minimal``.

Create your project based on the template
-----------------------------------------

Based on the version of the template you choose you will be asked to answer a number of
questions, which might include:

* ``git_base_url``: Remote URL to host your new git repositories (e.g. https://github.com/deephdc ).
* ``project_name``: Project name, to be added after \"git_base_url\" (see above)", (aka <your_project> in the following).
* ``author_name``: Author name(s) (and/or your organization/company/team). If many, separate by comma.
* ``author_email``: E-Mail(s) of main author(s) (or contact person). If many, separate by comma.
* ``description``: Short description of the project.
* ``app_version``: Application version (expects X.Y.Z (Major.Minor.Patch)).
* ``open_source_license``: Choose open source license, default is MIT. `More info <https://opensource.org/licenses>`__.
* ``docker_baseimage``: Docker image your Dockerfile starts from (``FROM <docker_baseimage>``) (don't provide the tag here), (e.g. tensorflow/tensorflow ).
* ``baseimage_cpu_tag``: CPU tag for the baseimage, e.g. 2.9.1. Has to match python3!
* ``baseimage_gpu_tag``: GPU tag for the baseimage, e.g. 2.9.1-gpu. Has to match python3!
  Sometimes ``baseimage_cpu_tag`` and ``baseimage_gpu_tag`` are the same (for example in `Pytorch <https://hub.docker.com/r/pytorch/pytorch/tags>`__).
  In `Tensorflow <https://hub.docker.com/r/tensorflow/tensorflow/tags>`__ they are different.
* ``failure_notify``: whether you want to receive updates if your model fails to build.

Based on your answers, we will fill the template and create your project repository
(linked to your ``git_base_url``)

Each repository has two branches: ``master`` (to commit stable changes) and ``test``
(to test features without disrupting your users).

You have to ways to create your project from the Template.

Via User Interface
~~~~~~~~~~~~~~~~~~

Go to the `Template creation webpage <https://templates.cloud.ai4eosc.eu/>`__.
You will need an :doc:`authentication <auth>` to access to this webpage.

Then select which version of the template you want and answer the questions.
Click on ``Generate`` and you will be able to download a ``.zip`` file with both
repositories.

Via Terminal
~~~~~~~~~~~~

You will need to `install cookiecutter <https://cookiecutter.readthedocs.io/en/latest/installation.html>`__
and then run it as follows:

.. code-block:: console

  $ pip install cookiecutter
  $ cookiecutter https://github.com/ai4os/ai4-template

You are first provided with an ``[Info]`` line with information about the parameter.
And in the next line you configure this parameter.
Once all questions are answered, the two repositories will be created.

Project structure
-----------------

Based on the on the branch you choose, the template will create different files.
The content of these files is populated based on your answer to the questions.

For demonstration purposes, here follows what a typical project created with the
``minimal`` template looks like.

.. code-block::

  │
  ├── Dockerfile             <- Describes main steps on integration of DEEPaaS API and
  │                             <project-name> application in one Docker image
  │
  ├── Jenkinsfile            <- Describes basic Jenkins CI/CD pipeline (see .sqa/)
  │
  ├── LICENSE                <- License file
  │
  ├── README.md              <- The top-level README for developers using this project.
  │
  ├── .sqa/                  <- CI/CD configuration files
  │
  ├── <project-name>         <- Source code for use in this project.
  │   │
  │   ├── __init__.py        <- Makes <project-name> a Python module
  │   │
  │   ├── api.py             <- Main script for the integration with DEEPaaS API
  │   │
  │   └── misc.py            <- Misc functions that were helpful across projects
  │
  ├── data/                  <- Folder to store the data
  │
  ├── models/                <- Folder to store models
  │
  ├── tests/                 <- Scripts to perform code testing
  |
  ├── metadata.json          <- Defines information propagated to the AI4OS Hub
  │
  ├── requirements.txt       <- The requirements file for reproducing the analysis environment, e.g.
  │                             generated with `pip freeze > requirements.txt`
  ├── requirements-test.txt  <- The requirements file for running code tests (see tests/ directory)
  │
  └── setup.py, setup.cfg    <- makes project pip installable (pip install -e .) so
                                <project-name> can be imported
