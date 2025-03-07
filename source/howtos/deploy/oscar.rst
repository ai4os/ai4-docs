Deploy a model on the AI4OS Inference platform using the Dashboard
==================================================================

.. admonition:: Requirements
   :class: info

   🔒 This tutorial requires :ref:`full authentication <getting-started/register:Full authentication>`.

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

The first step is to choose a module from the :doc:`Dashboard</reference/dashboard>`.
Under the ``Platform Categories`` tag section, select any module that has the tag ``AI4 Inference``.

In this tutorial, we will demonstrate a simple prediction using the popular `YOLO module <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/ai4os-yolov8-torch>`__.

.. image:: /_static/images/dashboard/module-yolo.png

In the module page, click on the option ``Deploy > Inference API (serverless)``.
This will automatically deploy your OSCAR service with some predefined configuration.

.. admonition:: Module compatibility
   :class: warning

   * Inference endpoints only work for models that return a JSON response (that is the case for most models).
   * Modules require a DEEPaaS version higher than ``2.5.0`` to work with OSCAR inference endpoints (that is the case for most models).
     If the module does not have a supported DEEPaaS, it will return a clear error message when trying to make an inference.


2. Make a prediction
--------------------

Retrieve the service information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the ``Inference`` tab, go to the ``Serverless (OSCAR)`` table and find your newly created service.

.. image:: /_static/images/dashboard/oscar-table.png

Click on :material-outlined:`info;1.5em` ``Info`` fo your service and you will find all the variables you need for making a prediction:

* **for synchronous calls**: the ``endpoint`` you will query and the secret ``token`` you need for authentication.
* **for asynchronous calls**: all the variables related to the `MINIO storage <https://min.io/>`__ that handles your predictions.

.. image:: /_static/images/dashboard/oscar-info.png
    :width: 400px


.. TODO: update this image when the dashboard is updated


Finding the model inputs
^^^^^^^^^^^^^^^^^^^^^^^^

Before making a prediction with that service, you first need to know what are the required inputs the model needs.

The following Python script demonstrates how to make a *synchronous call* asking for help.
To use the script, you have to replace the ``endpoint`` and ``token`` variables with the values :ref:`retrieved above <howtos/deploy/oscar:Retrieve the service information>`.

.. code-block:: python

    import base64

    import requests


    endpoint = "https://inference.cloud.ai4eosc.eu/run/ai4papi-***********************"
    token = "*************************************************************************"

    data = {"help": ""}
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }
    r = requests.post(url=endpoint, headers=headers, json=data)

    if r.status_code == 401:
        raise Exception("Invalid token.")
    if not r.ok:
        raise Exception(f"Some error has occurred: {r}")

    print(r.text)

In this case, we receive what are the inputs needed by the YOLO model.

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

Now that we know the inputs needed, it's time to make a synchronous prediction call on a `bear image <https://upload.wikimedia.org/wikipedia/commons/9/9e/Ours_brun_parcanimalierpyrenees_1.jpg>`__ with the YOLO model service.

The following Python script demonstrates how to make a *synchronous call* with some model inputs. It is important to note that:

* All parameters for the model should be passed inside a JSON payload.
* If the model needs a file (as it is the case here), it should be passed encoded as base64 in the ``oscar-files`` field in the data.

As before, to use the script, you have to replace the ``endpoint`` and ``token`` variables with the values :ref:`retrieved above <howtos/deploy/oscar:Retrieve the service information>`.

.. code-block:: python

    import base64

    import requests


    endpoint = "https://inference.cloud.ai4eosc.eu/run/ai4papi-***********************"
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
    r = requests.post(url=endpoint, headers=headers, json=data)

    if r.status_code == 401:
        raise Exception("Invalid token.")
    if not r.ok:
        raise Exception(f"Some error has occurred: {r}")

    print(r.text)

The script will print the logs, along with the JSON output of the model (in this case, the prediction made by YOLO).

.. code-block:: console

    [...]
    2024-09-30 12:09:19.502 29 INFO deepaas.cmd.cli [-] return: ['[\n  {\n    "name": "bear",\n    "class": 21,\n    "confidence": 0.93346,\n    "box": {\n      "x1": 109.39322,\n      "y1": 26.39718,\n      "x2": 627.42999,\n      "y2": 597.74689\n    }\n  }\n]']
    [...]


Asynchronous predictions
^^^^^^^^^^^^^^^^^^^^^^^^

Finally, it is also possible to make asynchronous calls to the same service.

This approach is especially beneficial when:

* You have lots of data. This is because you upload all the data to the Minio bucket, and we will process that data in parallel. When the predictions are completed you can retrieve them from the bucket.

* You need to automatize the processing of the predictions. This is because with this approach we save separately the logs (in a ``.log`` file) and the predictions (in a ``.json`` file). If the prediction was not successful, you will only retrieve the log file.

The following Python script demonstrates how to upload some inputs to the bucket, list the contents of the bucket and download the outputs when the predictions are ready.

To use the script, you have to replace the Minio-related variables with the values :ref:`retrieved above <howtos/deploy/oscar:Retrieve the service information>`.

.. code-block:: python

    import base64
    import json
    import time

    import boto3


    # This information is retrieved from your deployment information window
    MINIO_BUCKET = "ai4papi-*************************************************"
    MINIO_URL = "https://****************************************************"
    MINIO_ACCESS_KEY = "**********************************************@egi.eu"
    MINIO_SECRET_KEY = "*****************************************************"

    # This is how you decide to name your new prediction
    prediction_ID = "test-prediction"

    # Local paths (in current folder)
    pth_local_input = f"input-{prediction_ID}.json"
    pth_local_output = f"output-{prediction_ID}.json"
    pth_local_logs = f"output-{prediction_ID}.log"

    # Remote paths (in the bucket)
    # Two files will be produced in the output folder of the bucket
    # * <input_filename>.json: this file has the output of the prediction, in JSON format.
    #   --> this will only be created if the prediction is successful
    # * <input_filename>.log: this file has the logs of the prediction.
    #   --> this will always be created
    pth_remote_input = f"inputs/{prediction_ID}.json"
    pth_remote_output = f"outputs/{prediction_ID}.json"
    pth_remote_logs = f"outputs/{prediction_ID}.log"

    # Prepare the data you want to predict
    def get_base64(fpath):
        """
        Encode files as base64. We need to do this to pass files as prediction inputs in
        the JSON file.
        """
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

    # Create the JSON file
    with open(pth_local_input, "w") as f:
        json.dump(data, f)

    # Init the Minio Object Store
    client = boto3.client(
        "s3",
        endpoint_url=MINIO_URL,
        region_name="",
        verify=True,
        aws_access_key_id=MINIO_ACCESS_KEY,
        aws_secret_access_key=MINIO_SECRET_KEY,
    )

    # Upload the inputs to the bucket
    with open(pth_local_input, "rb") as data:
        client.upload_fileobj(data, MINIO_BUCKET, pth_remote_input)
    print(f"Uploaded data to {pth_remote_input} in bucket {MINIO_BUCKET}")

    # Now we wait until the prediction is made
    while True:
        # List objects in the bucket
        r = client.list_objects_v2(Bucket=MINIO_BUCKET)
        contents = [i["Key"] for i in r["Contents"]]

        # If the output is available, download it
        if pth_remote_logs in contents:
            with open(pth_local_logs, "wb") as data:
                client.download_fileobj(MINIO_BUCKET, pth_remote_logs, data)
            print(f"Downloaded logs from {pth_remote_logs} in bucket {MINIO_BUCKET}")

            # Prediction JSON will only be available if the prediction was successful
            if pth_remote_output in contents:
                with open(pth_local_output, "wb") as data:
                    client.download_fileobj(MINIO_BUCKET, pth_remote_output, data)
                print(f"Downloaded data from {pth_remote_output} in bucket {MINIO_BUCKET}")

            break

        else:
            print("Waiting for the prediction to complete ...")
            time.sleep(5)


This script will produce a ``.log`` file with the OSCAR logs and a ``.json`` file with the prediction of the YOLO model.


3. More info
------------

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

4. How to use OSCAR UI
------------

Accessing the Service via the UI
--------------------------------

To access the OSCAR service through the UI, follow these steps:

1. From the **Deployments** section, locate your deployed model.
2. Click on :material-outlined:`info;1.5em` **More Info** to view the service details.
3. Copy the **Inference URL** and paste it into your browser to open the OSCAR UI.
4. Once the UI is open, you need to convert your input file into JSON format before making a request.

Preparing the Input JSON File
-----------------------------

Use the following Python script to convert your file into a compatible JSON format:

.. code-block:: python

    import base64
    import json

    def get_base64(fpath):
        """Encodes a file in Base64 format."""
        with open(fpath, "rb") as f:
            encoded_str = base64.b64encode(f.read()).decode("utf-8")
        return encoded_str

    # Prepare the JSON payload
    data = {
        "oscar-files": [
            {
                "key": "files",
                "file_format": "png",
                "data": get_base64("./inputs_Cat.png"),
            },
        ]
    }

    # Save the JSON data to a file
    with open("input2.json", "w") as f:
        json.dump(data, f, indent=4)

Once your file is ready, you can use it to invoke the service using either **synchronous** or **asynchronous** requests.


Additional customizations
^^^^^^^^^^^^^^^^^^^^^^^^^

Do you want to manually deploy your OSCAR services for greater customization?
Check how to :doc:`Manually deploy a serverless inference endpoint  </howtos/deploy/oscar-manual>`
