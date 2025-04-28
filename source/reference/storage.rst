Storage
=======

Our storage provider
--------------------

For hosting the data necessary for your trainings, we provide access form inside your
deployments to the following hosting platforms:

* `AI4OS Nextcloud <https://share.services.ai4os.eu/>`__: this is a Nextcloud instance
  deployed for the project users. Each user gets a free 500 GB of storage there.

  .. admonition:: Account validation
     :class: important

     The first time you access this storage, you will need to contact the admins to validate your account.

  .. image:: /_static/images/nextcloud/folders.png


Accessing storage from inside your deployment
---------------------------------------------

To be able to access the Nextcloud storage from inside your deployment, you need to properly :ref:`configure your Storage <dashboard_storage>` when creating your deployment.

You have currently two ways of accessing your Nextcloud files from your deployment:

1. you can access them in the ``/storage`` path in your deployment.

   This is the **🌟️recommended method🌟️** for most users.
   It mounts a `virtual filesystem <https://rclone.org/commands/rclone_mount/>`__ that lets you access the Nextcloud storage via the network.

   If you configured the :ref:`Download of an external dataset <dashboard_storage>` the dataset will be available under ``/storage/ai4os-storage/datasets``.

2. you can copy the files to your deployment's local disk.

   This can be done in two ways:

   a. You can copy them from the ``/storage`` path to your desired local path.
   b. You can copy them directly from Nextcloud :ref:`using rclone <rclone_usage>`.

**Pros and Cons of each approach**:
Reading files from disk (**2**) is faster than reading them via the network (**1**).
But as deployments have a limited disk capacity (couple tens of GBs),
sometimes you have no other option than going with (**1**) if you want to train with a
really big dataset.

.. tip::

   Do you have any issues? Please check the :ref:`FAQ (storage) questions <faq_storage>`.
