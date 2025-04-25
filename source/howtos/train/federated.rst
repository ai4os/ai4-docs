Federated Learning in AI4OS
===========================

The AI4OS platform allows you to deploy servers to orchestrate Federated Learning trainings.
We currently support the two main Federated Learning frameworks:

* :doc:`Flower </howtos/train/federated-flower>`: due to its simpler configuration, this is the **recommended** option for beginners.
* :doc:`NVFLARE </howtos/train/federated-nvflare>`: for people who want a more fine-grained control of the training using a Dashboard UI.

Clients connect to those server to perform training on their local data.
Clients can be deployed either in the AI4OS platform (as a standard `AI4OS Development Environment <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/ai4os-dev-env>`__) or on external infrastructures.
See the tutorials on each Federated Learning framework to see how to configure the clients:

* :doc:`Flower tutorial </howtos/train/federated-flower>`
* :doc:`NVFLARE tutorial </howtos/train/federated-nvflare>`

.. todo: create a nice diagram to illustrate the FL architecture
