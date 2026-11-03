Train using Federated Learning
==============================

The platform allows you to deploy servers to orchestrate Federated Learning trainings.
We currently support the two main Federated Learning frameworks:

* :doc:`Flower </howtos/train/federated-flower>`: due to its simpler configuration, this is the **recommended** option for beginners.
* :doc:`NVFLARE </howtos/train/federated-nvflare>`: for people who want a more fine-grained control of the training using a Dashboard UI.

Clients connect to those server to perform training on their local data.
Clients can be deployed either in the platform (as a standard `Development Environment <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/ai4os-dev-env>`__) or on external infrastructures.
See the tutorials on each Federated Learning framework to see how to configure the clients:

.. grid:: 2
	:gutter: 2

	.. grid-item-card:: :material-outlined:`hub;1.5em` Flower tutorial
		:link: federated-flower
		:link-type: doc

		Learn how to configure clients and train with the Flower framework.

	.. grid-item-card:: :material-outlined:`hub;1.5em` NVFLARE tutorial
		:link: federated-nvflare
		:link-type: doc

		Learn how to configure clients and train with the NVFLARE framework.

.. todo: create a nice diagram to illustrate the FL architecture
