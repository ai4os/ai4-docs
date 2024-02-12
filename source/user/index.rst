User documentation
==================

.. admonition:: Useful links
   :class: important

    | :fa:`home` `Homepage <https://ai4os.eu/>`__
    |   A high level overview of the project.
    | :fa:`book` `Documentation <https://docs.ai4os.eu/>`__
    |   The main source of knowledge on how to use the project. Refer always to here in case of doubt.
    | :fa:`id-badge` :doc:`Authentication <overview/auth>`
    |   The authentication management for accessing the AI4OS stack.
    | :fa:`sliders` :doc:`Dashboard <overview/dashboard>`
    |   Where users will typically search for modules developed by the community, and find the relevant pointers to use them. It allows authenticated users to deploy virtual machines on specific hardware (eg. gpus) to train a module.
    | :fa:`database` `NextCloud <https://share.services.ai4os.eu/>`__
    |   The service that allows to store your data remotely and access them from inside your deployment. (`old instance <https://data-deep.a.incd.pt/>`__)
    | :fab:`github` `Github (software) <https://github.com/ai4os>`__
    |   The code of the software powering the platform.
    | :fab:`github` `Github (modules) <https://github.com/deephdc>`__
    |   The code of all the modules available in the platform.
    | :fab:`docker` `DockerHub <https://hub.docker.com/u/deephdc/>`__
    |   Where the Docker images of the modules are stored.
    | :fa:`timeline` `CI/CD pipeline <https://jenkins.indigo-datacloud.eu/job/Pipeline-as-code/job/DEEP-OC-org/>`__
    |   Continuous Integration and Continuous Development Jenkins instance to keep everything up-to-date with latest code changes.
    | :fa:`temperature-half` `Status of services <https://status.ai4eosc.eu/>`__
    |   Check if a specific AI4OS service might be down for some reason.
    | :fa:`folder-plus` `Module template <https://templates.cloud.ai4eosc.eu/>`__
    |   Create new modules based on our project's template.
    | :fa:`chart-line` `MLflow server <https://mlflow.dev.ai4eosc.eu/>`__
    |   Log your trainings parameters and models with our MLflow server.
    | :fa:`rocket` `Inference platform (OSCAR) <https://inference.cloud.ai4eosc.eu/>`__
    |    Scalable serverless inference of AI models.
    | :fa:`rocket` `Workflows platform (Flowfuse) <https://forge.flows.dev.ai4eosc.eu/>`__
    |    Compose custom AI workflows.


New to the project? How about a quick dive?

.. toctree::
   :maxdepth: 2

   Quickstart <quickstart>

Overview
--------

A more in depth documentation, with detailed description on the architecture and
components is provided in the following sections.

.. toctree::
   :maxdepth: 2

   AI4OS architecture <overview/architecture>
   User roles and workflows <overview/user-roles>
   Authentication <overview/auth>
   AI4OS Modules <overview/modules>
   AI4OS Modules Template <overview/cookiecutter-template>
   DEEPaaS API <overview/api>
   AI4OS Dashboard <overview/dashboard>
   AI4OS Storage <overview/storage>

How-to's
--------

Use a model (basic user)
^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
   :maxdepth: 2

   Perform inference locally <howto/inference-locally>
   Perform inference remotely <howto/inference-dashboard>
   Perform inference with AI4OS Inference (OSCAR) <howto/inference-oscar>
   Create an AI inference workflow with Node-RED & FlowFuse <howto/ai4-compose/flows>

Train a model (intermediate user)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
   :maxdepth: 2

   Train a model locally <howto/train-model-locally>
   Train a model remotely <howto/train-model-dashboard>
   Use rclone to sync your dataset <howto/rclone>
   Use MLFlow for tracking your trainings <howto/mlops/mlflow>

Develop a model (advanced user)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
   :maxdepth: 2

   Develop a model <howto/develop-model>


Use a tool (intermediate user)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We have specific guides for each of the tools.

.. toctree::
   :maxdepth: 2

   Federated server <howto/tools/federated-server>

Others
------

.. toctree::
   :maxdepth: 2

   Frequently Asked Questions (FAQ) <others/faq>
   Useful Machine Learning resources <others/useful-ml-resources>
   Video demos <others/video-demos>
