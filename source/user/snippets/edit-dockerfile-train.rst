Your ``./Dockerfile`` is in charge of creating a docker image that integrates
your application, along with deepaas and any other dependency.

You will see that the base Docker image is the image of the original repo.
Modify the appropriate lines to replace
the original model weights with the new model weights.
In our case, this could look something like this:

.. code-block:: docker

    ENV SWIFT_CONTAINER https://share.services.ai4os.eu/index.php/s/r8y3WMK9jwEJ3Ei/download
    ENV MODEL_TAR phytoplankton.tar.xz

    RUN rm -rf ai4os-image-classification-tf/models/*
    RUN curl --insecure -o ./image-classification-tf/models/${MODEL_TAR} \
        ${SWIFT_CONTAINER}/${MODEL_TAR}
    RUN cd ai4os-image-classification-tf/models && \
        tar -xf ${MODEL_TAR} &&\
        rm ${MODEL_TAR}

Check your Dockerfile works correctly by building it locally and running it:

.. code-block:: console

    $ docker build --no-cache -t your_project .
    $ docker run -ti -p 5000:5000 -p 6006:6006 -p 8888:8888 your_project

Your module should be visible in http://0.0.0.0:5000/ui