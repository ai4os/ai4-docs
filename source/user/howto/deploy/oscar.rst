Deploy a model on the AI4OS Inference platform using the Dashboard
==================================================================

The Dashboard offers the possibility to deploy a model as serverless using the AI4OS Inference Platform (based on OSCAR).

.. list-table::
    :header-rows: 1

    * - ✅ Pros
      - ❌ Cons
    * - - You are not consuming resources when you are not using the model,
        - Deployments can auto-scale to fit peaks in user queries,
        - Zero configuration needed as the model is deployed in the AI4OS stack.
      - - Predictions can have some latency, due to the AI model being loaded at each prediction.

1. Choose your module and deploy
--------------------------------

The first step is to choose a module from the :doc:`Dashboard</user/overview/dashboard>`.
There you will be able to find all the modules ready to be used under the tag ``Inference``.

We will first start doing a simple prediction using the popular `YOLO module <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/ai4os-yolov8-torch>`__.

.. image:: /_static/images/dashboard/module-yolo.png

In the module page, click on the option ``Deploy > Inference API (serverless)``.
This will automatically deploy your OSCAR service with some predefined configuration.

.. admonition:: Module compatibility
   :class: warning

   * Inference endpoints only work form models that return a JSON response (most models).
   * Modules require a deepaas version higher than ``2.5.0`` to work with OSCAR inference endpoints.
     If the module does not have a supported DEEPaaS, you will be show a clear error message when trying to make an inference.
     We are actively working on improving compatibility with all modules.


2. Make a prediction
--------------------

.. admonition:: Response status codes
   :class: important

    If the call we make returns a 502 error, you should wait a bit more.
    You docker image is probably getting pulled!

    If the error persists, please contact support.

Synchronous predictions
^^^^^^^^^^^^^^^^^^^^^^^

In the ``Inference`` tab, go to the ``OSCAR`` table and find your newly created service. Copy the endpoint url and the secret token.

.. image:: /_static/images/dashboard/oscar-info.png
    :width: 400px

To make a prediction with that service, you first need to know what are the required inputs.
For this run the following command from your console:

.. code-block:: console

    $ curl --location '***endpoint***' \
           --header 'Content-Type: application/json' \
           --header 'Authorization: Bearer ***token***' \
           --data '{"help": ""}'

As a response, you will receive what are the input args you should pass to the module.

.. code-block::

    [...]

    options:
    -h, --help
            show this help message and exit
    --files FILES
            Input an image or Video.
            accepted image formats: .bmo, .dng, .jpg, .jpeg, .mpo, .png, .tif, .tiff, .pfm, and .webp.
            accepted video formats: .asf, .avi, .gif, .m4v, .mkv,.mov, .mp4, .mpeg, .mpg, .ts, .wmv, .webm
            Type: str (filepath)
            *Required*
    [...]

Now it's time to make a prediction call on a `bear image <https://upload.wikimedia.org/wikipedia/commons/9/9e/Ours_brun_parcanimalierpyrenees_1.jpg>`__.
All parameters should be passed inside a JSON payload.
If the model inputs needs a file, it should be passed encoded as base64 in the ``oscar-files`` field in the data.

.. code-block:: console

    # Create a JSON payload with the base64 data and save it to a temporary file
    JSON_PAYLOAD=$(cat <<EOF
    {
    "oscar-files": [
        {
        "key": "files",
        "file_format": "jpg",
        "data": "$(base64 /home/iheredia/bear.jpg | tr -d "\n")"
        }
    ]
    }
    EOF
    )

    # Save the JSON payload to a temporary file
    TEMP_JSON_FILE=$(mktemp)
    echo "$JSON_PAYLOAD" > "$TEMP_JSON_FILE"

    # Step 3: Use curl to send the request with the JSON payload from the temporary file
    curl --location ***endpoint***' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer ***token***' \
    --data @"$TEMP_JSON_FILE"

    # Clean up the temporary file
    rm "$TEMP_JSON_FILE"

The response will give you the JSON output of the model (classifier.

.. code-block:: console

    2024-09-30 12:09:19.502 29 INFO deepaas.cmd.cli [-] return: ['[\n  {\n    "name": "bear",\n    "class": 21,\n    "confidence": 0.93346,\n    "box": {\n      "x1": 109.39322,\n      "y1": 26.39718,\n      "x2": 627.42999,\n      "y2": 597.74689\n    }\n  }\n]']


3. Full example: AI4EOSC toy model
----------------------------------

In this second part, we are going to demonstrate how to send a more complete set of input parameters to OSCAR, now using Python instead of CURL.

For educational purposes, we are going to use the `official AI4EOSC demo module <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/deep-oc-demo_app>`__.
While this model does not perform an AI task, it is very helpful as it shows the wide variety of inputs that can be sent to OSCAR inference endoints.

So go back to the previous steps and deploy the
`ai4os-demo-app <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/ai4os-demo-app>`__.
Once you have retrieved your endpoint and token, you can run the following Python script to make the prediction from your local computer:

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
        msg = 'deepaas.cmd.cli [-] return:'
        if msg in line:
            out = line.split(msg)[-1].strip()
            out = ast.literal_eval(out)
            break

    # Check deepaas output matches input
    keys = list(data.keys())
    if 'oscar-files' in data.keys():
        keys.remove('oscar-files')
    for k in keys:
        if k in ['demo_dict', 'demo_list_of_floats']:
            data[k] = ast.literal_eval(data[k])
        if data[k] != out[k]:
            print(f'Failed to validate {k}: {data[k]} != {out[k]}')


.. tip::

    If your call returns a 502 error, you should wait a bit more.
    You docker image is probably getting pulled!

    If the error persists, please contact support.

.. admonition:: Advanced usage
   :class: info

   Do you want to manually deploy your OSCAR services for greater customization?
   Check how to :doc:`Manually deploy a serverless inference endpoint  </user/howto/deploy/oscar-manual>`
