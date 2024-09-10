How to use Nextcloud with rclone
================================

**rclone** is a tool that enables you to synchronize contents between your machine and a remote storage.
It is kind of an `rsync <https://linux.die.net/man/1/rsync>`__ but for remote storages.
Although we will demonstrate here how to use it with Nextcloud, it can be used with many different remote storages (Dropbox, Google Drive, Amazon S3, etc)


1. Installing rclone
--------------------

All applications in the :doc:`AI4OS Dashboard</user/overview/dashboard>` are packed in a Docker image and have `rclone <https://rclone.org/>`__ installed by default. If you want to create a Docker containing your own application, you should install rclone in the container to be able to access the data stored remotely. When developing an application with the :doc:`AI4OS Modules Template </user/overview/cookiecutter-template>`, the Dockerfile already includes installation of rclone.

To install rclone on a Docker container based on Ubuntu you should add the following code:

.. code-block:: docker

    # Install rclone (needed if syncing with NextCloud for training; otherwise remove)
    RUN curl -O https://downloads.rclone.org/rclone-current-linux-amd64.deb && \
        dpkg -i rclone-current-linux-amd64.deb && \
        apt install -f && \
        mkdir /srv/.rclone/ && \
        touch /srv/.rclone/rclone.conf && \
        rm rclone-current-linux-amd64.deb && \
        rm -rf /var/lib/apt/lists/*

To install it directly on your machine:

.. code-block:: console

    $ curl -O https://downloads.rclone.org/rclone-current-linux-amd64.deb
    $ dpkg -i rclone-current-linux-amd64.deb
    $ apt install -f
    $ rm rclone-current-linux-amd64.deb

For other Linux flavors, please refer to the `rclone official site <https://rclone.org/downloads/>`__.


2. Configuring rclone
---------------------

... in a Dashboard deployment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before creating the deployment you must do the following:

1. :ref:`Sync Nextcloud from the profile section <user/overview/dashboard:Profile>`. This will create your rclone credentials.
2. :ref:`Select Nextcloud when configuring the deployment <user/overview/dashboard:Storage configuration>`. This will set set up rclone configuration for you via setting environment variables in your deployment.

Once your deployment is running, you must run the following command in the terminal to properly configure rclone:

.. code-block:: console

    $ echo export RCLONE_CONFIG_RSHARE_PASS=$(rclone obscure $RCLONE_CONFIG_RSHARE_PASS) >> /root/.bashrc
    $ source /root/.bashrc

.. We do this to spare users from having to install rclone in their local machines just to obscure the password.

This is because, to connect with the remote, rclone needs to use an obscured version of the password, not the raw one.

If your rclone version is higher than ``1.62.2``, then you must need to adapt the
endpoint, running this command
(see :ref:`Frequently Asked Questions <user/support/faq:🔥 rclone fails to connect>` for more info):

.. code-block:: console

    $ echo export RCLONE_CONFIG_RSHARE_URL=${RCLONE_CONFIG_RSHARE_URL//webdav\/}dav/files/${RCLONE_CONFIG_RSHARE_USER} >> /root/.bashrc
    $ source /root/.bashrc

You can always check those env variables afterwards:

.. code-block:: console

    $ printenv | grep RCLONE_CONFIG_RSHARE_
    RCLONE_CONFIG_RSHARE_VENDOR=nextcloud
    RCLONE_CONFIG_RSHARE_PASS=***some-password***
    RCLONE_CONFIG_RSHARE_URL=https://share.services.ai4os.eu/remote.php/webdav/
    RCLONE_CONFIG_RSHARE_TYPE=webdav
    RCLONE_CONFIG_RSHARE_USER=***some-user***

and modify them if needed:

.. code-block:: console

    $ export RCLONE_CONFIG_RSHARE_PASS=***new-password***
    # remember this should an obscured version of the raw password --> `rclone obscure <raw-password>`

... in your local machine
^^^^^^^^^^^^^^^^^^^^^^^^^

First, you need to generate your RCLONE credentials. For this, log into the `AI4OS Nextcloud <https://share.services.ai4os.eu/>`__,  go to (1) **Settings** (top right corner) ➜ (2) **Security** ➜ (3) **Devices & sessions**. Set a name for your application (typically in the docs we will use ``rshare``) and click on **Create new app password**. This will generate your ``<user>`` and ``<password>`` credentials. Your username should start with ``EGI_Checkin-...``.

.. image:: /_static/images/nextcloud/access.png

Then run ``rclone config`` command, these are the answers you should provide:

.. code-block:: console

    $ rclone config
    # choose "n"  for "New remote"
    # choose name for AI4OS Nextcloud --> rshare
    # choose "Type of Storage" --> Webdav
    # provide AI4OS Nextcloud URL for webdav access --> https://share.services.ai4os.eu/remote.php/webdav/
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
    url = https://share.services.ai4os.eu/remote.php/webdav/
    vendor = nextcloud
    user = ***some-username***
    pass = ***some-userpassword**  --> this is equivalent to `rclone obscure <password>`

.. admonition:: Security warning
    :class: tip

    For security reasons, the ``rclone.conf`` should never be saved as part of the Docker image. If you are running rclone from inside a Docker container, you should mount ``rclone.conf`` at runtime directly as a volume.

    .. code-block:: console

        $ docker run -ti -v $HOSTDIR_WITH_RCLONE_CONF/rclone.conf:/$HOME/.config/rclone/rclone.conf <your-docker-image>

    One can also mount the ``rclone.conf`` file at a custom location and tell rclone where to find it:

    .. code-block:: console

        $ docker run -ti -v $HOSTDIR_WITH_RCLONE_CONF/rclone.conf:/custom/path/to/rclone.conf <your-docker-image>
        $ rclone --config /custom/path/to/rclone.conf


3. Using rclone
---------------

You can check that everything works fine with:

.. code-block:: console

    $ rclone listremotes    # check you don't have two remote storages with same name
    $ rclone about rshare:  # should output your used space in Nextcloud.

.. tip::

    If ``listremotes`` is listing two remotes with the same name you probably configured the rclone twice.
    Most likely you ran ``rclone config`` on a machine deployed with the Dashboard, so you
    have both the ``env`` and ``rclone.conf`` configurations. To fix this, either remove the ``env`` variables
    (echo ``unset`` command into the ``.bashrc``) or delete the ``rclone.conf`` file.

You can start copying files from your remote to your local:

.. code-block:: console

    $ rclone copy rshare:/some/remote/path /some/local/path

.. tip::

    Uploading to Nextcloud can be particularly slow if your dataset is composed of lots of small files.
    Considering zipping your folder before uploading.

    .. code-block:: console

        $ zip -r <foldername>.zip <foldername>
        $ unzip <foldername>.zip
