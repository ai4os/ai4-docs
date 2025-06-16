:orphan:

Manually deploy a serverless inference endpoint
===============================================

Scalable AI model inference is handled by the `AI4OS Inference <https://inference.cloud.ai4eosc.eu/>`__ platform, powered by the `OSCAR <https://oscar.grycap.net>`__ open-source serverless platform.

An OSCAR cluster consists of, among other components:

* a Kubernetes cluster than can optionally auto-scale, in terms of number of nodes,
  within a certain boundaries.
* configured with `MinIO <https://min.io>`__, a high-performance object storage system,
  so that file uploads to a MinIO bucket can trigger the invocation of an OSCAR service
  to perform AI model inference.
* configured with `Knative <http://knative.dev>`__, a FaaS platform, so that synchronous
  requests to an OSCAR service are handled via dynamically provisioned pods (containers)
  in the Kubenetes cluster.

The AI4OS Inference platform consists of a pre-deployed OSCAR cluster exclusively accessible for :doc:`fully authenticated users </reference/user-access-levels>`.

We have different OSCAR clusters depending on the project you belong to:

* AI4EOSC, AI4Life: https://inference.cloud.ai4eosc.eu
* iMagine: https://inference-walton.cloud.imagine-ai.eu

You can also launch services via the `command-line interface (CLI) <https://docs.oscar.grycap.net/oscar-cli/>`__.

.. warning::
  This cluster is provided for testing purposes and OSCAR services may be removed at
  any time depending on the underlying infrastructure capacity and usage rates.
  Should this happen, you can easily re-deploy the services from the corresponding FDL file.

1. Configuring an OSCAR service
-------------------------------

The cluster is used to deploy OSCAR services, which are described by a
`Functions Definition Language (FDL) <https://docs.oscar.grycap.net/fdl/>`__
file which specifies (among other features):

* The Docker image, which includes the AI model that supports the
  :doc:`DEEPaaS API </reference/api>` and all the required libraries and data to
  perform the inference.
* The computing requirements (CPUs, RAM, GPUs, etc.).
* The shell-script to be executed inside the container created out of the Docker image
  for each service invocation.
* (Optional) The link to a MinIO bucket and an input folder.

2. Invoking an OSCAR service
----------------------------

OSCAR services can be invoked (see `Invoking services <https://docs.oscar.grycap.net/invoking/>`__ for further details):

* Asynchronously, by uploading files to a MinIO bucket to trigger the OSCAR service upon
  file uploads.
* Synchronously, by invoking the service from OSCAR CLI or via the
  `OSCAR Manager's REST API <https://docs.oscar.grycap.net/api/>`__.
  A certain number of pre-deployed containers can be kept up and running to mitigate the
  cold start problem (initial delays when performing the first invocations to the service).
* Through Exposed Services, where stateless services created out of large containers
  require too much time to be started to process a service invocation.
  This is the case when supporting the fast inference of pre-trained AI models that
  require close to real-time processing with high throughput.
  In a traditional serverless approach, the AI model weights would be loaded in memory
  for each service invocation (thus creating a new container).
  With this approach AI model weights could be loaded just once and the service would
  perform the AI model inference for each subsequent request.
  An auto-scaled load-balanced approach for these stateless services is supported.

3. More info and examples
-------------------------

* `Official OSCAR documentation <https://docs.oscar.grycap.net>`__
* Examples to `deploy AI models with DEEPaaS support <https://github.com/grycap/oscar/tree/master/examples>`__,
  including:

  - The deployment of the `Body pose detection <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/DEEP-OC-posenet-tf>`__
    AI model from the AI4OS Marketplace is documented in the `body-pose-detection <https://github.com/grycap/oscar/tree/master/examples/body-pose-detection>`__
    folder, used to perform asynchronous invocations via MinIO.
  - The deployment of the `Plants Species Classifier <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/plants-classification>`__
    AI model from the AI4OS Marketplace is documented in the
    `plant-classification-sync <https://github.com/grycap/oscar/tree/master/examples/plant-classification-sync>`__
    folder, used to perform synchronous invocations.
