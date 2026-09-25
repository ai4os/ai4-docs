.. _dashboard_profile:

Profile & more
==============

Profile
-------

In the top-right corner, you will be able to find:

* :material-outlined:`notifications;1.5em`: notifications about the platforms, like expected downtimes and issues,
* :material-outlined:`account_circle;1.5em`: your profile details.


In your profile overview you will find your current groups (virtual organizations) and :doc:`access levels </reference/user-access-levels>`.
In the top banner you will also find your name, email and user ID.

.. image:: /_static/images/dashboard/profile/overview.png


Additionally, you also have the following dedicated tabs.

API keys
^^^^^^^^

This tab centralizes the API keys created for other services from the ecosystem.

.. image:: /_static/images/dashboard/profile/api_keys.png

Currently you can manage here the :ref:`AI4EOSC LLM API keys <reference/llm:Retrieve the API credentials>`. To generate a new key, just provide a key name and an expiration date.

Linked storages
^^^^^^^^^^^^^^^

This tab centralizes the storages you have linked to the platform.
Those storages will be :ref:`mounted in your deployments <dashboard/deployments:Storage configuration>`, so that you can transparently access your data during training. This storages also enable additional platform functionality like one-click dataset download or automated CVAT backups.

.. image:: /_static/images/dashboard/profile/storage.png

By default, you can one-click link the :ref:`AI4EOSC Storage <reference/storage:AI4EOSC Storage>` , based on Nextcloud.
You can also one-click link any other Nextcloud instance, provided it is :ref:`correctly configured <technical/storage-providers:Nextcloud>`.

For non-Nextcloud storages, we provide a manual linking option (``Add configuration manually``, at the bottom). You can manually add credentials of any `RCLONE-compatible storage <https://rclone.org/overview/>`__, which includes S3, Dropbox, Google Drive, Azure Blobs, Google Cloud Storage, OneDrive, etc.

.. dropdown:: :fab:`youtube;youtube-icon` ㅤLink with any NextCloud storage service

  .. raw:: html

      <div style="position: relative; padding-bottom: 56.25%; margin-bottom: 2em; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/PHbHq4KbmwE" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
      </div>

  :material-outlined:`error;1.5em` Please, be aware that video demos can become quickly outdated. In case of doubt, always refer to the written documentation.

Linked services
^^^^^^^^^^^^^^^

This tabs groups the services you have linked with the platform, including both internal AI4EOSC services, and external services.

.. image:: /_static/images/dashboard/profile/services.png

This currently includes:

* the :doc:`AI4EOSC MLflow </howtos/develop/mlflow>`, that allows you to track your ML training metrics.
* your `Hugging Face <https://huggingface.co/>`__ account, that allows you to :doc:`deploy an LLM  </howtos/deploy/llm>` behind End-User-License-Agreements (EULA).

In order to link a service, you have to click on the ``Link`` button, log in the popup window and grant access to the Dashboard.
If you have previously linked the service, you also have to to delete old credentials and generate new ones using ``Re-link``.


.. _dashboard_ask_ai:

Ask AI
------

Finally, we have our :ref:`LLM Assistant <reference/llm:Ask questions about the documentation>` directly available from the Dashboard. You can ask it questions and it will use this documentation as a Knowledge Base to offer grounded responses.

.. image:: /_static/images/dashboard/ai-assistant.png
