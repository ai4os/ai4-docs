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
    | :fa:`network-wired` `Workflows platform (Flowfuse) <https://forge.flows.dev.ai4eosc.eu/>`__
    |    Compose custom AI workflows.


New to the project? How about a quick dive?

.. toctree::
   :maxdepth: 2

   📝 Quickstart <quickstart>
   ⭐ New features <new-features>

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

Try a model
^^^^^^^^^^^

.. toctree::
   :maxdepth: 2

   Try with the Dashboard (Gradio) <howto/try/dashboard-gradio>
   Try locally <howto/try/locally>


Develop a model
^^^^^^^^^^^^^^^

.. toctree::
   :maxdepth: 2

   Develop a model <howto/develop/dashboard>

We also provide guides for developers to implement and support advanced training
techniques in their modules:

.. toctree::
   :maxdepth: 1

   Use Incremental learning <howto/develop/incremental-learning>
   Use Distributed learning <howto/develop/distributed-learning>
   Use MLFlow for tracking your trainings <howto/develop/mlflow>


Train a model
^^^^^^^^^^^^^

.. toctree::
   :maxdepth: 2

   Train a model with the Dashboard <howto/train/dashboard>
   Make a federated training <howto/train/federated-server>
   Use rclone to sync your dataset (advanced) <howto/train/rclone>


Deploy a model in production
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
   :maxdepth: 2

   Deploy with OSCAR <howto/deploy/oscar>
   Deploy in your cloud <howto/deploy/cloud>

In addition to deploying standalone modules, we support the concatenation of different
AI modules into a multi-step workflow.

.. toctree::
   :maxdepth: 2

   Create a workflow with FlowFuse <howto/deploy/flowfuse>
   Create a workflow with Elyra <howto/deploy/elyra>


Others
------

.. toctree::
   :maxdepth: 2

   Useful Machine Learning resources <others/useful-ml-resources>
   Video demos <others/video-demos>

Support
-------

.. raw:: html

   </embed>
   <div style="background-color: #243652; padding: 10px; border-radius: 10px; color: #c9daf5;">
      <p>
      Do you need additional support? Are you interested in the project and want more
      information? <br>
      Please don't hesitate to <a href="mailto:ai4eosc-support@listas.csic.es" style="color: white; text-decoration: underline;">contact support</a>.
      </p>
   </div>
   </embed>


.. toctree::
   :maxdepth: 2

   Frequently Asked Questions (FAQ) <support/faq>
