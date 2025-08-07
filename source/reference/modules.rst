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

Provenance
----------

Being able to trace an AI module provenance is key to the `FAIR principles <https://www.nature.com/articles/sdata201618>`__, ensuring reproducibility and building trust in the module's predictions.

That's why every time a module's :ref:`CI/CD pipeline <reference/modules:CI /CD pipeline>` is executed, we build a provenance chain of that module.
Based on the module's :ref:`metadata <reference/modules:AI4OS metadata>`, we parse the different :ref:`platform components <getting-started/terminology:Architecture overview>`, gathering all the provenance information into a single RDF file (`example <https://provenance.services.ai4os.eu/rdf?applicationId=ai4os-demo-app>`__).
These sources include:

* **Jenkins**: we extract build information, like code quality tests or docker image hashes,
* **Nomad**: we extract training information, like what were the computing resources used to train a given module,
* **MLflow**: we extract experiment logging information, like the hyper-parameters used in the different training runs,
* **Module's metadata**: we extract module information like relevant keywords, external links or creation/modification dates,

In addition, this RDF file explains the connection between the different components, like how the Nomad deployment used a given dataset for training the module, or how Jenkins generated a new Harbor docker image.

For an improved user experience, we show users the final provenance chain in a simplified interactive graph (`example <https://provenance.services.ai4os.eu/?applicationId=ai4os-demo-app>`__):

.. image:: /_static/images/provenance/simple-graph.png

that can be expanded for further details:

.. image:: /_static/images/provenance/expanded-graph.png

For each module, both the RDF and the graph links are available in the :ref:`Dashboard's module details <dashboard_deployment>`, under the ``Provenance`` section in the right panel.

Finally, you can ask a chat bot assistant questions about the graph and it will use the underlying RDF file to offer grounded answers.

.. image:: /_static/images/provenance/chat.png
