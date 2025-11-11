How to use Nextcloud with rclone
================================

**rclone** is a tool that enables you to synchronize contents between your machine and a remote storage.
It is kind of an `rsync <https://linux.die.net/man/1/rsync>`__ but for remote storages.
Although we will demonstrate here how to use it with Nextcloud, it can be used with many different remote storages (Dropbox, Google Drive, Amazon S3, etc)


.. _rclone_installation:

1. Installing rclone
--------------------

All applications in the :doc:`AI4OS Dashboard</reference/dashboard>` are packed in a Docker image and have `rclone <https://rclone.org/>`__ installed by default. If you want to create a Docker containing your own application, you should install rclone in the container to be able to access the data stored remotely. When developing an application with the :doc:`AI4OS Modules Template </reference/cookiecutter-template>`, the Dockerfile already includes installation of rclone.

To install rclone on a Docker container you should add the following code to your Dockerfile:

.. code-block:: docker

    RUN curl https://rclone.org/install.sh | bash

To install it locally on your machine:

.. code-block:: console

    $ curl https://rclone.org/install.sh | sudo bash


.. _rclone_configuration:

2. Configuring rclone
---------------------

... in a Dashboard deployment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before creating the deployment you must do the following:

1. :ref:`Sync Nextcloud from the profile section <dashboard_profile>`. This will create your rclone credentials.
2. :ref:`Select Nextcloud when configuring the deployment <dashboard_storage>`. This will set set up rclone configuration for you via setting environment variables in your deployment.

When the deployment is created, you should have your env variables available to work with the latest RCLONE:

.. code-block:: console

    $ printenv | grep RCLONE_CONFIG_RSHARE_
    RCLONE_CONFIG_RSHARE_VENDOR=nextcloud
    RCLONE_CONFIG_RSHARE_PASS=<YOUR-PASSWORD>
    RCLONE_CONFIG_RSHARE_URL=https://share.cloud.ai4eosc.eu/remote.php/dav/files/<YOUR-USER>
    RCLONE_CONFIG_RSHARE_TYPE=webdav
    RCLONE_CONFIG_RSHARE_USER=<YOUR-USER>

.. dropdown:: ㅤㅤ A note on older RCLONE versions

    In RCLONE versions ``=< 1.62.2``, the RCLONE environment variables had the following shape (`issue <https://github.com/rclone/rclone/issues/7103>`__).

    .. code-block:: console

        RCLONE_CONFIG_RSHARE_VENDOR=nextcloud
        RCLONE_CONFIG_RSHARE_PASS=<YOUR-PASSWORD>
        RCLONE_CONFIG_RSHARE_URL=https://share.cloud.ai4eosc.eu/remote.php/webdav/
        RCLONE_CONFIG_RSHARE_TYPE=webdav
        RCLONE_CONFIG_RSHARE_USER=<YOUR-USER>

    So in your module uses an old version of RCLONE, you can either:

    1. Update to a newer RCLONE version,
    2. Still use and old version but make sure to update your ``.bashrc`` with these variables.


... in your local machine
^^^^^^^^^^^^^^^^^^^^^^^^^

First, you need to generate your RCLONE credentials. For this, log into the `AI4OS Nextcloud <https://share.cloud.ai4eosc.eu/>`__,  go to (1) **Settings** (top right corner) ➜ (2) **Security** ➜ (3) **Devices & sessions**. Set a name for your application (typically in the docs we will use ``rshare``) and click on **Create new app password**. This will generate your ``<user>`` and ``<password>`` credentials. Your username should start with ``EGI_Checkin-...``.

.. image:: /_static/images/nextcloud/access.png

Then run ``rclone config`` command, these are the answers you should provide:

.. code-block:: console

    $ rclone config
    # choose "n"  for "New remote"
    # choose name for AI4OS Nextcloud --> rshare
    # choose "Type of Storage" --> Webdav
    # provide AI4OS Nextcloud URL for webdav access --> ttps://share.cloud.ai4eosc.eu/remote.php/dav/files/<YOUR-USER>
    # choose Vendor --> Nextcloud
    # specify "user" --> (see `<user>` in "Configuring rclone" above).
    # password --> y (Yes type in my own password)
    # specify "password" --> (see `<password>` in "Configuring rclone" above).
    # bearer token --> ""
    # Edit advanced config? --> n (No)
    # Remote config --> y (Yes this is OK)
    # Current remotes --> q (Quit config)

This will create an configuration file in ``$HOME/.config/rclone/rclone.conf``.:

.. code-block::

    [rshare]
    type = webdav
    url = https://share.cloud.ai4eosc.eu/remote.php/dav/files/<YOUR-USER>
    vendor = nextcloud
    user = <YOUR-USER>
    pass = <YOUR-PASSWORD>  --> this is equivalent to `rclone obscure <password>`

.. admonition:: Security warning
    :class: tip

    For security reasons, the ``rclone.conf`` should never be saved as part of the Docker image. If you are running rclone from inside a Docker container, you should mount ``rclone.conf`` at runtime directly as a volume.

    .. code-block:: console

        $ docker run -ti -v $HOSTDIR_WITH_RCLONE_CONF/rclone.conf:/$HOME/.config/rclone/rclone.conf <your-docker-image>

    One can also mount the ``rclone.conf`` file at a custom location and tell rclone where to find it:

    .. code-block:: console

        $ docker run -ti -v $HOSTDIR_WITH_RCLONE_CONF/rclone.conf:/custom/path/to/rclone.conf <your-docker-image>
        $ rclone --config /custom/path/to/rclone.conf


.. _rclone_usage:

3. Using rclone
---------------

You can check that everything works fine with:

.. code-block:: console

    $ rclone listremotes    # check you don't have two remote storages with same name
    $ rclone about rshare:  # should output your used space in Nextcloud.

.. dropdown:: ㅤ 🛠️ Troubleshooting duplicate remotes

    If ``listremotes`` is listing two remotes with the same name you probably configured the rclone twice.
    Most likely you ran ``rclone config`` on a machine deployed with the Dashboard, so you have both the ``env`` and ``rclone.conf`` configurations.

    To fix this, either remove the ``env`` variables (echo ``unset`` command into the ``.bashrc``) or delete the ``rclone.conf`` file.

You can start copying files from your remote to your local:

.. code-block:: console

    $ rclone copy rshare:/some/remote/path /some/local/path

Uploading to Nextcloud can be particularly slow if your dataset is composed of lots of small files.
Considering zipping your folder before uploading.

.. code-block:: console

    $ zip -r <foldername>.zip <foldername>
    $ unzip <foldername>.zip
