Frequently Asked Questions (FAQ)
================================

This page gathers know issues of the platform, along with possible solutions.
If your issue does not appear here, please contact support.

.. TODO: check if the FAQ still apply

🔥 rclone fails to connect
--------------------------

You tried to connect to connect to the `AI4OS Nextcloud <https://share.services.ai4os.eu/>`__
and you are returned the following error message:

.. code:: console

    root@b79d4b9279f6:/srv# rclone about rshare:
    2024/02/05 13:26:56 Failed to create file system for "rshare:": the remote url looks incorrect. Note that nextcloud chunked uploads require you to use the /dav/files/USER endpoint instead of /webdav. Please check 'rclone config show remotename' to verify that the url field ends in /dav/files/USERNAME

This is due to a `change in endpoints <https://github.com/rclone/rclone/issues/7103>`__
introduced in RCLONE ``1.63.X``:

.. code-block::

    old endpoint: https://share.services.ai4os.eu/remote.php/webdav/
    new endpoint: https://share.services.ai4os.eu/remote.php/dav/files/<USER>

So you are experiencing this because you are running RCLONE with version higher than
1.62.

To fix this run the following command which will overwrite your endpoint:

.. code-block:: console

    $ echo export RCLONE_CONFIG_RSHARE_URL=${RCLONE_CONFIG_RSHARE_URL//webdav}/dav/files/${RCLONE_CONFIG_RSHARE_USER} >> /root/.bashrc


More info on how to :ref:`configure rclone <user/howto/rclone:Configuring rclone>`.

.. TODO: another option is to fix the rclone version to 1.62.2

.. To install rclone on a Docker container based on Ubuntu you should add the following code:

.. .. code-block:: docker

..     # Install rclone (needed if syncing with NextCloud for training; otherwise remove)
..     RUN curl -O https://downloads.rclone.org/v1.62.2/rclone-v1.62.2-linux-amd64.deb && \
..         apt install ./rclone-v1.62.2-linux-amd64.deb && \
..         mkdir /srv/.rclone/ && \
..         touch /srv/.rclone/rclone.conf && \
..         rm rclone-current-linux-amd64.deb && \
..         rm -rf /var/lib/apt/lists/*

.. To install it directly on your machine:

.. .. code-block:: console

..     $ curl -O https://downloads.rclone.org/v1.62.2/rclone-v1.62.2-linux-amd64.deb
..     $ apt install ./rclone-v1.62.2-linux-amd64.deb
..     $ rm rclone-current-linux-amd64.deb


🔥 I ran out of disk in my deployment
--------------------------------------

The current Nomad cluster has not the ability to properly isolate disk between
different users using the same physical machine. So it might be the case that some
user might be using more resources than their due share, thus consuming the disk
of other users that share their same node.
We are planning to fix this issue in the new cluster we are setting up.

In the meantime, if you are sure that `you are using less than 20 GB of disk`,
but you still find that there is not disk left, please contact support.


🔥 My GPU just disappeared from my deployment
---------------------------------------------

You try to list to GPU and it doesn't appear:

.. code-block:: console

    $ nvidia-smi
    Failed to initialize NVML: Unknown Error"

This is due to `this issue <https://github.com/NVIDIA/nvidia-docker/issues/1730>`__.
It should get fixed when we upgrade the GPU drivers, and this is planned for
the next Nomad cluster we are setting up.

In the meantime, your best option is to delete your deployment and create a new one.


🔥 I delete my deployment but it keeps reappearing
--------------------------------------------------

No fix for this yet. Happens from time to time, for unknown reasons.
Hopefully this will be magically fixed in the new cluster we are setting up with
the upgraded Nomad version.


🔥 Service X is not working
---------------------------

Check the `Status page <https://status.ai4eosc.eu/>`__ to see if there is any
maintenance action going on.
If you don't see anything, wait a couple of hours to make sure it is not a
temporary issue.

If the issue persists, please contact support.
