AI4OS Dashboard
===============

The AI4OS dashboard allows users to access computing resources to deploy, perform inference,
and train modules hosted at the Marketplace.
The Dashboard simplifies the deployment and hides some of the technical parts that most
users do not need to worry about.

Currently, the following platforms have deployed a version of the AI4OS Dashboard.
You should access one of those Dashboards depending on the project you are a member of:

* `AI4EOSC Dashboard <https://dashboard.cloud.ai4eosc.eu>`__
* `iMagine Dashboard <https://dashboard.cloud.imagine-ai.eu>`__
* `AI4Life Dashboard <https://ai4life.cloud.ai4eosc.eu>`__
* `Tutorials Dashboard <https://tutorials.cloud.ai4eosc.eu>`__

The Dashboard has a two views:

* a **public view** that let's you browse through the modules
* a **private view** that additionally allows you to make deployments based on those
  modules and check the statistics.
  To access this view you need :doc:`authentication </reference/user-access-levels>`.

In the remaining part of this doc we will assume you have access to this private view.

The Dashboard is divided between modules (AI models) and tools (eg. an image labelling tool,
a federated server, etc). In the remaining part of this doc we will focus on how to deploy
a module but the workflow is similar for tools.


.. _dashboard_profile:

Profile
-------

In the top-right corner, you will be able to find:

* :material-outlined:`notifications;1.5em`: notifications about the platforms, like expected downtimes and issues,
* :material-outlined:`account_circle;1.5em`: your profile details.

.. image:: /_static/images/dashboard/profile.png

In your profile details you will find:

* ``Personal information``: your full name and your email.

* ``Virtual organizations``: the VOs you are a member of and which roles you have in them.

* ``Linked services``: many of the ecosystem services can be linked to the Dashboard, for a tighter integration that delivers a smoother experience:

  You can link for example:

  * the :doc:`AI4OS storage </reference/storage>` as well as :doc:`external storage providers </technical/howto-developers/storage-providers>`,
  * the :doc:`MLflow Experiment Tracking </howtos/develop/mlflow>`,
  * your `Huggingface <https://huggingface.co/>`__ account,

  In order to link a service, you have to click on the ``Link`` button, log in the popup window and grant access to the Dashboard.
  If you have previously linked the service, you also have to to delete old credentials and generate new ones using ``Re-link``.

  .. dropdown:: :fab:`youtube;youtube-icon` ㅤLink with any NextCloud storage service

    .. raw:: html

        <div style="position: relative; padding-bottom: 56.25%; margin-bottom: 2em; height: 0; overflow: hidden; max-width: 100%; height: auto;">
          <iframe src="https://www.youtube.com/embed/PHbHq4KbmwE" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
        </div>

    :material-outlined:`error;1.5em` Please, be aware that video demos can become quickly outdated. In case of doubt, always refer to the written documentation.


.. _dashboard_marketplace:

Navigating the Marketplace
--------------------------

Once you log into the Dashboard, you will be shown all the items the ``Marketplace`` has to offer.
Those are basically:

* :material-outlined:`build;1.5em` ``Tools``: set of AI tools that come handy in the Machine Learning workflow.

  We currently offer for example:

  - The **AI4OS Development Environment** to develop new modules (:doc:`tutorial </howtos/develop/dashboard>`)
  - Several **Federated Learning Server** to make federated privacy-friendly trainings (:doc:`Flower </howtos/train/federated-flower>`, :doc:`NVFLARE </howtos/train/federated-nvflare>`)
  - The **Computer Vision Annotation Tool** (CVAT) to label images (:doc:`tutorial </howtos/train/cvat>`)

* :material-outlined:`model_training;1.5em` ``Modules``: set of AI models designed to perform given tasks (eg. image classification)

.. image:: /_static/images/dashboard/marketplace.png

You can use filters to quickly find the module you want.
We provide filtering by:

* ``Libraries``: this is the Deep Learning the module uses (eg. Pytorch, Tensorflow)
* ``Tasks``: this is the broad task the module addresses (eg. Computer Vision, Natural Language Processing)
* ``Platform Categories``: platform-specific tags.
  Current options include:

  - ``AI4 tools``
  - ``AI4 pretrained``: modules that already come with a trained AI model
  - ``AI4 inference``: modules that can be used for inference (usually overlaps with *AI4 pretrained*)
  - ``AI4 trainable``: modules that can be trained on a new dataset

  For example the `image classifier <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/ai4os-image-classification-tf>`__ is both pretrained (because is comes with a model trained on ImageNet), inference-ready (because it allows to use that model to do predictions) and trainable (because it allows to retrain that model on a different dataset, to create for example a `plant classifier <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/plants-classification>`__ )

* ``Data type``: type of data the module processes (eg. Image, Audio)
* ``Tags``: any module-specific tag


.. _dashboard_deployment:

Making a deployment
-------------------

Once you choose the module, you will be presented with the module's information:

.. image:: /_static/images/dashboard/module.png

To deploy click in ``Deploy > Inference API (dedicated)`` and you will be redirected to a configuration page.

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

  - For performing simple inference, ``DEEPaaS`` (API) is the recommended option, as no code changes are required.
  - For retraining a module, ``JupyterLab`` is the recommended option, as it offers access to Terminal windows which are needed to mount remote data into your machine.
  - For developing a new module, ``JupyterLab`` is the recommended option, as it offers the possibility to directly interact with the machine to write code.
    Some modules might offer also ``VScode``.

  If you select either ``JupyterLab`` or ``VScode`` you must set a password at least 9 characters long.

  .. dropdown:: ㅤ 💡 What if I want both ``DEEPaaS`` and ``VSCode`` ?

    We do not provide the option to run both JupyterLab and DEEPaaS at the same time,  as code changes performed subsequently via JupyterLab wouldn't be
    reflected in DEEPaaS (which is launched with the initial codebase), thus potentially leading to confusion.

    If you want to have access to both services in the same deployment, launch with JupyterLab.
    In JupyterLab, open a **Terminal** window (:fa:`square-plus` (New launcher) ➜ **Others** ➜ **Terminal**).
    Then run ``deep-start --deepaas`` to launch DEEPaaS.
    If you make subsequent code changes, you will have to kill the old DEEPaaS process and launch a new one.

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

.. _dashboard_storage:

Storage configuration
^^^^^^^^^^^^^^^^^^^^^

This is where you can configure how to connect your storage to your deployment.
You have two sections:

1. **Storage configuration**

   This is what will allow you to access your storage from inside your deployment.

   You will be able to select any storage from the ones you have configured in
   your :ref:`Profile section <dashboard_profile>`.

   For advanced users, it is also possible to fill your RCLONE credentials manually.
   Please :ref:`go here <rclone_configuration>` in order to find how to create them.

.. image:: /_static/images/dashboard/storage-rclone.png

2. **Download external datasets**

   This section provides the option to sync with datasets from multiple external repositories, including
   `Zenodo <https://zenodo.org/>`__, `Hugginsface <https://huggingface.co/>`__, `Figshare <https://figshare.com/>`__, `Github <https://github.com/>`__, `Seanoe <https://www.seanoe.org/>`__, `Data Europa <https://data.europa.eu/>`__, `Dryad <https://datadryad.org/>`__, `Open Science Framework (OSF) <https://osf.io/>`__, `Mendeley Data <https://data.mendeley.com/>`__ and `many more <https://j535d165.github.io/datahugger/repositories/>`__!

   * For Zenodo, we provide an embedded search functionality to find the datasets attached to any community.
   * For all repositories, we provide the ability to directly provide a DOI or a URL.

   With any dataset, you can select a ``force_pull`` option, so that if your dataset
   already exists in your storage it will overwrite the existing files.

   If the module you are deploying has an reference dataset listed by the module's creator, this will appear as a suggested dataset.

.. dropdown:: :fab:`youtube;youtube-icon` ㅤDownload a dataset from Zenodo

   .. raw:: html

      <div style="position: relative; padding-bottom: 56.25%; margin-bottom: 2em; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/QXp85utCr4A" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
      </div>

   :material-outlined:`error;1.5em` Please, be aware that video demos can become quickly outdated. In case of doubt, always refer to the written documentation.


.. image:: /_static/images/dashboard/storage-datasets.png


.. _dashboard-manage-deployments:

Managing the deployments
------------------------

In the ``Deployments`` tab (in the Navigation panel on the left) you have a table view of all the deployments you have made so far, separated both in ``Modules`` and ``Tools`` tables:

.. image:: /_static/images/dashboard/deployments_modules_tools.png

Under :material-outlined:`info;1.5em` ``Info`` you will find details about your deployment such as UUID, resources assigned/requested, error messages, endpoints of all services, etc.
For the endpoints of the services you have:

* ``API``: :doc:`Module's API </reference/api>`, only accessible if you launched with the DEEPaaS command or launched JupyterLab then ran DEEPaaS.
* ``IDE``: :ref:`Development environment <howtos/develop/dashboard:2. Prepare your development environment>`, only accessible if you launched with the JupyterLab or VScode command.
* ``Monitor``: :ref:`Training monitoring <howtos/train/standard:4. Start training the model>`, only accessible if the module has been coded to explicitly display monitoring (check the module's README or training arguments) and if a training is currently running.
* ``UI``: :ref:`Gradio User Interface <howtos/deploy/nomad:2.1 UI prediction>`, only accessible if you launched with the DEEPaaS command.
* ``Custom``: a custom UI created by the module's developer (if any)

Under :material-outlined:`terminal;1.5em` ``Quick access`` you will be able to access the service you deployed at launch time.

If you had a deployment that took more than a week to deploy you will receive an :material-outlined:`mark_email_unread;1.5em` email notification when it is finally deployed.

.. admonition:: Deployment deletion :material-outlined:`delete;1.5em`
   :class: tip

   Sometimes deployments can get stuck in the deletion process, thus not completely freeing the resources you are consuming (eg. GPUs). If this is the case, please try re-deleting them again. This time it should execute a hard delete, completely purging your deployment.


.. _dashboard_snapshots:

Creating a snapshot of a deployment
-----------------------------------

In the ``Modules`` table, you will see a :material-outlined:`add_a_photo;1.5em` ``Create snapshot`` option.

This will allow to create a snapshot of any module you have deployed. This come especially handy for example when a downtime of the cluster is expected and you do not want to lose your work, or when you don't plan to keep working on something for a period of time but you don't want to keep consuming the resources.

Once you click in the button, the snapshot will appear below, in the ``Snapshots`` table.
You can redeploy snapshots at any time by clicking in the :material-outlined:`view_in_ar;1.5em` ``Redeploy snapshot`` button, where you will be asked whether to redeploy in :doc:`standard mode </howtos/train/standard>` or :doc:`batch mode </howtos/train/batch>`.

.. image:: /_static/images/dashboard/deployments_snapshots.png

.. _dashboard_statistics:

View your statistics
--------------------

In the ``Dashboard`` tab (in the Navigation panel on the left) you can access different types of statistics from the platform.

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
