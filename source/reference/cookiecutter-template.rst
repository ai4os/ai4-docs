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

* ``project_name``: Short name of your project (max 4 words). The GitHub repository name and Python module name are derived from the project_name.
* ``author_name``: Author name(s) (and/or your organization/company/team). If many, separate by comma.
* ``author_email``: E-Mail(s) of main author(s). If many, separate by comma.
* ``description``: A short description of the project.
* ``app_version``: Application version (expects X.Y.Z (Major.Minor.Patch), in accordance with `https://semver.org/`).
* ``open_source_license``: Choose one of the licenses (default is MIT). `More info <https://opensource.org/licenses>`__.
* ``docker_baseimage``: Docker image your Dockerfile starts from (``FROM <docker_baseimage>``). Do not provide the tag here.
* ``baseimage_tag``: Default tag for docker_baseimage (for Tensorflow: CPU version, e.g. 2.9.1).
* ``baseimage_gpu_tag``: GPU tag for the baseimage, e.g. 2.9.1-gpu. Should match and use Python 3.

Based on your answers, we will fill the template and create your project repository
(linked to `AI4OS Hub <https://github.com/ai4os-hub>`__).

Each repository has three branches: ``main`` (to commit stable changes),
``test`` (to test features without disrupting your users) and
``dev`` (to develop new features).

You have two ways to create your project from the Template.

Via User Interface
~~~~~~~~~~~~~~~~~~

Go to the `Template creation webpage <https://templates.cloud.ai4eosc.eu/>`__.
You will need an :doc:`authentication </reference/user-access-levels>` to access to this webpage.

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
  ├── VERSION                <- <project-name> version file
  │
  ├── .sqa/                  <- CI/CD configuration files
  │
  ├── <project-name>         <- Source code for use in this project.
  │   │
  │   ├── __init__.py        <- Makes <project-name> a Python module
  │   │
  │   ├── api.py             <- Main script for the integration with DEEPaaS API
  │   |
  │   ├── config.py          <- Configuration file to define Constants used across <project-name>
  │   │
  │   └── misc.py            <- Misc functions that were helpful across projects
  │
  ├── data/                  <- Folder to store the data
  │
  ├── models/                <- Folder to store models
  │   
  ├── tests/                 <- Scripts to perform code testing
  |
  ├── metadata.json          <- Metadata information propagated to the AI4OS Hub
  │
  ├── pyproject.toml         <- a configuration file used by packaging tools, so <project-name>
  │                             can be imported and installed using `pip install -e .`                             
  │
  ├── requirements.txt       <- The requirements file for reproducing the analysis environment, i.e.
  │                             contains a list of packages needed to make <project-name> work
  │
  ├── requirements-test.txt  <- The requirements file for running code tests (see tests/ directory)
  │
  └── tox.ini                <- Configuration file for the tox tool used for testing (see .sqa/)
