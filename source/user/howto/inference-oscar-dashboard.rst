Inference with OSCAR
====================

.. When this is ready, add to the index and move other OSCAR docs to technical
.. documentation

OSCAR is the serverless platform we use use in the project.
More info on OSCAR can be found in the :doc:`OSCAR technical documentation </technical/howto-developers/oscar>`.


1. Choose your module and deploy
--------------------------------

The first step is to choose a module from the :doc:`Dashboard</user/overview/dashboard>`.
There you will be able to find all the modules ready to be used under the tag ``Inference``.

For educational purposes we are going to use the `demo application <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/deep-oc-demo_app>`__.
This will allow us to see the general workflow.

In the module page, click on the option ``Deploy with OSCAR``.
This will automatically deploy your OSCAR service with some predefined configuration.


2. Run a prediction
-------------------

In the ``Deployments`` tab, go to the ``OSCAR services`` table and find your newly
selected service.

Copy the endpoint url and the secret token. To make a prediction with that service,
you first need to know what are the required inputs.

So run the following command form your console:

.. code-block:: console

    $ curl --location '***endpoint***' \
           --header 'Content-Type: application/json' \
           --header 'Authorization: Bearer ***token***' \
           --data '{"help": ""}'

The response will give you what are the input args you should pass to the module.

.. code-block::

    [...]
    optional arguments:
      -h, --help
              show this help message and exit
      --demo_str DEMO_STR
      --demo_str_choice DEMO_STR_CHOICE
              demo description
              Choices: ['choice1', 'choice2']
      --demo_int DEMO_INT
      --demo_int_range DEMO_INT_RANGE
      --demo_float DEMO_FLOAT
      --demo_bool DEMO_BOOL
      --demo_dict DEMO_DICT
      --demo_list_of_floats DEMO_LIST_OF_FLOATS
      --demo_image DEMO_IMAGE
              image
              Type: FILEPATH
      --demo_audio DEMO_AUDIO
              audio
              Type: FILEPATH
      --demo_video DEMO_VIDEO
              video
              Type: FILEPATH

Now it's time to make a prediction call.

All parameters should be passed inside the data dictionary.
If the model needs a file, it should be passed encoded as base64 in the ``oscar-files``
field in the data. This can be achieved in using the ``base64`` command in Linux.

.. code-block:: console

    $ curl --location '***endpoint***' \
           --header 'Content-Type: application/json' \
           --header 'Authorization: Bearer ***token***' \
           --data '{ \
             "demo_str": "my demo string", \
             "oscar-files": { \
               "demo_image": "$(base64 ***/path/to/image***)", \
               } \
             }'

The response will give you the JSON output of the model.

.. tip::

    Do you want to manually deploy your OSCAR services for greater customization?
    Check out the :doc:`OSCAR technical documentation </technical/howto-developers/oscar>`.
