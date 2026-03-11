Concepts and Terminology
========================

There are several different components in the AI4OS/AI4EOSC stack that are relevant for the users.
Later on you will see how each :doc:`different type of user <user-roles>` can take advantage of the different components.

.. admonition:: What is the difference between AI4OS and AI4EOSC?
   :class: info

   `AI4OS <https://ai4os.eu/>`__ is the name of the software stack described in this documentation.

   `AI4EOSC <https://ai4eosc.eu/>`__ is the project that initially developed that stack and is currently maintaining it.
   AI4EOSC also host a particular deployment of the AI4OS stack components (under `cloud.ai4eosc.eu`).
   For example:

   * The :doc:`Dashboard </reference/dashboard>` deployed as the `AI4EOSC Dashboard <https://dashboard.cloud.ai4eosc.eu/>`__,
   * The :doc:`Storage </reference/storage>` deployed as the `AI4EOSC Storage <https://share.cloud.ai4eosc.eu/>`__,
   * etc.

   In this regard, it is similar to other projects who have adopted the AI4OS Stack,
   like `iMagine <https://www.imagine-ai.eu/>`__ who deployed it's own version of the
   AI4OS Dashboard as the `iMagine Dashboard <https://dashboard.cloud.imagine-ai.eu/>`__.

   To reduce duplicities and lower the entry barrier for external projects, many
   AI4OS components deployed by AI4EOSC (e.g. the `CI/CD pipeline <https://jenkins.cloud.ai4eosc.eu/>`__ or the `Login <https://login.cloud.ai4eosc.eu/realms/ai4eosc/account>`__)
   also serve others projects, like iMagine.


Dashboard
---------

The :doc:`Dashboard </reference/dashboard>` allows users to access computing resources to deploy, perform inference and train AI modules.
The Dashboard simplifies the deployment and hides some of the technical parts that most users do not need to worry about.


AI modules
----------

The :doc:`AI modules </reference/modules>` are developed both by the platform and by users.
For creating modules, we provide the :doc:`AI Modules Template </reference/modules/template>`
as a starting point.
Every AI module of the platform exposes it's functionality under a :doc:`common API </advanced/api>`, so that models can be accessed in a consistent way.

In addition to AI modules, the Dashboard also allows to deploy tools
(eg. a :doc:`Federated Server </howtos/train/federated-flower>`).


Training infrastructure
-----------------------

The Dashboard allows to deploy AI models in a **federated** computing infrastructure, based on `Nomad <https://developer.hashicorp.com/nomad>`__.
Each supported project can bring their own computing resources that can either be used exclusively by project members or shared with other projects.

Those are the datacenters that are currently part of the federation:

.. raw:: html

    <iframe style="width: 100%; height: 500px; border: 0;" allowfullscreen allow="geolocation" src="https://umap.openstreetmap.fr/en/map/ai4os-datacenters_1307858?scaleControl=false&miniMap=false&scrollWheelZoom=true&zoomControl=false&editMode=disabled&moreControl=false&searchControl=false&tilelayersControl=false&embedControl=false&datalayersControl=false&onLoadPanel=none&captionBar=false&captionMenus=true&captionControl=false&locateControl=false&measureControl=false&editinosmControl=false&printControl=false#4/44.72/6.15"></iframe>

Inference infrastructure
------------------------

The inference infrastructure, based on `OSCAR <https://oscar.grycap.net/>`__, allows users to deploy trained AI modules in :doc:`serverless mode </howtos/deploy/oscar>`. It supports horizontal scalability, quickly adapting to peaks in demand.
Users can also compose those modules in :doc:`complex AI workflows </howtos/pipelines/flowfuse>`.

Other non-serverless deployment options :doc:`are available </howtos/deploy/index>`, including deploying in external clouds.

The Storage
-----------

:doc:`Storage </reference/storage>` is is connected transparently to deployments, so that users can train AI modules on their custom data.


Architecture overview
---------------------

If you are curious, this is a very high level architecture overview of the platform:

.. image:: /_static/images/ai4eosc/architecture.png

And if you are feeling super-nerdy 🤓️, these are the low-level
`C4 architecture diagrams <https://structurizr.com/share/73873/2f769b91-f208-41b0-b79f-5e196435bdb1>`__
of the platform.
