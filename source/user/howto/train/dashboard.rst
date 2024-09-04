Train a model remotely
======================

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; margin-bottom: 2em; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/W1bPmUhzYFY" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

This is a step by step guide on how to train a general model from the :doc:`AI4OS Dashboard </user/overview/dashboard>`
with your own dataset.

In this tutorial we will see how to retrain a `generic image classifier <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/ai4os-image-classification-tf>`__
on a custom dataset to create a `phytoplankton classifier <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/uc-lifewatch-deep-oc-phyto-plankton-classification>`__.
If you want to follow along, you can download the toy phytoplankton dataset :fa:`download` `here <https://api.cloud.ifca.es:8080/swift/v1/public-datasets/phytoplankton-mini.zip>`__.

If you are new to Machine Learning, you might want to check some
:doc:`useful Machine Learning resources </user/others/useful-ml-resources>` we compiled to help you getting started.

.. admonition:: Requirements

    * You need  a :doc:`Authentication </user/overview/auth>` to be able to access the Dashboard and Nextcloud storage.
    * For **Step 7** we recommend having `docker <https://docs.docker.com/install/#supported-platforms>`__ installed (though it's not strictly mandatory).


1. Choose a module from the Marketplace
---------------------------------------

The first step is to choose a model from the :doc:`AI4OS Dashboard</user/overview/dashboard>`. Make sure to select a module with the ``trainable`` tag.
For educational purposes we are going to use a `general model to identify images <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/ai4os-image-classification-tf>`__.
Some of the model dependent details can change if using another model, but this tutorial will provide
a general overview of the workflow to follow when using any of the modules in the AI4OS Dashboard.


2. Upload your files to Nextcloud
---------------------------------

For this example we are going to use the `AI4OS Nextcloud <https://share.services.ai4os.eu/>`__ for storing
the dataset you want to retrain the model with.

So login to Nextcloud with your :doc:`credentials </user/overview/auth>`
and you should access to an overview of your files.
Now it's time to upload your dataset.
When training a model, the data has usually to be in a specific format and folder structure.
It's usually helpful to read the README in the source code of the module
(in this case `located here <https://github.com/ai4os-hub/ai4os-image-classification-tf>`__)
to learn the correct way to setting it up.

In the case of the **image classification module**, we will create the following folders:

.. image:: /_static/images/nextcloud/folders.png

* A folder called ``models`` where the new training weights will be stored after the training is completed
* A folder called ``data`` that contains two different folders:

  * The sub folder ``images`` containing the input images needed for the training
  * The sub folder ``dataset_files`` containing a couple of files:

    * ``train.txt`` indicating the relative path to the training images
    * ``classes.txt`` indicating which are the categories for the training

Again, the folder structure and their content will of course depend on the module to be used.
This structure is just an example in order to complete the workflow for this tutorial.

Once you have prepared your data locally, you can drag your folder to the Nextcloud Web UI to upload it.

If you have your dataset in a remote machine, you will have to
:ref:`install rclone <user/howto/train/rclone:1. Installing rclone>` on your remote machine,
:ref:`configure it <user/howto/train/rclone:2. Configuring rclone>`
and do an :ref:`rclone copy <user/howto/train/rclone:3. Using rclone>` to move your data to Nextcloud.

.. tip::

    Uploading to Nextcloud can be particularly slow if your dataset is composed of lots of small files.
    Considering zipping your folder before uploading.

    .. code-block:: console

        $ zip -r <foldername>.zip <foldername>
        $ unzip <foldername>.zip


3. Deploy with the Training Dashboard
-------------------------------------

Now go to the :doc:`AI4OS Dashboard </user/overview/dashboard>`  and login with your :doc:`credentials </user/overview/auth>`.
Then go to (1) **Modules (marketplace)** ➜ (2) **Train image classifier** ➜ (3) **Train module**.

Now you will be presented with a configuration form.
For the purposes of running a retraining, it should be filled as following:

1. In the **General configuration** you should select:

* ``Template = default (with storage options)``, unless stated otherwise in your modules README.
* ``Command = JupyterLab`` because we want the flexibility of being able to interact with the code and the terminal, not just the API.
* ``Hardware configuration = GPU`` because training is a very resource consuming task.
* ``Docker tag = gpu`` because Docker tag has to match the hardware it will be run on.

2. Once this is set, you can proceed to fill the **Specific configuration**:

* ``jupyter password``, you have to provide a password at least 9 characters long, so that nobody will be able to access your machine, which will be exposed on a public IP.
* ``rclone_user``, ``rclone_password``: those are the credentials to be able to mount your Nextcloud directory in your deployment.
  :ref:`Go here <user/howto/train/rclone:2. Configuring rclone>` in order to find how to create them.

Now that you are done configuring, click **Submit** to create the deployment.
See the :doc:`Dashboard guide </user/overview/dashboard>` for more details.


4. Go to JupyterLab and mount your dataset
------------------------------------------

After submitting you will be redirected to the deployment's list.
In your new deployment go to **Access** and choose **JupyterLab**. You will be redirected to ``http://jupyterlab_endpoint``

Now that you are in JupyterLab, open a **Terminal** window (:fa:`square-plus` (New launcher) ➜ **Others** ➜ **Terminal**).

First let's check we are seeing our GPU correctly:

.. code-block:: console

    $ nvidia-smi

This should output the GPU model along with some extra info.

Then :ref:`configure rclone <user/howto/train/rclone:2. Configuring rclone>`.
We can also check rclone is correctly configured with:

.. code-block:: console

    $ rclone about rshare:

which should output your used space in Nextcloud.

.. tip::
    If you happen to need additional packages, you will have to update the package index first.
    Note that sudo is not needed as you are always root in your Docker containers:

    .. code-block:: console

        $ apt update
        $ apt install vim

Now we will mount our remote Nextcloud folders in our local containers:

.. code-block:: console

    $ rclone copy rshare:/data/dataset_files /srv/ai4os-image-classification-tf/data/dataset_files
    $ rclone copy rshare:/data/images /srv/ai4os-image-classification-tf/data/images

Paths with the ``rshare`` prefix are Nextcloud paths.
As always, paths are specific to this example. Your module might need different paths.
If you zipped your files before uploading to Nextcloud you will have to ``rclone copy`` the ``zip`` file,
unzip it and copy the contents to the appropriate folders.

Mounting your dataset *might take some time*, depending on the dataset size, file structure (lots of small files vs few big files), and so on.
So grab a cup of coffee and prepare for the next steps.

Now that you dataset is mounted, we will run DEEPaaS to interactively run the training. In your terminal window type:

.. code-block:: console

    $ nohup deep-start --deepaas &

The ``&`` will keep your command running even if you close the terminal, and ``nohup`` will produce a log file
``nohup.out`` that you can always look at if you want to know what is going on under the hood.


5. Open the DEEPaaS API and train the model
-------------------------------------------

Now go back to the deployments list view.
In your deployment go to **Access** and choose **DEEPaaS**. You will be redirected to ``http://deepaas_endpoint/ui``.

.. image:: /_static/images/endpoints/deepaas.png
   :width: 500 px

Look for the ``train`` POST method. Modify the training parameters you wish to change
and execute.

If some kind of monitorization tool is available for the module, you will be able to
follow the training progress at ``http://monitor_endpoint`` (click **Access** button
➜ **Monitoring**, in the deployments page).
For example, in the image classification module, you can monitor training progress with
Tensorboard.

.. image:: /_static/images/endpoints/tensorboard.png


6. Test and export the newly trained model
------------------------------------------

Once the training has finished, you can directly test it by clicking on the ``predict`` POST method.
For this you have to kill the process running deepaas, and launch it again.

.. code-block:: console

    $ kill -9 $(ps aux | grep '[d]eepaas-run' | awk '{print $2}')
    $ kill -9 $(ps aux | grep '[t]ensorboard' | awk '{print $2}')  # optionally also kill monitoring process

This is because the user inputs for deepaas are generated at the deepaas launching.
Thus it is not aware of the newly trained model. Once deepaas is restarted, head to the
``predict`` POST method, select you new model weights and upload the image your want to classify.

If you are satisfied with your model, then it's time to save it into your remote storage,
so that you still have access to it if your machine is deleted.
For this we have to create a ``tar`` file with the model folder (in this case, the foldername is
the timestamp at which the training was launched) so that we can download in our Docker container.

So go back to JupyterLab, open a Terminal window and run:

.. code-block:: console

    $ cd /srv/ai4os-image-classification-tf/models
    $ tar cfJ <modelname.tar.xz> <foldername>
    $ rclone copy /srv/ai4os-image-classification-tf/models rshare:/models

Now you should be able to see your new models weights in Nextcloud.

For the next step, you need to make them `publicly available <https://docs.nextcloud.com/server/latest/user_manual/en/files/sharing.html>`__
through an URL so they can be downloaded in your Docker container.
In Nextcloud, go to the ``tar`` file you just created:
:fa:`share-nodes` ➜ Share Link ➜ :fa:`square-plus` (Create a new share link)

.. admonition:: Zenodo preservation

    `Optionally`, in order to improve the reproducibility of your code, we encourage you
    to share your training dataset on `Zenodo <https://zenodo.org>`__.
    Once you upload the dataset, make sure to link it with the relevant Zenodo community
    (`AI4EOSC <https://zenodo.org/communities/ai4eosc>`__,
    `iMagine <https://zenodo.org/communities/imagine-project>`__).

    If long-term preservation and versioning of model weights is important to you, you can
    also upload the model weights to Zenodo in addition to Nextcloud.


7. Create a repo for your new module
------------------------------------

Now, let's say you want to share your new application with your colleagues.
The process is much simpler that when :doc:`developing a new module from scratch </user/howto/develop/dashboard>`,
as your code is the same as the original application, only your model weights
are different.

To account for this simpler process, we have prepared a version of the
:doc:`the AI4OS Modules Template </user/overview/cookiecutter-template>`
specially tailored to this task:

* Go to the `Template creation webpage <https://templates.cloud.ai4eosc.eu/>`__.
  You will need an :doc:`authentication </user/overview/auth>` to access to this webpage.
* Then select the ``child-module`` branch of the template and answer the questions.
* Click on ``Generate`` and you will be able to download a ``.zip`` file with
  the project's directory. Extract it locally.


8. Update your project's metadata
---------------------------------

.. include:: /user/snippets/edit-metadata.rst


9. Update your project's Dockerfile
-----------------------------------

.. include:: /user/snippets/edit-dockerfile-train.rst


10. Integrating the module in the Marketplace
---------------------------------------------

.. include:: /user/snippets/integrate-marketplace.rst


11. Next steps
--------------

Do you want to go further?

* What about trying to integrate :doc:`MLflow Experiment tracking </user/howto/develop/mlflow>` into your deployment?

.. tip::

    If you run into problems you can always check the :doc:`Frequently Asked Questions (FAQ) </user/support/faq>`.


.. TODO: renable when ready

.. 9. [optional] Add your new module to the original Continuous Integration pipeline
.. ---------------------------------------------------------------------------------

.. Your module is already in the Marketplace.
.. But what happens if the code in the original image-classification module changes?
.. This should trigger a rebuild of your Docker container as it is based on that code.

.. This can be achieved by modifying the ``Jenkinsfile`` in the `image-classification Docker repo <https://github.com/ai4os-hub/ai4os-image-classification-tf/blob/master/Jenkinsfile>`__.
.. One would add an additional stage to the Jenkins pipeline like so:

.. .. code-block::

..     stage("Re-build DEEP-OC Docker images for derived services") {
..         when {
..             anyOf {
..                branch 'master'
..                branch 'test'
..                buildingTag()
..             }
..         }
..         steps {

..             // Wait for the base image to be correctly updated in DockerHub as it is going to be used as base for
..             // building the derived images
..             sleep(time:5, unit:"MINUTES")

..             script {
..                 def derived_job_locations =
..                 ['Pipeline-as-code/DEEP-OC-org/DEEP-OC-plants-classification-tf',
..                  'Pipeline-as-code/DEEP-OC-org/DEEP-OC-conus-classification-tf',
..                  'Pipeline-as-code/DEEP-OC-org/DEEP-OC-seeds-classification-tf',
..                  'Pipeline-as-code/DEEP-OC-org/DEEP-OC-phytoplankton-classification-tf'
..                  ]

..                 for (job_loc in derived_job_locations) {
..                     job_to_build = "${job_loc}/${env.BRANCH_NAME}"
..                     def job_result = JenkinsBuildJob(job_to_build)
..                     job_result_url = job_result.absoluteUrl
..                 }
..             }
..         }
..     }

.. So if you want this step to be performed, you must submit a PR to the original module Docker repo with similar changes as above.
