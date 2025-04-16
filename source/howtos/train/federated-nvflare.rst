Federated Learning with NVFLARE
===============================

.. admonition:: Requirements
   :class: info

   🔒 This tutorial requires :ref:`full authentication <getting-started/register:Full authentication>`.





Deploying a Federated server
----------------------------

The workflow for deploying a FL server is similar to the one for
:doc:`deploying a module </reference/dashboard>`.

In this particular case, you will need to pay attention to:

* Your credentials to access the NVFLARE Dashboard and associated Jupyter notebook.

* Whether to make the project public or restrict the training to authorized trusted partners.

* The Docker image that the client need to use to connect to the server.

* The start and end dates of the training

  .. image:: /_static/images/dashboard/configure_nvflare.png

Federated learning training in AI4EOSC
--------------------------------------

In the :ref:`deployments list <dashboard-manage-deployments>` you will be able to see your newly created NVFLARE instance.
Clicking the ``Quick access`` button, you will directly enter the NVFLARE Dashboard.
Enter your credentials from the configuration and voilá, you're in!

.. image:: /_static/images/endpoints/nvflare-dashboard.png

For more information on running a training, please follow the official `NVFLARE documentation <https://nvflare.readthedocs.io/en/main/index.html>`__.

We will soon add a simple example for reference! 🚀