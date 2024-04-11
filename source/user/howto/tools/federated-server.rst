Federated server
================

Deploying a Federated server
----------------------------

The workflow for deploying a Federated server is similar to the one for
:doc:`deploying a module </user/overview/dashboard>`, so please refer that.

The main difference in the configuration is the last step:

* ``Federated configuration`` section will let you choose how many rounds you will train,
  the minimum number of clients, the federated aggregation methods and the metric(s) analyzed.

Federated learning training in AI4EOSC
--------------------------------------
Once your federated server is deployed, you have to:

1. (Recomended) When starting the deployment of the federated learning server, use JupyterLab or VisualStudio Code as service to run if you want to monitor the process. Execute:

   .. code-block:: console

       cd federated-server/fedserver
       python3 server.py

   If you want to change any parameters in the federated configuration, you can always modify ``fedserver/server.py``.

   *(Optional)*: if you deploy it using ``fedserver`` the federated learning server will be started automatically, but you will not be able to monitor the process (e.g. if there is a failure, how the clients are connected or if any of them is disconnected).


2. Once you server is running, find the ``fedserver`` deployment ID or the endpoint, located
   in the ``Info`` in the deployments table.
   Share the deployment ID or the endpoint and the token with the clients that will take part in the training.
   They will then add that information in their code to be able to connect with the server.
   We provide `some examples of client implementations <https://github.com/deephdc/federated-server/tree/main/fedserver/examples>`__
   to serve as reference.


Client-server authentication
----------------------------
AIOS provide users with a secret management system that can be used for authenticating theimplementationimplementation clients prior to their incorporation into the federated training through the use of tokens.
You can generate as many federated secrets (tokens) for authenticating the clients with the server as needed (label them so that you can revoke them if necessary):

.. image:: /_static/images/test-secrets.png
   :width: 500 px

From the client side: 

  .. code-block:: python

      import flwr as fl
      from pathlib import Path
      import certifi
      import ai4flwr.auth.bearer

      # Read the data, create the model
      # (...)

      # Create the class Client(), example of Flower client:
      class Client1(fl.client.NumPyClient):
          def get_parameters(self, config):
              return model.get_weights()
      
          def fit(self, parameters, config):
              model.set_weights(parameters)
              model.fit(x_train, y_train, epochs=5, batch_size=16)
              return model.get_weights(), len(x_train), {}
      
          def evaluate(self, parameters, config):
              model.set_weights(parameters)
              loss, accuracy = model.evaluate(x_test, y_test)
              return loss, len(x_test), {"accuracy": accuracy}

        
      token = "12345" # Token generated in the dashboard
      auth_plugin = ai4flwr.auth.bearer.BearerTokenAuthPlugin(token)
      
      # Start -> connecting with the server
      uuid = '...' # Fill with the UUID of the deployment of the FL server
      end_point = f"fedserver-{uuid}.deployments.cloud.ai4eosc.eu"
      fl.client.start_client(
          server_address=f"{end_point}:443", 
          client=Client1(),
          root_certificates=Path(certifi.where()).read_bytes(),
          call_credentials=auth_plugin.call_credentials()
      )


.. note::
    For more information, see the *Getting Started* step by step guide available in the `federated server repository <https://github.com/deephdc/federated-server>`__.

    Also, you can check the tutorial on the use of `Federated Learning within the AI4EOSC Platform <https://youtu.be/FrgVummLNbU>`__.
