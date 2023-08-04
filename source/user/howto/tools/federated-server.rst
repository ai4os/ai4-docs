Federated server
================

Deploying a Federated server
----------------------------

The workflow for deploying a Federated server is similar to the one for
:doc:`deploying a module <../../overview/dashboard>`, so please refer that.

The main differences in the configuration are:

* ``Federated token``: is a token that you **must copy** and keep safe. You will
  distribute the token among the clients that will take part in the federated training,
  as a way to authenticate them and keep the training private and secure.

* ``Federated configuration`` section will let you choose how many rounds you will train,
  the federated averaging methods, etc.

Training with that server
-------------------------

Once your federated server is deployed, you have to:

1) *(Optional)*:
   If you deployed with Jupyterlab, you will need to open a terminal and start the server:

   .. code-block:: console

       python3 -m fedsever.server

   If you want to change any parameters in the federated configuration, you can always
   modify ``fedserver/server.py``.

2) Once you server is running, find the ``fedserver`` endpoint, located
   in the :fa:`circle-info` ``Info`` in the deployments table.
   Share the endpoint and the token with the clients that will take part in the training.
   They will then add that information in their code to be able to connect with the server.
   We provide `some examples of client implementations <https://github.com/deephdc/federated-server/tree/main/fedserver/client_samples>`__
   to serve as a reference.
