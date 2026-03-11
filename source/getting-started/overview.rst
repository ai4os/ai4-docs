Platform overview
=================

AI4EOSC provides a comprehensive platform for artificial intelligence and machine learning applications for scientific usecases. The project offers a federated computing infrastructure and shared services that enable researchers, developers, and organizations to collaborate on AI model development, training, and deployment at scale.

.. admonition:: A note on terminology
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


Components
----------

There are several different components in the AI4OS/AI4EOSC stack that are relevant for the users.
Later on you will see how each different type of user can take advantage of the different components.

Dashboard
^^^^^^^^^

The :doc:`Dashboard </reference/dashboard>` allows users to access computing resources to deploy, perform inference and train AI modules.
The Dashboard simplifies the deployment and hides some of the technical parts that most users do not need to worry about.


AI modules
^^^^^^^^^^

The :doc:`AI modules </reference/modules>` are developed both by the platform and by users.
For creating modules, we provide the :doc:`AI Modules Template </reference/modules/template>`
as a starting point.
Every AI module of the platform exposes it's functionality under a :doc:`common API </advanced/api>`, so that models can be accessed in a consistent way.

In addition to AI modules, the Dashboard also allows to deploy tools
(eg. a :doc:`Federated Server </howtos/train/federated-flower>`).


Training infrastructure
^^^^^^^^^^^^^^^^^^^^^^^

The Dashboard allows to deploy AI models in a **federated** computing infrastructure, based on `Nomad <https://developer.hashicorp.com/nomad>`__.
Each supported project can bring their own computing resources that can either be used exclusively by project members or shared with other projects.

Those are the datacenters that are currently part of the federation:

.. raw:: html

    <iframe style="width: 100%; height: 500px; border: 0;" allowfullscreen allow="geolocation" src="https://umap.openstreetmap.fr/en/map/ai4os-datacenters_1307858?scaleControl=false&miniMap=false&scrollWheelZoom=true&zoomControl=false&editMode=disabled&moreControl=false&searchControl=false&tilelayersControl=false&embedControl=false&datalayersControl=false&onLoadPanel=none&captionBar=false&captionMenus=true&captionControl=false&locateControl=false&measureControl=false&editinosmControl=false&printControl=false#4/44.72/6.15"></iframe>

Inference infrastructure
^^^^^^^^^^^^^^^^^^^^^^^^

The inference infrastructure, based on `OSCAR <https://oscar.grycap.net/>`__, allows users to deploy trained AI modules in :doc:`serverless mode </howtos/deploy/oscar>`. It supports horizontal scalability, quickly adapting to peaks in demand.
Users can also compose those modules in :doc:`complex AI workflows </howtos/pipelines/flowfuse>`.

Other non-serverless deployment options :doc:`are available </howtos/deploy/index>`, including deploying in external clouds.

The Storage
^^^^^^^^^^^

:doc:`Storage </reference/storage>` is is connected transparently to deployments, so that users can train AI modules on their custom data.


Architecture overview
^^^^^^^^^^^^^^^^^^^^^

If you are curious, this is a very high level architecture overview of the platform:

.. image:: /_static/images/ai4eosc/architecture.png

And if you are feeling super-nerdy 🤓️, these are the low-level
`C4 architecture diagrams <https://structurizr.com/share/73873/2f769b91-f208-41b0-b79f-5e196435bdb1>`__
of the platform.


Our different user roles
------------------------

The platform is focused on three different types of users.
Depending on what you want to achieve you should belong into one or more of the following categories:


.. image:: /_static/images/ai4eosc/user-roles.png


The basic user
^^^^^^^^^^^^^^

This user wants to use modules that are already pre-trained and test them with their data.
Therefore, they don't need to have any particular machine learning knowledge. For example, they can take an already trained module
for `plant classification <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/plants-classification>`__
that has been containerized, and use it to classify their own plant images.

**What the platform can offer to you:**

* a :doc:`Dashboard </reference/dashboard>` full of ready-to-use modules to perform inference with your data,
* a :doc:`GUI </howtos/deploy/nomad>` to easily interact with the services,
* an :doc:`API </advanced/api>` to integrate the AI modules with your own  services,
* solutions to run the inference in :doc:`the Cloud </howtos/deploy/cloud>` or in your :doc:`local resources </howtos/try/locally>`,
* the ability to :doc:`create pipelines </howtos/pipelines/index>` by composing different modules.

.. admonition:: Related HowTo's
   :class: info

   * :doc:`How to try a model </howtos/try/index>`
   * :doc:`How to deploy a model in production </howtos/deploy/index>`
   * :doc:`How to create AI model pipelines </howtos/pipelines/index>`


The intermediate user
^^^^^^^^^^^^^^^^^^^^^

The intermediate user wants to retrain an available module to perform the same task but
fine-tuning it to their own data.
They still might not need high level knowledge on modelling of machine learning problems, but typically do need basic
programming skills to prepare their own data into the appropriate format.
Nevertheless, they can re-use the knowledge being captured in a trained network and adjust the network to their problem
at hand by re-training the network on their own dataset.
An example could be a user who takes the generic `image classifier <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/ai4os-image-classification-tf>`__
model and retrains it to perform `plant classification <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/plant-classification>`__.

**What the platform can offer to you:**

* the ability to train out-of-the-box a module of the :doc:`Dashboard </reference/dashboard>`,
* the ability to easily connect your training to your dataset hosted on our :doc:`data storage resources </reference/storage>`,
* a private instance of :doc:`Computer Vision Annotation Tool (CVAT) </howtos/train/cvat>` to annotate your dataset,
* a private server to create :doc:`Federated Learning trainings with Flower </howtos/train/federated-flower>`,
* the ability to :doc:`use GPUs </howtos/train/standard>` to accelerate your training,
* an :doc:`API </advanced/api>` to easily interact with the model,
* solutions to deploy your developed model in :doc:`the Cloud </howtos/deploy/cloud>` or in your :doc:`local resources </howtos/try/locally>`,
* the ability to share your module with other users in the :ref:`Dashboard Marketplace <dashboard_marketplace>`.

.. admonition:: Related HowTo's
   :class: info

   * :doc:`How to train a model </howtos/train/index>`


The advanced user
^^^^^^^^^^^^^^^^^

The advanced users are the ones that will develop their own machine learning models
and therefore need to be competent in machine learning.
This would be the case for example if we provided an image classification model
but the users wanted to perform object localization, which is a fundamentally different task.
Therefore they will design their own neural network architecture, potentially re-using parts of the code from other
models.

**What the platform can offer to you:**

* a :doc:`ready-to-use IDE </howtos/develop/dashboard>` (VScode, Jupyterlab) with the main DL frameworks (Pytorch, Tensorflow) running on different types of hardware (CPUs, GPUs),
* the ability to easily connect your environment to your dataset hosted on our :doc:`data storage resources </reference/storage>`,
* the ability to integrate :doc:`experiment tracking with MLflow </howtos/develop/mlflow>` in your trainings,
* tutorials on performing different types of trainings (:doc:`incremental learning </howtos/develop/incremental-learning>`, :doc:`distributed learning </howtos/develop/distributed-learning>`)
* the ability to :doc:`use GPUs </howtos/train/standard>` to accelerate your development,
* the possibility to :ref:`integrate your module with the API <deepaas-integrate>` to enable easier user interaction,
* solutions to deploy your developed model in :doc:`the Cloud </howtos/deploy/cloud>` or in your :doc:`local resources </howtos/try/locally>`,
* the ability to share your module with other users in the :ref:`Dashboard Marketplace <dashboard_marketplace>`.

.. admonition:: Related HowTo's
   :class: info

   * :doc:`How to develop a model </howtos/develop/index>`
