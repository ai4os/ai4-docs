Storage
=======

For hosting the data necessary for your trainings, we provide access form inside your
deployments to the following hosting platforms:

* `AI4OS Nextcloud <https://share.services.ai4os.eu/>`__: this is a Nextcloud instance
  deployed for the project users. Each user gets a free 5 TB of storage there.


To able able to access storage from your deployment, you need to properly
:ref:`configure your Storage <user/overview/dashboard:Storage configuration>`
when creating your deployment.

You have currently two ways of accessing your Nextcloud files from your deployment:

1. you can :ref:`copy them locally <user/howto/rclone:3. Using rclone>` to your deployment disk using rclone.

2. you can access them in the ``/storage`` path in your deployment. This is a `virtual
   filesystem <https://rclone.org/commands/rclone_mount/>`__ that lets you access the Nextcloud storage via the network.

Reading files from disk (**1**) is faster than reading them via the network (**2**).
But as deployments have a limited disk capacity (couple tens of GBs),
sometimes you have no other option than going with (**2**) if you want to train with a
really big dataset.

If you configured the :ref:`Download of an external dataset <user/overview/dashboard:Storage configuration>`
the dataset will be available under ``/storage/ai4os-storage/datasets``.

Do you have any issues? Please check the :ref:`FAQ (storage) questions <user/support/faq:Storage issues>`.
