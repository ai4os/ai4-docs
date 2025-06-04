Modules
=======

Every component in the platform is open-source, including the modules!
This means that everything you develop in the platform can be :doc:`deployed anywhere else </howtos/deploy/cloud>`.

All  modules are found at the :doc:`AI4OS Dashboard <dashboard>`, the source code is
hosted under `Github's ai4os-hub <https://github.com/ai4os-hub>`__ organization and the corresponding Docker images are
hosted under `DockerHub's ai4oshub <https://hub.docker.com/u/ai4oshub/>`__ organization.

Modules follow the following name convention:

* ``ai4os-hub/ai4-<project-name>``: module officially developed by the project
* ``ai4os-hub/<project-name>``: modules developed by external users

Docker images have usually tags depending on whether they are using Github's ``master`` or ``test`` and
whether they use ``cpu`` or ``gpu``. Tags are usually:

* ``latest`` or ``cpu``: master + cpu
* ``gpu``: master + gpu
* ``cpu-test``: test + cpu
* ``gpu-test``: test + gpu

AI4OS metadata
--------------

All modules have comprehensive metadata to make them `FAIR <https://www.nature.com/articles/sdata201618>`__ friendly.
The metadata can later be downloaded in several formats in the
:ref:`Dashboard module detail page <dashboard_deployment>`.

Editing a module's metadata
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: /snippets/edit-metadata.rst


CI /CD pipeline
---------------

In the project we use `Jenkins <https://jenkins.services.ai4os.eu/job/AI4OS-hub>`__
for implementing CI/CD (Continuous Integration / Continuous Development) pipeline. This pipeline automatically performs a
series of actions for you each time you commit a change in your code. This ensures that all the information and builds
across the project are always up-to-date with your code.

A typical pipeline is divided in two parts:

* a model quality assurance section, using `tox <https://tox.wiki/>`__, where we do:

  * code style analysis using `flake8 <https://flake8.pycqa.org/>`__,
  * unit testing using `pytest <https://docs.pytest.org/>`__,
  * security scanners using `Bandit <https://bandit.readthedocs.io/>`__,
  * `metadata validation <https://github.com/ai4os/ai4-metadata>`__,

* a platform components update, where we:

  * build the Docker image to the AI4OS Registry and mirror to DockerHub,
  * update the Marketplace and additional AI4OS services,
  * regenerate the provenance chain of that module,

.. image:: /_static/images/ai4eosc/jenkins.png


Module popularity
-----------------

In order to efficiently explore the catalog of modules, it is useful to know what are the most popular modules.

Assessing the popularity of module is a difficult task because there are many proxy metrics of popularity, each one with it's own shortcomings:

* **Github Stars**: while useful, many users do not take the time to star the modules they use.
* **DockerHub downloads**: downloads sometimes do not reflect real usage because they can be inflated by CI/CD automated builds.
* **Number of created persistent deployments**: they can be misleading sometimes, as someone can deploy a module a single time but use it a lot, while another person might download it and immediately remove it.
* **Number of created tryme deployments**: this metric is very informative but it privileges trained modules (eg. YOLO trained to detect fishes) over untrained ones (eg. YOLO with no trained weights). This is unfair because the trained module used the untrained module as a base reference, so the base module is indeed popular.
* **Number of Dashboard views**: this metric could prioritize fancy shinny modules over modules that are really used by users,

To be able to easily compare across modules and mitigate the individual shortcomings, we weight these individual metrics into an overall **aggregated popularity score**. This aggragated score allows to sort the catalog modules by popularity.

.. todo: add image