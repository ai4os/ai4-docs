Federated server
================

Deploying a Federated server
----------------------------

The workflow for deploying a Federated server is similar to the one for
:doc:`deploying a module </user/overview/dashboard>`, so please refer that.

The main differences in the configuration are:

* ``Federated token``: is a token that you **must copy** and keep safe. You will
  distribute the token among the clients that will take part in the federated training,
  as a way to authenticate them and keep the training private and secure.

* ``Federated configuration`` section will let you choose how many rounds you will train,
  the minimum number of clients, the federated averaging methods, and the metric analyzed.

Federated learning training in AI4EOSC
--------------------------------------
Once your federated server is deployed, you have to:

1. (Recomended) When starting the deployment of the federated learning server, use JupyterLab or VisualStudio Code as service to run if you want to monitor the process. Execute:

  .. code-block:: console

       python3 -m fedsever.server

If you want to change any parameters in the federated configuration, you can always modify ``fedserver/server.py``.

   *(Optional)*: if you deploy it using ``fedserver`` the federated learning server will be started automatically, but you will not be able to monitor the process (e.g. if there is a failure, how the clients are connected or if any of them is disconnected).


2. Once you server is running, find the ``fedserver`` deployment ID or the endpoint, located
   in the ``Info`` in the deployments table.
   Share the deployment ID or the endpoint and the token with the clients that will take part in the training.
   They will then add that information in their code to be able to connect with the server.
   We provide `some examples of client implementations <https://github.com/deephdc/federated-server/tree/main/fedserver/examples>`__
   to serve as reference.

.. note::
    For more information, see the *Getting Started* step by step guide available in the `federated server repository <https://github.com/deephdc/federated-server>`__. 

    Also, you can check the tutorial on the use of `Federated Learning within the AI4EOSC Platform <https://youtu.be/FrgVummLNbU>`__.

