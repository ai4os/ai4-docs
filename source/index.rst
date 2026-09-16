Welcome to AI4EOSC documentation!
=================================

The ``AI4EOSC`` platform empowers scientists by lowering the barrier to adopt the latest
AI models and tools. The platform provides a user-friendly workbench to easily train,
deploy, share and monitor AI models. It covers the full ML lifecycle: from model creation
and training to deployment and monitoring in production, adhering strictly to FAIR
principles for science (fully open-source and portable with no vendor lock-in). Furthermore,
AI4EOSC is actively expanding to support Generative AI (GenAI) and agentic workflows for
scientific research.


The AI4EOSC Ecosystem
---------------------

The platform is developed and expanded through a collaborative ecosystem of **projects**,
**gateways**, and scientific **communities**:

* **Projects** (`DEEP-HDC <https://deep-hybrid-datacloud.eu/>`__, `AI4EOSC <https://ai4eosc.eu/>`__, `AI4Life <https://ai4life.eurobioimaging.eu/>`__, `iMagine <https://imagine-ai.eu/>`__, `EOSC-ARENA <https://eosc-arena.eu/>`__, `FLUID-AI <https://fluid-ai.eu/>`__, `GenAI4Earth <https://genai4earth.eu/>`__):
  EU-funded initiatives that develop and extend the AI4EOSC platform with new capabilities—from core MLOps, distributed training, and composite AI to Generative AI, agentic environments, and FAIR data/model interoperability.

* **Gateways** (`AI4EOSC <https://dashboard.cloud.ai4eosc.eu/>`__, `iMagine <https://dashboard.cloud.imagine-ai.eu/>`__, `AI4Life <https://ai4life.cloud.ai4eosc.eu/>`__, `KMD4EOSC <https://kmd4eosc.pl/>`__, `Tutorials <https://tutorials.cloud.ai4eosc.eu/>`__):
  Dedicated instances of the AI4EOSC platform built on top of the shared platform foundation (common API, authentication, and compute/storage infrastructure). Each gateway is customized with specific branding, tools, and domain-specific model catalogs to access dedicated resources for a given community.

* **Communities & Scientific Domains**:
  Scientific communities group researchers within specific domains (e.g., climate forecasting, genomics and life sciences, aquatic imaging and biodiversity, and interdisciplinary science). One gateway serves a given community, while a single community can leverage several gateways to access the AI models and computing tools relevant to their research.


.. grid:: 2
    :gutter: 3

    .. grid-item-card:: :fas:`sign-hanging;fa-lg sd-mr-2`  Getting started
        :link: /getting-started/index
        :link-type: doc

        Start here to get an overview of the platform and how to use it.

    .. grid-item-card:: :material-outlined:`dashboard;1.5em`  Dashboard
        :link: /dashboard/index
        :link-type: doc

        Learn how to navigate the dashboard and make deployments.

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

   getting-started/quickstart
   getting-started/register
   getting-started/overview
   getting-started/new-features


.. toctree::
   :titlesonly:
   :maxdepth: 2
   :caption: AI4EOSC Dashboard
   :hidden:

   dashboard/catalog
   dashboard/deployments
   dashboard/statistics
   dashboard/profile



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

   AI4EOSC LLM <reference/llm>
   Storage <reference/storage>
   AI Modules <reference/modules>
   User access levels <reference/user-access-levels>

.. toctree::
   :titlesonly:
   :maxdepth: 2
   :caption: Considerations
   :hidden:

   Environmentally aware <considerations/footprint>
   Privacy first <considerations/privacy>
   FAIR by design <considerations/fair>

.. toctree::
   :titlesonly:
   :maxdepth: 2
   :caption: Help and support
   :hidden:

   help/index
   help/faq
   help/glossary

.. toctree::
   :titlesonly:
   :maxdepth: 2
   :caption: Other resources
   :hidden:

   External links <others/other-links>
   Useful Machine Learning resources <others/useful-ml-resources>
   Video demos <others/video-demos>

.. toctree::
   :titlesonly:
   :maxdepth: 2
   :caption: Advanced topics
   :hidden:

   DEEPaaS API <advanced/api>
   Use RCLONE to sync your dataset <advanced/rclone>
   RCLONE code examples <advanced/rclone-examples>

.. toctree::
   :maxdepth: 2
   :titlesonly:
   :hidden:
   :caption: Technical documentation

   Support a new project <technical/support-new-project>
   Organize a tutorial <technical/organize-tutorial>
   Compatible storage providers <technical/storage-providers>


.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`search`
