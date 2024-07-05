Inference with OSCAR
====================

OSCAR is the serverless platform we use use in the project to perform inference.


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

.. admonition:: Caveats

   * Inference endpoints only work form models that return a JSON response.
   * Modules with a deepaas version lower than ``2.3.1`` won't likely work.

   Do you want to manually deploy your OSCAR services for greater customization?
   Check out the :doc:`OSCAR technical documentation </user/howto/inference-oscar>`


3. Full example: AI4EOSC toy model
----------------------------------

While this model does not perform an AI task, it is very helpful in order to see how
module parameters have to be formatted in the call.

So go back to the previous steps and deploy the
`ai4os-demo-app <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/ai4os-demo-app>`__.
Once you have retrieved your endpoint and token, you can run the following Python script
to make the prediction from your local computer:

.. code-block:: python

    import ast
    import base64

    import requests


    token = '*************************'
    url = '***************************'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}',
    }

    def get_base64(fpath):
        with open(fpath, "rb") as f:
            encoded_str = base64.b64encode(f.read()).decode('utf-8')
        return encoded_str

    data = {
        'demo_str': 'hi there!!!!',
        'demo_str_choice': 'choice1',
        'demo_int': -3,
        'demo_int_range': 42,
        'demo_float': -0.9,
        'demo_bool': False,
        'demo_dict': '{"c": "d"}',
        'demo_list_of_floats': "[1.2, -1.8]",
        'oscar-files': [
            {
                'key': 'demo_image',
                'file_format': 'png',
                'data': get_base64('./sample-image.png'),
            },
            {
                'key': 'demo_audio',
                'file_format': 'wav',
                'data': get_base64('./sample-audio.wav'),
            },
            {
                'key': 'demo_video',
                'file_format': 'mp4',
                'data': get_base64('./sample-video.mp4'),
            },
        ]
    }
    # data = {'help': ''}

    r = requests.post(url=url, headers=headers, json=data)
    out = r.text

    if r.status_code == 401:
        raise Exception('Invalid token.')

    # Save OSCAR output
    with open("./output-oscar.txt", "w") as f:
        f.write(out)

    ####################################################################################
    # As the demo-app is a dummy model that returns the same inputs it has been fed    #
    # with, we can load the OSCAR output to check it matches with our input            #
    ####################################################################################

    # Load OSCAR output
    with open("./output-oscar.txt", "r") as f:
        out = f.read()

    # Stop if error message detected
    error_msgs = [
        'deepaas-cli: error',
        'deepaas-cli predict: error',
        'ERROR deepaas-cli',
        'Traceback ',
    ]
    if any([e in out for e in error_msgs]):
        print(out)
        raise Exception()

    # Find was is the line of deepaas output (startswith "{") and only keep that
    for line in out.split('\n')[::-1]:
        if line.startswith('{'):
            out = ast.literal_eval(line)

    # Check deepaas output matches input
    keys = list(data.keys())
    if 'oscar-files' in data.keys():
        keys.remove('oscar-files')
    for k in keys:
        if k in ['demo_dict', 'demo_list_of_floats']:
            data[k] = ast.literal_eval(data[k])
        if data[k] != out[k]:
            print(f'Failed to validate {k}: {data[k]} != {out[k]}')
