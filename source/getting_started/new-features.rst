⭐ New features
===============

Here is a quick summary of the major updates in the platform that are relevant for
users. Minor updates to the documentation will still be performed continuously but not
notified here.

``📘 docs, 📈 dashboard, 📌 others``

.. Template
.. * 📘 new :doc:`... </user/...>` page (``2024-04-03``)

* 📈 support the ability of :ref:`making snapshots of deployments <dashboard_snapshots>` (``2024-11-26``)
* 📈 enable Gradio UI for inference on :ref:`AI4OS dedicated resources <nomad-gradio>` (``2024-11-26``)
* 📈 added support to :doc:`label images with CVAT </howtos/train/cvat>` (``2024-11-14``)
* 📈 add support for `Seanoe <https://www.seanoe.org/>`__ and `Data Europa <https://data.europa.eu/>`__ datasets :ref:`downloading <dashboard_storage>` (``2024-10-18``)
* 📈 redesign of the Dashboard Marketplace, with :ref:`new filtering features <dashboard_marketplace>` (``2024-10-18``)
* 📈 redesign of the Dashboard module pages, following the new metadata schema (``2024-10-18``)
* 📈 we send notifications to users when deployments take long to deploy (``2024-10-11``)
* 📌 we started supporting the `AI4Life project <https://ai4life.eurobioimaging.eu/>`__ (``2024-10-07``)
* 📈 new ability :doc:`deploy OSCAR services </howtos/deploy/oscar>` from the Dashboard (``2024-09-25``)
* 📈 redesign the Dashboard+Docs around the main user workflows: Try, Develop, Deploy (``2024-09-20``)
* 📈 new :ref:`Profile section <dashboard_profile>` where you can link your storage providers (``2024-09-04``)
* 📈 new :doc:`try-me deployments </howtos/try/dashboard-gradio>` (``2024-09-03``)
* 📌 new federated cluster is available in production (``2024-08-05``)
* 📈 new :ref:`external datasets download <dashboard_storage>` feature (``2024-06-30``)
* 📘 new guides to perform :doc:`Incremental Learning </howtos/develop/incremental-learning>` (``2024-06-20``)
* 📈 new :ref:`stats section <dashboard_statistics>` in the Dashboard (``2024-05-14``)
* 📘 support for token authentication in :doc:`Federated Learning trainings </howtos/train/federated-server>` (``2024-04-16``)
* 📘 new :doc:`New features  <new-features>` page (meta!) (``2024-04-03``)
* 📘 new tutorials for creating AI Inference pipelines  (:doc:`Elyra </howtos/pipelines/elyra>`, :doc:`Flowfuse </howtos/pipelines/flowfuse>`) (``2024-03-18``)
* 📘 new :doc:`MLflow </howtos/develop/mlflow>` tutorials (``2024-02-09``)
* 📘 new :doc:`Frequently Asked Questions (FAQ) </help/faq>` page (``2024-02-05``)
* 📌 :doc:`MLflow </howtos/develop/mlflow>` available under new domain (``2024-01-29``)
* 📈 we enforce a quota of 2 GPUs per user for better resource distribution (``2024-01-25``)
* 📘 updated :doc:`Quickstart </getting_started/quickstart>` page (``2024-01-24``)
* 📈 users are able to select specific GPU models (``2024-01-18``)
* 📌 new :doc:`Nextcloud </reference/storage>` storage available (``2024-01-15``)


🚀 Upcoming features
--------------------

In this section, we will offer some insight on to where the AI4OS stack is heading.

First, the are a number of mature features that are in the process of being integrated
in the stack:

* 📈 try model endpoints with OSCAR
* 📈 new tool for image annotation (CVAT)
* 📈 new tool for efficient video streaming (Kafka)
* 📈 support for federated learning with NVflare

Along with these upcoming features, we are exploring more improvements. These are
in an experimental status and might not finally get integrated in the stack.

* 📈 carbon footprint estimator for your deployments
* 📈 graph visualizations of your module/deployment metadata
* 📈 ability to snapshot deployments
* 📈 ability to launch trainings in batch
* 📈 new popularity metrics

Do you find something missing? Please check
:ref:`how to suggest a new feature <new-features-request>`.
