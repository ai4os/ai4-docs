Train a model
=============

.. admonition:: Requirements
   :class: info

   🔒 This tutorial requires :ref:`full authentication <getting-started/register:Full authentication>`.

This is a step by step guide on how to train a model with your own dataset.

If you are new to Machine Learning, you might want to check some :doc:`useful Machine Learning resources </others/useful-ml-resources>` we compiled to help you getting started.

.. admonition:: Requirements
    :class: info

    * You need :doc:`full authentication </reference/user-access-levels>` to be able to access both the Dashboard and Nextcloud storage.
    * For **Step 8** we recommend having `docker <https://docs.docker.com/install/#supported-platforms>`__ installed (though it's not strictly mandatory).


1. Upload your dataset to Nextcloud
-----------------------------------

For this example we are going to use the `AI4OS Nextcloud <https://share.services.ai4os.eu/>`__ for storing
the dataset you want to retrain the model with. So login to Nextcloud with your credentials and you should access to an overview of your files.

.. image:: /_static/images/nextcloud/folders.png

Now it's time to upload your dataset.
When training a model, the data has usually to be in a specific format and folder structure.
It's usually helpful to read the README in the source code of the module (in this case `located here <https://github.com/ai4os-hub/ai4os-image-classification-tf>`__) to learn the correct way to setting it up.

In the case of the **image classification module**, we will create the following folders:

* A folder called ``models`` where the new training weights will be stored after the training is completed
* A folder called ``data`` that contains two different folders:

  * The sub folder ``images`` containing the input images needed for the training
  * The sub folder ``dataset_files`` containing a couple of files:

    * ``train.txt`` indicating the relative path to the training images
    * ``classes.txt`` indicating which are the categories for the training

Again, the folder structure and their content will of course depend on the module to be used.

Once you have prepared your data locally, you can drag your folder to the Nextcloud Web UI to upload it.

.. admonition:: Uploading tips
    :class: tip

    * If you need to upload your dataset from a remote machine (ie. no GUI), you can
      :ref:`install rclone <rclone_installation>` on your
      remote machine, :ref:`configure it <rclone_configuration>` and do an :ref:`rclone
      copy <rclone_usage>` to move your data to Nextcloud.

    * Uploading to Nextcloud can be particularly slow if your dataset is composed of lots of small files.
      Considering zipping your folder before uploading.

      .. code-block:: console

          $ zip -r <foldername>.zip <foldername>
          $ unzip <foldername>.zip


2. Prepare your training environment
------------------------------------

In this tutorial we will see how to retrain a `generic image classifier <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/ai4os-image-classification-tf>`__
on a custom dataset to create a `phytoplankton classifier <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/phyto-plankton-classification>`__.
If you want to follow along, you can download the toy phytoplankton dataset :fa:`download` `here <https://api.cloud.ifca.es:8080/swift/v1/public-datasets/phytoplankton-mini.zip>`__.

The first step is to choose a model from the :doc:`AI4OS Dashboard</reference/dashboard>`. Make sure to select a module with the ``AI4 trainable`` tag.
For educational purposes we are going to retrain a `generic image classifier <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/ai4os-image-classification-tf>`__.
Some of the model dependent details can change if using another model, but this tutorial will provide a general overview of the workflow to follow when using any of the modules in the AI4OS Dashboard.

Check :ref:`how to configure <dashboard_deployment>` the  image classifier.
During the configuration, you should make sure:

* to select either ``JupyterLab`` or ``VScode`` as the **service** to run, because we want the flexibility of being able to interact with the code and the terminal, not just the API.
* to select ``GPU`` as **hardware**, because training is a very resource consuming task. This will also imply that you might need to select a **Docker tag** that is compatible with GPUs.
* to connect with one of your synced **storage providers**  (in our case, the project's Nextcloud instance)


3. Access your deployment
-------------------------

After submitting you will be redirected to the deployment's list.
In your new deployment, select ⓘ ``Info`` and click in the IDE endpoint, when it becomes active.
After logging in you should be able to to see your IDE:

.. image:: /_static/images/endpoints/vscode.png

Now, open a Terminal to perform some sanity checks:

* **Check the GPU is correctly mounted**:

  .. code-block:: console

    $ nvidia-smi

  This should output the GPU model along with some extra info.

* **Your storage is correctly mounted**:

  .. code-block:: console

    $ ls /storage

  This should output your Nextcloud folder structure.

  .. admonition:: Accessing storage
    :class: info

    Your files under ``/storage`` are mounted via a virtual filesystem.
    This has :doc:`pros and cons </reference/storage>`.
    We also offer the possibility to :ref:`copy the files to the local machine <rclone_usage>` as long as they fit the available disk.


4. Start training the model
---------------------------

We will use the DEEPaaS API to interactively run the training. In your Terminal type:

.. code-block:: console

    $ nohup deep-start --deepaas &

The ``&`` will keep your command running even if you close the terminal, and ``nohup`` will produce a log file ``nohup.out`` that you can always look at if you want to know what is going on under the hood.

Now go back to the Dashboard, in the ``Deployments`` list view.
In your deployment go to ⓘ ``Info`` and click on the ``API`` active endpoint.

.. image:: /_static/images/endpoints/deepaas.png
   :width: 500 px

Look for the ``train`` POST method. Modify the training parameters you wish to change and execute. In our case, you might need to correctly point to the training dataset location.

If some kind of monitorization tool is available for the module, you will be able to follow the training progress at ``Monitor`` active endpoint. In the case of the image classification module, you can monitor training progress with Tensorboard.

.. image:: /_static/images/endpoints/tensorboard.png


5. Test and export the newly trained model
------------------------------------------

Once the training has finished, you can directly test it by clicking on the ``predict`` POST method. For this you have to kill the process running deepaas, and launch it again.

.. code-block:: console

    $ kill -9 $(ps aux | grep '[d]eepaas-run' | awk '{print $2}')
    $ kill -9 $(ps aux | grep '[t]ensorboard' | awk '{print $2}')  # optionally also kill monitoring process
    $ nohup deep-start --deepaas &  # relaunch

.. admonition:: Note
    :class: info

    We need to do this because the user inputs for deepaas are generated at the deepaas launching. Thus the original deepaas process is not aware of the newly trained model.

Once deepaas is restarted, head to the ``predict`` POST method, select you new model weights and upload the image your want to classify.

If you are satisfied with your model, then it's time to save it into your remote storage.
Open a Terminal window and run:

.. code-block:: console

    $ cd /srv/ai4os-image-classification-tf/models
    $ tar cfJ <modelname.tar.xz> <foldername>  # create a tar file
    $ cp <modelname.tar.xz> /storage/  # save to storage

Now you should be able to see your new models weights in Nextcloud.
For **Step 8**, you will need to download the weights from the Dockerfile. To allow this, make the weights atr file `publicly available <https://docs.nextcloud.com/server/latest/user_manual/en/files/sharing.html>`__. For this, click on :fa:`share-nodes` ➜ Share Link ➜ :fa:`square-plus` (Create a new share link)

.. admonition:: Zenodo preservation
    :class: info

    `Optionally`, in order to improve the reproducibility of your code, we encourage you
    to share your training dataset on `Zenodo <https://zenodo.org>`__.
    Once you upload the dataset, make sure to link it with the relevant Zenodo community
    (`AI4EOSC <https://zenodo.org/communities/ai4eosc>`__,
    `iMagine <https://zenodo.org/communities/imagine-project>`__).

    If long-term preservation and versioning of model weights is important to you, you can
    also upload the model weights to Zenodo in addition to Nextcloud.


6. Create a repo for your new module
------------------------------------

Now, let's say you want to share your new application with your colleagues.
The process is much simpler that when :doc:`developing a new module from scratch </howtos/develop/dashboard>`,
as your code is the same as the original application, only your model weights
are different.

To account for this simpler process, we have prepared a version of the
:doc:`the AI4OS Modules Template </reference/cookiecutter-template>`
specially tailored to this task:

* Go to the `Template creation webpage <https://templates.cloud.ai4eosc.eu/>`__.
  You will need an :doc:`authentication </reference/user-access-levels>` to access to this webpage.
* Then select the ``child-module`` branch of the template and answer the questions.
* Click on ``Generate`` and you will be able to download a ``.zip`` file with
  the project's directory. Extract it locally.


7. Update your project's metadata
---------------------------------

.. include:: /snippets/edit-metadata.rst


8. Update your project's Dockerfile
-----------------------------------

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


9. Integrating the module in the Marketplace
--------------------------------------------

.. include:: /snippets/integrate-marketplace.rst


.. admonition:: Next steps
    :class: tip

    If to go further, check our tutorials on how to:

    * :doc:`run a federated learning training </howtos/train/federated-server>`
