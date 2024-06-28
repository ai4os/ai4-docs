Try a service locally
=====================

.. admonition:: Useful video demos
   :class: important

    - `Running a module locally with docker <https://www.youtube.com/watch?v=3ORuymzO7V8&list=PLJ9x9Zk1O-J_UZfNO2uWp2pFMmbwLvzXa&index=13>`__

.. admonition:: Requirements

    This section requires having `docker <https://docs.docker.com/install/#supported-platforms>`__ installed.

    Starting from version 19.03 docker supports NVIDIA GPUs (see `here <https://docs.docker.com/engine/release-notes/>`__ and `here <https://github.com/moby/moby/pull/38828>`__).
    If you happen to be using an older version you can give a try to `nvidia-docker <https://github.com/nvidia/nvidia-docker/wiki/Installation-(version-2.0)>`__

    If you need to use docker in an environment without root privileges (eg. an HPC cluster)
    check `udocker <https://github.com/indigo-dc/udocker/releases>`__ instead of docker.


1. Choose your module
---------------------

The first step is to choose a module from the :doc:`Dashboard</user/overview/dashboard>`.
For educational purposes we are going to use a `general model to identify images <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/ai4os-image-classification-tf>`__. This will allow us to see the general workflow.

Once we have chosen the Module page we will
find that it has an associated docker container in `DockerHub <https://hub.docker.com/u/ai4oshub/>`__. For example, in the
example we are running here, the container would be ``ai4oshub/ai4os-image-classification-tf``. This means that to pull the
docker image and run it you should:

.. code-block:: console

    $ docker pull ai4oshub/ai4os-image-classification-tf

Docker images have usually tags depending on whether they are using ``master`` or ``test`` and whether they use
``cpu`` or ``gpu``. Tags are usually:

* ``latest`` or ``cpu``: master + cpu
* ``gpu``: master + gpu
* ``cpu-test``: test + cpu
* ``gpu-test``: test + gpu

So if you wanted to use gpu and the test branch you could run:

.. code-block:: console

    $ docker pull ai4oshub/ai4os-image-classification-tf:gpu-test

Instead of pulling from Dockerhub you can choose to build the image yourself:

.. code-block:: console

    $ git clone https://github.com/ai4os-hub/ai4os-image-classification-tf
    $ cd ai4os-image-classification-tf
    $ docker build -t ai4oshub/ai4os-image-classification-tf .


2. Launch the API and predict
-----------------------------

Run the container with

.. code-block:: console

	$ docker run -ti -p 5000:5000 -p 6006:6006 -p 8888:8888 ai4oshub/ai4os-image-classification-tf

Once running, point your browser to http://127.0.0.1:5000/ui and you will see the API documentation, where you can
test the module's functionality, as well as perform other actions.

.. image:: /_static/images/deepaas.png
  :width: 500

Go to the  ``predict()`` function and upload the file/data you want to predict (in the case of the image classifier
this should be an image file). The appropriate data formats of the files you have to upload are often discussed
in the module's Marketplace page or in their Github README files.

The response from the ``predict()`` function will vary from module to module but usually consists on a JSON dict
with the predictions. For example the image classifier return a list of predicted classes along with predicted accuracy.
Other modules might return files (eg. images, zips, ...) instead of a JSON response.
