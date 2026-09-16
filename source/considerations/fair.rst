FAIR-by-design
==============

The **FAIR principles** (Findable, Accessible, Interoperable, and Reusable) were formulated to ensure that digital scientific assets can be discovered, accessed, integrated, and reused by both humans and automated systems. While FAIR originally focused primarily on research datasets, the rapid emergence of data-driven science has made applying FAIR to Machine Learning models, software, and computational workflows equally critical.

In modern AI research, scientists frequently face reproducibility and transparency challenges:

* **Opaque model lineages**: Training processes, exact hyperparameters, and environment dependencies are rarely documented systematically.
* **Metadata fragmentation**: Models are shared across disparate repositories with incomplete or incompatible metadata descriptions.
* **Vendor lock-in and closed platforms**: AI models are often tightly coupled to proprietary cloud ecosystems or proprietary APIs, hindering independent verification.
* **Isolated data and compute**: Connecting scientific datasets from open repositories to distributed compute infrastructure remains cumbersome.

The **AI4EOSC** platform and the **AI4OS** stack were architected from the ground up with a **FAIR-by-design** approach. By embedding standardized metadata schemas, non-intrusive end-to-end provenance tracking, open-source principles, and native scientific data integrations directly into the MLOps lifecycle, the platform ensures that every AI asset is transparent, traceable, and reusable across the European Open Science Cloud (EOSC) and the broader scientific community.


Standardized metadata and semantic discovery
--------------------------------------------

Rich and consistent metadata is essential to make AI modules easily findable and interoperable across scientific domains and external service catalogs.

* **Schema enforcement**: Every AI module registered in the platform catalog must provide a valid metadata description adhering to a defined JSON Schema.
* **Comprehensive descriptors**: The schema combines user-defined fields (such as title, summary, description, DOI, dataset citations, model weights, software libraries, and input data modalities) with automatically populated fields from external sources (e.g., license details and modification timestamps from GitHub).
* **Semantic linked data (MLDCAT-AP)**: The Platform API retrieves module metadata and serializes it into standard linked data formats (JSON-LD, RDF Turtle). It supports transformation into standard application profiles such as **MLDCAT-AP** (the Machine Learning DCAT Application Profile), enabling semantic search, catalog federation, and interoperability with external registries.

.. note::

    Learn more about how module metadata is structured and edited in the :doc:`AI modules metadata guide </reference/modules/metadata>`.


End-to-end provenance and reproducibility
-----------------------------------------

Provenance provides an immutable, transparent record of how an AI module was created, trained, tested, and packaged. AI4EOSC implements an automated, non-intrusive provenance capture system that gathers metadata across the entire workflow without requiring changes to existing user code or tools.

* **Non-intrusive multi-source harvesting**: When code changes are committed, the :doc:`CI/CD pipeline </reference/modules/cicd>` automatically collects provenance fragments from multiple components:

  * **Platform API & Metadata**: Author information, module descriptions, and referenced scientific datasets or DOIs.
  * **Nomad Orchestrator**: Compute resource specifications (CPU, GPU, memory allocations) and execution run metadata.
  * **MLflow**: Hyperparameters, training metrics, run artifacts, and experiment tracking logs.
  * **Jenkins CI/CD**: Build status, code quality checks, and container image checksums.
  * **Environmental footprint**: Real-time :doc:`carbon and energy metrics </considerations/footprint>` captured during training runs.

* **Semantic graph generation (W3C PROV-O)**: Heterogeneous JSON fragments from all sources are stored in a PostgreSQL database and transformed via declarative RDF Mapping Language (RML) rules (using CARML). The resulting linked graph complies with the **W3C PROV-O** ontology and aligns with emerging standards like **FAIR4ML**.
* **Interactive visualization & AI assistant**: Users can inspect the full provenance lineage directly in the Dashboard via an interactive visual graph explorer, or query the graph in natural language using the platform's integrated :doc:`LLM assistant </reference/llm>`.

.. image:: /_static/images/provenance/simple-graph.png
    :alt: Simplified provenance graph

.. note::

    Explore detailed examples and interactive graph features in the :doc:`AI module provenance guide </reference/modules/provenance>`.


Openness and avoiding vendor lock-in
------------------------------------

True accessibility in science requires open software, transparent artifacts, and independence from proprietary platforms.

* **Open-source software stack**: All core AI4OS platform components, orchestration tools, and deployment templates are open source and publicly maintained under the `AI4OS GitHub organization <https://github.com/ai4os>`__.
* **Open AI module catalog**: Every module developed on the platform has a public repository hosted under the `AI4OS Hub GitHub organization <https://github.com/ai4os-hub>`__. Code, model weights, training configurations, and documentation are publicly accessible and linkable.
* **Public container images**: Workloads and modules are packaged into standard Docker container images built reproducibly via CI/CD pipelines and published to public registries (`DockerHub <https://hub.docker.com/u/ai4oshub/>`__ and `Harbor <https://registry.cloud.ai4eosc.eu/>`__).
* **Infrastructure portability**: Workloads are not tied to a single infrastructure provider. Users can deploy modules to any external Docker-enabled environment (:doc:`try locally </howtos/try/locally>`), federated research clouds (:doc:`deploy on custom clouds via IM </howtos/deploy/cloud>`), on-premise servers, or the :doc:`EOSC EU Node </howtos/deploy/eosc-node>` using the Infrastructure Manager (IM) and TOSCA orchestration templates.


Interoperability and ecosystem integration
------------------------------------------

AI4EOSC is designed to adapt to existing research ecosystems rather than forcing communities into rigid, isolated silos:

* **Unified API abstraction**: Modules share a consistent interface powered by the :doc:`DEEPaaS API </advanced/api>`, exposing standard training, prediction, and configuration endpoints regardless of the underlying machine learning framework (PyTorch, TensorFlow, Scikit-learn, etc.).
* **External AI catalog connectors**: The platform can federate external model repositories. For example, a dedicated connector for the `BioImage Model Zoo <https://bioimage.io/>`__ maps external model metadata to enable :doc:`one-click deployments of external community models </howtos/deploy/external>` directly from the AI4EOSC dashboard.
* **Direct scientific repository integration**: Datasets can be linked and :ref:`synchronized at launch time <dashboard_storage>` from established FAIR data repositories (including `Zenodo <https://zenodo.org/>`__, `Data Europa <https://data.europa.eu/>`__, `Dryad <https://datadryad.org/>`__, and `SeaNoe <https://www.seanoe.org/>`__) by simply referencing their DOI or URL via `DataHugger <https://github.com/J535D165/datahugger>`__ integrations.
* **Storage interoperability**: Workloads can connect to any :doc:`RCLONE-compatible storage provider </advanced/rclone>` (such as Nextcloud, Amazon S3, Ceph, dCache, ownCloud, or Google Drive) with seamless credential injection.