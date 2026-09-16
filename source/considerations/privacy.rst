Privacy and data sovereignty
============================

Data privacy, security, and digital sovereignty have been foundational principles in the design of the AI4EOSC platform. Modern research workflows often handle sensitive data—such as patient health records, personal identifiers, proprietary datasets, or confidential scientific findings—that cannot be shared publicly or transferred outside institutional boundaries.

The platform provides a secure environment aligned with European data protection standards (GDPR), enabling researchers to run advanced machine learning, distributed training, and Generative AI workflows while maintaining strict control over their data.

.. note::

    For official legal notices and terms, please consult our `Privacy Policy <https://ai4eosc.eu/privacy-policy/>`__.


Collaborate without data sharing
--------------------------------

A common challenge in modern machine learning is the trade-off between privacy and model accuracy: training state-of-the-art models often requires aggregating diverse datasets from multiple institutions, but regulatory or ethical constraints prohibit centralizing raw data.

To overcome this, AI4EOSC provides first-class support for **Federated Learning (FL)**:

* **Data remains local**: Raw data never leaves client premises or institutional firewalls. Only model updates (weights or gradients) are communicated with the central orchestrator.
* **Standard framework support**: The platform offers preconfigured, ready-to-deploy federated servers for both :doc:`Flower </howtos/train/federated-flower>` (recommended for quick and flexible setups) and :doc:`NVFLARE </howtos/train/federated-nvflare>` (recommended for fine-grained control and management via a Dashboard UI).
* **Differential privacy (DP)**: To defend against model inversion or membership inference attacks, server-side :ref:`differential privacy <howtos/train/federated-flower:Server side differential privacy>` introduces calibrated Gaussian noise and fixed clipping norms during the global aggregation step.
* **Metric privacy (d-privacy)**: For domains with measurable distances between datasets, :ref:`metric privacy <howtos/train/federated-flower:Server side metric privacy>` calibrates perturbation dynamically based on the distance between client model updates, providing a superior trade-off between privacy guarantees and model utility.


Bring your own resources and data locality
------------------------------------------

When organizational policies or compliance rules strictly require data to stay on-premise:

* **Federated compute integration**: External compute nodes and on-premise hardware can be federated into our Nomad orchestrator, allowing users to run containerized workloads directly where their data is stored.
* **Hybrid FL deployments**: Clients participating in federated trainings can run entirely on external or local institutional hardware while connecting securely to the platform-hosted aggregation server using TLS certificates and token-based authentication.
* **Direct storage mounts**: Workloads can mount local or institutional storage providers directly, avoiding unnecessary data replication to external cloud environments.


Privacy in Generative AI workflows
----------------------------------

Mainstream commercial GenAI providers frequently raise privacy and IP concerns, including using user-submitted prompts, confidential documents, or code to train future commercial foundation models.

AI4EOSC eliminates these risks by adopting a **privacy-first architecture** for Generative AI:

* **Sovereign, self-hosted models**: All LLM services (accessible via the :doc:`AI4EOSC LLM chatbot </reference/llm>` or as :doc:`self-deployed LLM instances </howtos/deploy/llm>`) are hosted exclusively on European research infrastructure. Prompts and conversations are never transmitted to third-party commercial providers.
* **Zero model training on user data**: User prompts, uploaded documents, conversation histories, and knowledge bases are strictly never used to train or fine-tune models.
* **User-controlled data retention**: Chat sessions and knowledge bases remain under complete user control. When you delete a chat or a knowledge base, all associated data is permanently wiped from the platform.


Security, access control, and isolation
---------------------------------------

To accommodate a multi-tenant, multi-institution, and pan-European research community, the platform implements a layered security model:

* **Federated authentication & RBAC**: Identity management is centralized through a dedicated Keycloak instance using OpenID Connect (OIDC), acting as a trusted broker with external academic identity providers (such as EGI Check-In and eduGAIN / MyAccessID). Aligned with the AARC Blueprint Architecture, this reduces the trust boundary to a single managed service. Access control is enforced through Role-Based Access Control (RBAC) with tiered :doc:`user access levels </reference/user-access-levels>`.
* **Zero-plaintext secret management**: Sensitive credentials—such as storage synchronization tokens or federated learning join tokens—are secured and dynamically injected into workloads using HashiCorp Vault. Users can define secret lifetimes, generate scoped tokens, and revoke them instantly via the Dashboard or API to isolate compromised credentials or prevent malicious participation.
* **Password-protected deployments & endpoints**: Interactive user workloads (such as JupyterLab, VS Code, or FastAPI interfaces) are exposed behind mandatory password or token authentication configured by the user at launch time, ensuring unauthorized parties cannot access running environments or data.
* **Organizational & workload isolation**: Compute resources and service catalogs are partitioned at the institutional level using Nomad namespaces (supporting separate projects such as iMagine or AI4EOSC). At the workload level, user deployments run in isolated network namespaces, preventing cross-tenant visibility or interference while restricting inter-deployment traffic strictly to authenticated endpoints.