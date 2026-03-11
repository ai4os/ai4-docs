:orphan:

AI module CI/CD
===============

In the platform, we use `Jenkins <https://jenkins.cloud.ai4eosc.eu/job/AI4OS-hub>`__
for implementing the CI/CD (Continuous Integration / Continuous Development) pipeline. This pipeline automatically performs a
series of actions for you each time you commit a change in your code. This ensures that all the information and builds
across the project are always up-to-date with your code.

A typical pipeline is divided in two parts:

* a model quality assurance section, using `tox <https://tox.wiki/>`__, where we do:

  * code style analysis using `flake8 <https://flake8.pycqa.org/>`__,
  * unit testing using `pytest <https://docs.pytest.org/>`__,
  * security scanners using `bandit <https://bandit.readthedocs.io/>`__,
  * `metadata validation <https://github.com/ai4os/ai4-metadata>`__,

* a platform components update, where we:

  * build the Docker image to the platform Registry and mirror to DockerHub,
  * update the :ref:`Marketplace <dashboard_marketplace>` and additional platform services,
  * archive the code to `Zenodo <https://zenodo.org/communities/ai4eosc>`__ if a code release is made,
  * regenerate the :doc:`provenance </reference/modules/provenance>` chain of that module,

.. image:: /_static/images/ai4eosc/jenkins.png
