Storage
=======

Storage is  currently taken care of by the `AI4OS Nextcloud <https://data-deep.a.incd.pt/>`__ instance.

You have currently two ways of accessing your Nextcloud files from your deployment:

1. you can :ref:`copy them locally <user/howto/rclone:Using rclone>` to your deployment disk using rclone.

2. you can access them in the ``/storage`` path in your deployment. This is a `virtual
   filesystem <https://rclone.org/commands/rclone_mount/>`__ that lets you access the Nextcloud storage via the network.

For these options to work, you need to configure your :ref:`RCLONE credentials <user/howto/rclone:Configuring rclone>`
when launching your deployment (under **Storage** options).

Reading files from disk (**1**) is faster than reading them via the network (**2**).
But as deployments have a limited disk capacity (couple tens of GBs),
sometimes you have no other option than going with (**2**) if you want to train with a
really big dataset.

.. warning::

    With option (**2**):

    * File read errors can happen if the network is slow.

    * If you see the following error message when trying to access ``/storage``:

      .. code-block:: console

        ls: reading directory '/storage/': Input/output error

      this means you probably submitted the wrong :ref:`RCLONE credentials <user/howto/rclone:Configuring rclone>` during deployment.
      So please try to make a new deployment with the correct credentials.

.. tip::
    To free some space in your deployment, always make sure to delete files in the Trash
    (``/root/.local/share/Trash/files``).

:fa:`gear` In parallel, we are working on expanding disk capacity in the deployments! :fa:`gear`
