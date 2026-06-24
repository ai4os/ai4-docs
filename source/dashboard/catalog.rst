.. _dashboard_marketplace:

Catalog
=======

The AI4EOSC catalog gathers the different types of AI assets that the platform currently offers.

AI Modules
----------

The AI Modules catalog is a set of AI models designed to perform given AI tasks (eg. image classification).
The catalog shows both models developed specifically for the platform, as well as :doc:`external model catalogs </howtos/deploy/external>` that have been integrated to make them deployable in the platform.

.. image:: /_static/images/dashboard/marketplace.png

You can use filters to quickly find the module you want.
We provide filtering by:

* ``Libraries``: this is the Deep Learning the module uses (eg. Pytorch, Tensorflow)
* ``Tasks``: this is the broad task the module addresses (eg. Computer Vision, Natural Language Processing)
* ``Platform Categories``: platform-specific tags.
  Current options include:

  - ``AI4 pretrained``: modules that already come with a trained AI model
  - ``AI4 inference``: modules that can be used for inference (usually overlaps with *AI4 pretrained*)
  - ``AI4 trainable``: modules that can be trained on a new dataset

  For example the `image classifier <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/ai4os-image-classification-tf>`__ is both pretrained (because is comes with a model trained on ImageNet), inference-ready (because it allows to use that model to do predictions) and trainable (because it allows to retrain that model on a different dataset, to create for example a `plant classifier <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/plants-classification>`__ )

* ``Data type``: type of data the module processes (eg. Image, Audio)
* ``Tags``: any module-specific tag

Tools
-----

The Tools catalog is a collection of tools that come handy in assisting users during the whole Machine Learning workflow cycle.

.. todo: add image

We currently offer for example:

- The **Development Environment** to develop new modules (:doc:`Develop a model from scratch </howtos/develop/dashboard>`)
- Several **Federated Learning Servers** to make federated privacy-friendly trainings (:doc:`Flower </howtos/train/federated-flower>`, :doc:`NVFLARE </howtos/train/federated-nvflare>`)
- The **Computer Vision Annotation Tool** (CVAT) to label images (:doc:`Labeling images with CVAT </howtos/train/cvat>`)

LLMs
----

The LLM catalog is a collection of LLM models that users can leverage for generative tasks.

.. todo: add image

There are currently two kinds of LLMs:

* **Platform-wise LLMs**: those are LLMs that are permanently deployed for all platform users.
  For more information on how to use them, please refer to :doc:`AI4EOSC LLM documentation </reference/llm>`.
* **Self-deployable LLM**: those are LLMs that are deployable per user.
  The catalog has multiple open-source models from a wide range of AI-relevant actors (Qwen, DeepSeek, Meta).
  For more information on how to use them, please refer to the tutorial: :doc:`Deploy your own LLM chatbot </howtos/deploy/llm>`.
