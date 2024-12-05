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
Under the ``Platform Categories`` tag section, select any module that has the tag ``AI4 Inference``.

In this tutorial, we will demonstrate a simple prediction using the popular `YOLO module <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/ai4os-yolov8-torch>`__.

.. image:: /_static/images/dashboard/module-yolo.png

In the module page, click on the option ``Deploy > Inference API (serverless)``.
This will automatically deploy your OSCAR service with some predefined configuration.

.. admonition:: Module compatibility
   :class: warning

   * Inference endpoints only work for models that return a JSON response (that is the case for most models).
   * Modules require a DEEPaaS version higher than ``2.5.0`` to work with OSCAR inference endpoints.
     If the module does not have a supported DEEPaaS, you will be show a clear error message when trying to make an inference.


2. Make a prediction
--------------------

In the ``Inference`` tab, go to the ``Serverless (OSCAR)`` table and find your newly created service.

.. image:: /_static/images/dashboard/oscar-table.png

Click on :material-outlined:`info;1.5em` ``Info`` fo your service and you will find all the variables you need for making a prediction:

* **for synchronous calls**: the ``endpoint`` url and the secret ``token`` you need for authentication.

.. image:: /_static/images/dashboard/oscar-info.png
    :width: 400px


Finding what are your model inputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To make a prediction with that service, you first need to know what are the required inputs.
For this run the following Python script to make a synchronous call asking for help:


.. code-block:: python

    import base64

    import requests


    url = "https://inference.cloud.ai4eosc.eu/run/ai4papi-****************************"
    token = "*************************************************************************"

    data = {"help": ""}
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }
    r = requests.post(url=url, headers=headers, json=data)

    if r.status_code == 401:
        raise Exception("Invalid token.")
    if not r.ok:
        raise Exception(f"Some error has occurred: {r}")

    print(r.text)

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


.. admonition:: Response status codes
   :class: important

   If the call returns a ``502`` error, you should wait a bit more, your docker image is probably getting pulled!

   If the error persists, please contact support.

Synchronous predictions
^^^^^^^^^^^^^^^^^^^^^^^

Now that we now what are the inputs the model needs, it's time to make a prediction call on a `bear image <https://upload.wikimedia.org/wikipedia/commons/9/9e/Ours_brun_parcanimalierpyrenees_1.jpg>`__.
All parameters should be passed inside a JSON payload.
If the model inputs needs a file, it should be passed encoded as base64 in the ``oscar-files`` field in the data.

.. code-block:: python

    import base64

    import requests


    url = "https://inference.cloud.ai4eosc.eu/run/ai4papi-****************************"
    token = "*************************************************************************"

    def get_base64(fpath):
        with open(fpath, "rb") as f:
            encoded_str = base64.b64encode(f.read()).decode("utf-8")
        return encoded_str

    data = {
        "oscar-files": [
            {
                "key": "files",
                "file_format": "jpg",
                "data": get_base64("./bear.jpg"),
            },
        ]
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }
    r = requests.post(url=url, headers=headers, json=data)

    if r.status_code == 401:
        raise Exception("Invalid token.")
    if not r.ok:
        raise Exception(f"Some error has occurred: {r}")

    print(r.text)

The script will print the logs, along with the JSON output of the model.

.. code-block:: console

    [...]
    2024-09-30 12:09:19.502 29 INFO deepaas.cmd.cli [-] return: ['[\n  {\n    "name": "bear",\n    "class": 21,\n    "confidence": 0.93346,\n    "box": {\n      "x1": 109.39322,\n      "y1": 26.39718,\n      "x2": 627.42999,\n      "y2": 597.74689\n    }\n  }\n]']
    [...]

3. More
-------

Make a prediction using Bash
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
For completeness sake, we provide the equivalent commands to perform the above operations in Bash, instead of Python.

.. dropdown:: ㅤㅤ Synchronous call with YOLO (Bash)

    Find the input parameters needed by the model:

    .. code-block:: console

        $ curl --location '***endpoint***' \
            --header 'Content-Type: application/json' \
            --header 'Authorization: Bearer ***token***' \
            --data '{"help": ""}'

    Make a synchronous call with an image input:

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


Learn how to feed different input types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We are going to demonstrate how to send a more complete set of input parameters to OSCAR.

For educational purposes, we are going to use the `official AI4EOSC demo module <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/deep-oc-demo_app>`__.
While this model does not perform an AI task, it is very helpful as it shows the wide variety of inputs that can be sent to OSCAR inference endpoints.

So go back to the previous steps and deploy the
`ai4os-demo-app <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/ai4os-demo-app>`__.
Once you have retrieved your endpoint and token, you can run the following Python script to make the prediction from your local computer:


.. dropdown:: ㅤㅤ Synchronous call with the demo app (Python)


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

        print(out)


Additional customizations
^^^^^^^^^^^^^^^^^^^^^^^^^

Do you want to manually deploy your OSCAR services for greater customization?
Check how to :doc:`Manually deploy a serverless inference endpoint  </user/howto/deploy/oscar-manual>`
