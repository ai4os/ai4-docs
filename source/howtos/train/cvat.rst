.. _labeling-images-with-cvat:

Labeling images with CVAT
=========================

.. admonition:: Requirements
   :class: info

   🔒 This tutorial requires :ref:`full authentication <getting-started/register:Full authentication>`.

In this tutorial, we will guide you on how to use the `Computer Vision Annotation Tool (CVAT) <https://www.cvat.ai/>`__ in the AI4OS platform to annotate images.

Deploying CVAT
--------------

The CVAT tool is located at the top of the :ref:`Marketplace <dashboard_marketplace>`, in the ``Tools`` section.

The workflow for deploying CVAT is similar to the one for :doc:`deploying a module </reference/dashboard>`.
In this particular case, you will need to pay attention to:

* **CVAT credentials**:
  When configuring the deployment of CVAT, you will need to enter your ``CVAT username``  and ``CVAT password`` to authenticate yourself in the CVAT instance.

* **Storage**:
  For using CVAT, it is *mandatory* to have a :ref:`storage provider linked <dashboard_profile>`.
  This is because, each time you delete a CVAT instance a snapshot will automatically be created in your storage.
  When you deploy a new CVAT instance, you can either start from an existing snapshot or from a blank state (no snapshot).

  .. image:: /_static/images/dashboard/storage-cvat-snapshots.png


Using CVAT
----------

In the :ref:`deployments list <dashboard-manage-deployments>` you will be able to see your newly created CVAT instance.
Clicking the ``Quick access`` button, you will directly enter the CVAT UI.

.. image:: /_static/images/endpoints/cvat-login.png

The enter you ``CVAT username``  and ``CVAT password`` and voilá, you're in!

.. image:: /_static/images/endpoints/cvat-projects.png


CVAT uses a hierarchical structure to organize annotation work:

- **Projects** are used to organize multiple related tasks under a shared label schema and configuration. Projects are ideal for managing large annotation efforts that span multiple datasets or annotation tasks.

- **Tasks** are a specific annotation assignment within a project. Each task defines the label schema to use for annotation and contains the data to be annotated.

- **Jobs** are a subdivision of a task, containing a subset of the data. They allow for the distribution of annotation work among different annotators.

We recommend creating start by creating a project then create subsequent tasks.
Creating a project is important because this will enable :ref:`periodic backups <howtos/train/cvat:CVAT automated backups>` to automatically be generated.

Connecting your dataset
^^^^^^^^^^^^^^^^^^^^^^^

When creating a new task you have to provide some data to annotate.
You have the following options:

1. **My computer**: Upload data from your local computer
2. **Connected file share**: Use datasets you already have in the :doc:`AI4OS Storage </reference/storage>`.

   In this case, anything you save under ``ai4os-storage/tools/cvat/share`` will be available for annotation in CVAT.

3. **Remote sources**: Use publicly available images, by providing URLs.

   For example, you can make public any folder in the :doc:`AI4OS Storage </reference/storage>` by clicking :material-outlined:`more_horiz;1.5em` → :material-outlined:`info;1.5em` ``Open details`` → :material-outlined:`link;1.5em` ``Share link``

4. **Cloud storage**: In case you have your dataset hosted on ASW S3, Azure or Google Cloud.


For more information on using CVAT, please follow the `official CVAT documentation <https://docs.cvat.ai/docs/>`__.

.. image:: /_static/images/endpoints/cvat-ai-screencast.gif
    :width: 1000px

CVAT automated backups
----------------------

Annotating a dataset is a very time consuming task, so having automated backups is a must.

In AI4OS, we support multiple ways to backup your annotations.
All those backup are saved in the :doc:`AI4OS storage </reference/storage>` under ``ai4os-storage/tools/cvat``.

To avoid collapsing your storage quota, we adapt the backup schedule to the backup size (ie. lighter backups are made more frequently).
The performed backups are:

* **when a deployment is deleted by the user**, we save a full backup of the deployment. This not only includes project annotations, but also meta configurations (like user groups).
  Those are the snapshots that you will later be able to :ref:`select in the configuration form <howtos/train/cvat:Deploying CVAT>`.

  Location:  ``ai4os-storage/tools/cvat/backups``

* **every day**, we save a full project backup with images and annotations.
  To restore from that backup, you will need to import it manually in the CVAT UI.

  Location:  ``ai4os-storage/tools/cvat/backups-periodic``

* **every hour**, we save a project backup just with annotations.
  To restore from that backup, you will need to import it manually in the CVAT UI.

  Location:  ``ai4os-storage/tools/cvat/backups-periodic``
