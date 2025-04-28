Welcome to AI4OS/AI4EOSC documentation!
=======================================

The ``AI4EOSC`` platform and the ``AI4OS`` stack empowers scientist by lowering the
barrier to adopt the latest AI models and tools. The platform provides a user-friendly
workbench to easily train, deploy, share and monitor AI models. The stack provides a set
of tools and services to easily create and deploy AI models.

It covers the full ML cycle: from model creation, to training, deployment and monitoring
in production. Following the FAIR principles for science, both our software (platform
and models) are fully open-source and easily portable to any other platform (no vendor
lock-in!).

Current supported platforms:

   * `AI4EOSC <https://ai4eosc.eu/>`__: AI for the European Open Science Cloud
   * `iMagine <https://imagine-ai.eu/>`__: Imaging data and services for aquatic science
   * `AI4Life <https://ai4life.eurobioimaging.eu/>`__: AI models and methods for the life sciences



.. grid:: 2
    :gutter: 3

    .. grid-item-card:: :fas:`sign-hanging;fa-lg sd-mr-2`  Getting started
        :link: /getting-started/index
        :link-type: doc

        Start here to get an overview of the platform and how to use it.

    .. grid-item-card:: :fas:`circle-info;fa-lg sd-mr-2`  How-Tos
        :link: /howtos/index
        :link-type: doc

        How to accomplish common tasks, such as trying a model, developing a new one,
        training, deploying, etc.

    .. grid-item-card:: :fas:`book;fa-lg sd-mr-2`  Reference
        :link: /reference/index
        :link-type: doc

        Detailed information about the platform, dashboard, storage, modules, etc. and
        how to use them.

    .. grid-item-card:: :fas:`question;fa-lg sd-mr-2`  Help and support
        :link: /help/index
        :link-type: doc

        Get help and support, including a FAQ section.

    .. grid-item-card:: :fas:`link;fa-lg sd-mr-2`  Other resources
        :link: /others/index
        :link-type: doc

        Useful Machine Learning resources, video demos, and other links.


.. toctree::
   :titlesonly:
   :maxdepth: 1
   :hidden:
   :glob:
   :caption: Start here

   getting-started/terminology
   getting-started/quickstart
   getting-started/register
   getting-started/user-roles
   getting-started/new-features


.. toctree::
   :maxdepth: 3
   :caption: Howto guides
   :hidden:

   howtos/try/index
   howtos/develop/index
   howtos/train/index
   howtos/deploy/index
   howtos/pipelines/index


.. toctree::
   :titlesonly:
   :maxdepth: 2
   :caption: User reference
   :hidden:

   User access levels <reference/user-access-levels>
   AI4OS Dashboard <reference/dashboard>
   AI4OS Storage <reference/storage>
   AI4OS Modules <reference/modules>
   AI4OS Modules Template <reference/cookiecutter-template>
   AI4OS LLM chatbot <reference/llm>


.. toctree::
   :titlesonly:
   :maxdepth: 2
   :caption: Advanced topics
   :hidden:

   RClone code examples <reference/rclone-code-examples>
   DEEPaaS API <reference/api>

.. toctree::
   :titlesonly:
   :maxdepth: 2
   :caption: Help and support
   :hidden:

   help/index
   help/faq

.. toctree::
   :titlesonly:
   :maxdepth: 2
   :caption: Other resources
   :hidden:

   External links <others/other-links>
   Useful Machine Learning resources <others/useful-ml-resources>
   Video demos <others/video-demos>

.. toctree::
   :maxdepth: 2
   :titlesonly:
   :hidden:
   :caption: Resource provider documentation

   technical/index

.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`search`
