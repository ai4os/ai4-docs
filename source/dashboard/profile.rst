.. _dashboard_profile:

Profile & more
==============

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

  * the :doc:`Storage </reference/storage>` as well as :doc:`external storage providers </technical/storage-providers>`,
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


.. _dashboard_ask_ai:

Ask AI
------

Finally, we have our :ref:`LLM Assistant <reference/llm:Ask questions about the documentation>` directly available from the Dashboard. You can ask it questions and it will use this documentation as a Knowledge Base to offer grounded responses.

.. image:: /_static/images/dashboard/ai-assistant.png
