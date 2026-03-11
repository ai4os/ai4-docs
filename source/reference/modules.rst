AI Modules
==========

AI modules are the building blocks of the platform. They are AI models devloped by users to solve particular usecases.
And of course, they are open-source! This means that every model you develop in the platform can be :doc:`deployed anywhere else </howtos/deploy/cloud>`.

Modules can be explored interactively from the :doc:`Dashboard <dashboard>`, their source code is in `Github <https://github.com/ai4os-hub>`__ and the corresponding images are hosted in `DockerHub <https://hub.docker.com/u/ai4oshub/>`__.

.. dropdown:: ℹ️ Module naming conventions

  Modules follow the following name convention:

  * ``ai4os-hub/ai4-<project-name>``: module officially developed by the project
  * ``ai4os-hub/<project-name>``: modules developed by external users

  Docker images have usually tags depending on whether they are using Github's ``master`` or ``test`` and
  whether they use ``cpu`` or ``gpu``. Tags are usually:

  * ``latest`` or ``cpu``: master + cpu
  * ``gpu``: master + gpu
  * ``cpu-test``: test + cpu
  * ``gpu-test``: test + gpu

The following documentation will help you delve deeper into the different aspects of the modules:

.. grid:: 1
    :gutter: 3

    .. grid-item-card:: :material-outlined:`dashboard;1.5em`  Template
        :link: /reference/modules/template
        :link-type: doc

        Learn how to fast track your module development starting for our AI module template.

    .. grid-item-card:: :material-outlined:`search;1.5em`  Metadata
        :link: /reference/modules/metadata
        :link-type: doc

        Learn how to accurately describe your module for an enhanced discoverability.

    .. grid-item-card:: :fas:`share-nodes;fa-lg`  Provenance
        :link: /reference/modules/provenance
        :link-type: doc

        Learn how our comprehensive provenance chain allows to track how a module was trained.

    .. grid-item-card:: :material-outlined:`autorenew;1.5em`  CI/CD pipeline
        :link: /reference/modules
        :link-type: doc

        Learn how to the AI4EOSC CI/CD pipeline enforces best practices in code development.
