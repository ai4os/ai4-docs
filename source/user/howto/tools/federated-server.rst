Federated server
================

In this tutorial, we will guide on how to use the Federated Learning (FL) server in the AI4OS
platform to perform a FL training.

For more information, see the *Getting Started* step by step guide available in the
`federated server repository <https://github.com/deephdc/federated-server>`__, as well
as the tutorial on `using Federated Learning within the AI4OS Platform <https://youtu.be/FrgVummLNbU>`__.


Deploying a Federated server
----------------------------

The workflow for deploying a FL server is similar to the one for
:doc:`deploying a module </user/overview/dashboard>`.

When configuring the deployment of the FL server, we recommend selecting ``JupyterLab``
or ``VS Code`` as service to run if you want to monitor the process.
If you select ``fedserver``, the FL server will be started automatically,
but you will not be able to monitor the process (e.g. if there is a failure, how the
clients are connected or if any of them is disconnected).

.. admonition:: Note

    In the first configuration step you must select the docker tag. Note that the tag ``token`` will
    deploy the federated server including the authentication between the server and the clients (explained in the section *Client-server authentication*)


The last section (``Federated configuration``) section will let you choose specific
configuration for the FL training server like:

* how many rounds you will train,
* the minimum number of clients,
* the federated aggregation methods and the metric(s) analyzed,
* etc.


Federated learning training in AI4EOSC
--------------------------------------

Starting the Federated Learning server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Note

    This step is not needed if you configured the deployment to run with the ``fedserver`` option.

If you deployed with JupyterLab/VScode, open the IDE and start the fedserver process:

.. code-block:: console

    $ cd federated-server/fedserver
    $ python3 server.py

If you want to change any parameters in the federated configuration, you can
always modify ``fedserver/server.py``.

Retrieve the configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^

Now that your fedserver is running, you need to do the following steps:

1. **Find the endpoint where your server is deployed:**

   Once your FL server is running, go back to the Dashboard, find your deployment,
   click on :fa:`circle-info` ``Info`` and copy the URL of ``fedserver`` endpoint.

2. **In case you deployed it using the docker tag tokens, generate new secrets (if you need more that one) and distribute them to the clients:**

   AI4OS provides users with a token-based system that can be used for authenticating
   the clients prior to their incorporation into the federated training.

   To access the secret token, find your deployments and click the :fa:`key` icon.
   You can generate as many tokens as needed (eg. 1 token per client), as well as
   revoke them:

   .. image:: /_static/images/test-secrets.png
     :width: 500 px


You will need to share the endpoint and the appropriate token with the clients that
will take part in the training.
In the section below we will explain how the clients can use them to connect to the
training.

Client-server authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the AI4OS project, we use an `adapted version of the flwr library <https://github.com/AI4EOSC/flower>`__ to perform FL trainings.

In the code below, we provide an example on how to integrate the previously obtained
token and endpoint into the client code.
More examples are `available here <https://github.com/deephdc/federated-server/tree/main/fedserver/examples>`__.

.. code-block:: python

    import flwr as fl
    from pathlib import Path
    import certifi
    import ai4flwr.auth.bearer

    # Read the data, create the model
    # (...)

    # Create the class Client(), example of Flower client:
    class Client(fl.client.NumPyClient):
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


    token = "*********************" # INCLUDE THE TOKEN GENERATED IN THE DASHBOARD 
    auth_plugin = ai4flwr.auth.bearer.BearerTokenAuthPlugin(token)

    # Start -> connecting with the server
    endpoint = "*********************"  # FILL IN WITH THE ENDPOINT (dashboard)
    fl.client.start_client(
        server_address=f"{endpoint}:443",
        client=Client(),
        root_certificates=Path(certifi.where()).read_bytes(),
        call_credentials=auth_plugin.call_credentials()
    )
