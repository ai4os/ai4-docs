Welcome to AI4OS documentation!
===============================

The ``AI4OS`` stack empowers scientist by lowering the barrier to adopt the latest AI
models and tools. It covers the full ML cycle: from model creation, to training, deployment
and monitoring in production. Following the FAIR principles for science, both our software
(platform and models) are fully open-source and easily portable to any other platform
(no vendor lock-in!).

.. admonition:: A quick note on terminology
   :class: info

   ``AI4OS`` is the name of the generic software stack that is
   powering the deployments of different platforms (``AI4EOSC``, ``iMagine``, etc).
   So, for example, the **AI4OS Dashboard** is the component that can be deployed as the
   **AI4EOSC Dashboard** or the **iMagine Dashboard**.
   These platform-specific Dashboards can have minor customizations but the underlying
   technology remains the same.

   Current supported platforms:

   * `AI4EOSC <https://ai4eosc.eu/>`__: AI for the European Open Science Cloud
   * `iMagine <https://imagine-ai.eu/>`__: Imaging data and services for aquatic science
   * `AI4Life <https://ai4life.eurobioimaging.eu/>`__: AI models and methods for the life sciences


.. admonition:: Useful links
   :class: important

    | :fa:`home` `Homepage <https://ai4os.eu/>`__
    |   A high level overview of the project.
    | :fa:`book` `Documentation <https://docs.ai4os.eu/>`__
    |   The main source of knowledge on how to use the project. Refer always to here in case of doubt.
    | :fa:`id-badge` :doc:`Authentication <user/overview/auth>`
    |   The authentication management for accessing the AI4OS stack.
    | :fa:`sliders` :doc:`Dashboard <user/overview/dashboard>`
    |   Where users will typically search for modules developed by the community, and find the relevant pointers to use them. It allows authenticated users to deploy virtual machines on specific hardware (eg. gpus) to train a module.
    | :fa:`database` `NextCloud <https://share.services.ai4os.eu/>`__
    |   The service that allows to store your data remotely and access them from inside your deployment. (`old instance <https://data-deep.a.incd.pt/>`__)
    | :fab:`github` `Github (software) <https://github.com/ai4os>`__
    |   The code of the software powering the platform.
    | :fab:`github` `Github (modules) <https://github.com/ai4os-hub>`__
    |   The code of all the modules available in the platform.
    | :fab:`docker` `DockerHub <https://hub.docker.com/u/ai4oshub/>`__
    |   Where the Docker images of the modules are stored.
    | :fab:`docker` `Harbor <https://registry.services.ai4os.eu/>`__
    |   Custom Docker image registry we deployed to overcome DockerHub limitations.
    | :fa:`timeline` `CI/CD pipeline <https://jenkins.services.ai4os.eu/job/AI4OS-hub>`__
    |   Continuous Integration and Continuous Development Jenkins instance to keep everything up-to-date with latest code changes.
    | :fa:`temperature-half` `Status of services <https://status.ai4eosc.eu/>`__
    |   Check if a specific AI4OS service might be down for some reason.
    | :fa:`folder-plus` `Module template <https://templates.cloud.ai4eosc.eu/>`__
    |   Create new modules based on our project's template.
    | :fa:`chart-line` `MLflow server <https://mlflow.cloud.ai4eosc.eu/>`__
    |   Log your trainings parameters and models with our MLflow server.
    | :fa:`rocket` `Inference platform (OSCAR) <https://inference.cloud.ai4eosc.eu/>`__
    |    Scalable serverless inference of AI models.
    | :fa:`network-wired` `Inference pipelines platform (Flowfuse) <https://forge.flows.dev.ai4eosc.eu/>`__
    |    Compose custom AI inference pipelines.

User documentation
------------------

If you are a user (current or potential) you should :doc:`start here <user/index>`.

.. toctree::
   :maxdepth: 3

   user/index

Component documentation
-----------------------

Here we share the documentation of components develop within the platform but that
have their own documentation pages:

* `DEEPaaS documentation <https://docs.ai4os.eu/projects/deepaas>`__
* `OSCAR <https://docs.oscar.grycap.net>`__


Technical documentation
-----------------------

If you are searching for technical notes on various areas, please check the
following section.

.. toctree::
   :maxdepth: 3

   technical/index

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
