AI4OS Dashboard
===============

The AI4OS dashboard allows users to access computing resources to deploy, perform inference,
and train modules hosted at the Marketplace.
The Dashboard simplifies the deployment and hides some of the technical parts that most
users do not need to worry about.

Currently, the following platforms have deployed a version of the AI4OS Dashboard.
You should access one of those Dashboards depending on the project you are a member of:

* `AI4EOSC Dashboard <https://dashboard.cloud.ai4eosc.eu/>`_
* `iMagine Dashboard <https://dashboard.cloud.imagine-ai.eu>`_
* `Tutorials Dashboard <https://tutorials.cloud.ai4eosc.eu>`_

The Dashboard has a two views:

* a **public view** that let's you browse through the modules
* a **private view** that additionally allows you to make deployments based on those
  modules and check the statistics.
  To access this view you need :doc:`authentication <auth>`.

In the remaining part of this doc we will assume you have access to this private view.

The Dashboard is divided between modules (AI models) and tools (eg. an image labelling tool,
a federated server, etc). In the remaining part of this doc we will focus on how to deploy
a module but the workflow is similar for tools.



Navigating the Marketplace
--------------------------

Once you log into the Dashboard, you are able to see all possible modules for deploying
in the ``Marketplace`` panel.
Those are basically:

* ``AI4OS Development Environment``: special module especially designed to :doc:`develop new AI models </user/howto/develop/dashboard>`.
* ``Modules``: set of AI models designed to perform given tasks (eg. image classification)
* ``Tools``: set of AI tools that come handy in the Machine Learning workflow (eg. image labeling)

.. image:: /_static/images/dashboard/home.png

Modules can be:

* **Trainable**: Those are modules that an user can train on their own data to create a new service. Like training an
  `image classifier <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/ai4os-image-classification-tf>`__ with a
  plants dataset to create a `plant classifier <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/deep-oc-plants-classification-tf>`__
  service.
  Look for the ``trainable`` tag in the marketplace to find those modules.

* **Trained (inference-ready)**: Those are modules that have been pre-trained for a specific task (like the
  `plant classifier <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/deep-oc-plants-classification-tf>`__ mentioned earlier).

Some modules can both be trainable and trained.
For example the `image classifier <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/ai4os-image-classification-tf>`__
can be trained to create other image classifiers but can also be deployed for inference as it comes pre-trained with a
general-purpose image classifier.


Making a deployment
-------------------

Once you choose the module, you will be presented with the module's information:

.. image:: /_static/images/dashboard/module.png

To deploy click in ``Train module`` and you will be redirected to a configuration page.

.. image:: /_static/images/dashboard/configure.png

This page will allow you to configure mainly three aspects:

* **General configuration**, including the service to run and Docker tags.
* **The computing resources** of the new deployment. A user can select multiple CPUs and GPUs, the machine RAM as well as
  optionally choosing the physical site where the machine must be deployed.
* **The remote storage options**, like tokens for authentication with Nextcloud.

Use the :fa:`toggle-on` ``Show help`` toggle to view additional info about the fields to fill.

Once you are happy with the state of your configuration, click ``Submit`` and you will
be redirected to the page listing all the current deployments.

General configuration
^^^^^^^^^^^^^^^^^^^^^

The parameters to configure are:

* ``Deployment title``: short name/sentence to quickly identify your deployment.

* ``Deployment description``: longer description of your deployment.

* ``Service`` determines which service to launch:

  - For performing simple inference, ``DEEPaaS`` is the recommended option, as no code changes are required.
  - For retraining a module, ``JupyterLab`` is the recommended option, as it offers access to Terminal windows which are needed to mount remote data into your machine.
  - For developing a new module, ``JupyterLab`` is the recommended option, as it offers the possibility to directly interact with the machine to write code.
    Some modules might offer also ``VScode``.

  If you select either ``JupyterLab`` or ``VScode`` you must set a password at least 9 characters long.

  .. dropdown:: ㅤㅤ What if I want both ``DEEPaaS`` and ``VSCode`` ?

    We do not provide the option to run both JupyterLab and DEEPaaS at the same time,  as code changes performed subsequently via JupyterLab wouldn't be
    reflected in DEEPaaS (which is launched with the initial codebase), thus potentially leading to confusion.

    If you want to have access to both services in the same deployment, launch with JupyterLab.
    In JupyterLab, open a **Terminal** window (:fa:`square-plus` (New launcher) ➜ **Others** ➜ **Terminal**).
    Then run ``deep-start --deepaas`` to launch DEEPaaS.
    If you make subsequent code changes, you will have to kill the old DEEPaaS process and launch a new one.

* ``Hostame``: select a custom name to access your services (eg. selecting  ``my-custom-name`` will make your service available under ``http://deepaas.my-custom-name.deployments.cloud.ai4eosc.eu`` if the address is available)

* ``Docker tag`` selects the appropriate Docker tags of your module (tags may vary across modules).
  You should choose Docker tag that match with the hardware you selected in the previous step.
  So if you selected a CPU, look for ``latest`` or ``cpu`` tags.
  If you selected a GPU, look for ``gpu`` tag.

Hardware configuration
^^^^^^^^^^^^^^^^^^^^^^

Choose the hardware type to run on:

* For inference and code development, we recommend using ``CPU`` as they are low intensity tasks.
* For (re)training, we recommend using ``GPU`` as this is a more demanding task.
  For the time being we limit to 1 GPU per deployment (and 2 GPUs per user) to allow for a
  fair distribution of resources.

Storage configuration
^^^^^^^^^^^^^^^^^^^^^

This is where you can configure how to connect your storage to your deployment.
You have two sections:

1. **Provide your RCLONE credentials**

   This is what will allow you to access your Nextcloud storage from inside your deployment.
   For this, you have to provide your **rclone** credentials.
   Please :ref:`go here <user/howto/train/rclone:2. Configuring rclone>` in order to find how to create them.

2. **Download external datasets**

   This section provides the option to sync with datasets from multiple external repositories, including
   `Zenodo <https://zenodo.org/>`__, `Hugginsface <https://huggingface.co/>`__, `Figshare <https://figshare.com/>`__, `Github <https://github.com/>`__, `Dryad <https://datadryad.org/>`__, `Open Science Framework (OSF) <https://osf.io/>`__, `Mendeley Data <https://data.mendeley.com/>`__ and `many more <https://j535d165.github.io/datahugger/repositories/>`__!

   * For Zenodo, we provide an embedded search functionality to find the datasets attached to any community.
   * For all repositories, we provide the ability to directly provide a DOI.

   With any dataset, you can select a ``force_pull`` option, so that if your dataset
   already exists in your storage it will overwrite the existing files.

.. image:: /_static/images/dashboard/storage.png


Managing the deployments
------------------------

In the ``Deployments`` panel you have a view of all the
deployments you have made so far:

.. image:: /_static/images/dashboard/deployments.png


Under :fa:`circle-info` ``Info`` you will find details about your deployment such as UUID,
resources assigned/requested, error messages, endpoints of all services, etc.
For the endpoints of the services you have:

* ``DEEPaaS`` , only accessible if you launched with the DEEPaaS command or launched JupyterLab then ran DEEPaaS.
* ``IDE`` , only accessible if you launched with the JupyterLab or VScode command
* ``Monitor`` : this is the training monitoring page. Only accessible if the module has been coded to explicitly
  display monitoring (check the module's README or training arguments) and if a training is currently running.

Under :fa:`rectangle-list` ``Quick access`` you will be able to access the service you deployed at launch time.


View your statistics
--------------------

In the ``Dashboard`` panel you can access different types of
statistics from the platform.

Current usage
^^^^^^^^^^^^^

In this section, you can see how the resources are currently being used:

.. image:: /_static/images/dashboard/stats-overview.png

* In ``Cluster Usage Overview`` you will see how many resources are currently
  consumed/available in the platform.
* In ``Your Usage`` you will see how many resources you are currently consuming.

Datacenters
^^^^^^^^^^^

In this section you will see a map of the datacenters that are providing resources for
the platform, along with their metrics:

.. image:: /_static/images/dashboard/stats-datacenters.png

Graphs
^^^^^^

In this section you can see the historical usage metrics of the platform.

.. image:: /_static/images/dashboard/stats-graphs.png

* In ``Usage over time`` you can see the daily usage time-series over the last 3 months.
  In addition to the standard resources, we show how many jobs where running and were
  queued at each point in time.

* In ``Aggregate Resource Usage`` you will be able to see to total use  of resources,
  aggregated over the lifetime of the project. We show both the whole project aggregate
  use, as well as your particular use.

  The metrics units are ``<resource> / day``. Therefore 2000 CPU consumed means that you
  have consumed the equivalent of 1 CPU for 2000 days (eg. same as 2 CPU for 1000 days).

  As the resources in the project are assigned for exclusive usage, the metrics are not
  measuring *real* usage, but *allocated* usage. So if you create a 1-CPU deployment for
  10 days, the aggregate usage will show 10 CPU days, even if you did not actually use
  the CPU at all.
