Train in batch mode
===================

.. admonition:: Requirements
   :class: info

   🔒 This tutorial requires :ref:`full authentication <getting-started/register:Full authentication>`.

This is a step by step guide on how to train a model with your own dataset in batch mode.
In batch mode, you will create a create a temporary job that is killed after the training is completed.

We are aware that batch mode is not as convenient for end users as :doc:`standard mode </howtos/train/standard>`, where you are given a persistent deployment that you can use with an IDE. Nevertheless, batch mode is preferable platform-wise because resources are optimally allocated.

To promote the usage of batch mode between users, we have **dedicated Tesla V100 GPU nodes** exclusively devoted to batch mode.

Batch mode can be used very similarly to :doc:`standard mode </howtos/train/standard>`, most of the tutorial still applies:

1. You start by preparing your data,
2. You create a batch job with the commands you want to run,
3. Your model weights are saved in the AI4OS storage when the job is completed,
4. You finally follow the same steps to add your model to the Marketplace,

What can I deploy in batch mode?
--------------------------------

You can deploy any existing module in the marketplace.
To create a batch job, click on the ``Batch`` button in the :ref:`module detail <dashboard_deployment>`.

.. image:: /_static/images/dashboard/module.png


It's also possible to :ref:`redeploy from a snapshot <dashboard_snapshots>`. In this case, a typical workflow would be for example:

1. to develop a model in a CPU deployment using VScode,
2. when you feel the model is ready to be trained, create a snapshot of your deployment,
3. in the snapshot table, redeploy your snapshot in batch mode

Configuring a batch job
-----------------------

Batch mode is very similar to standard mode configuration. The main differences are the following.

Storage
^^^^^^^

In batch mode, it is mandatory to :ref:`connect a storage <dashboard_storage>` to your job. This is done because:

* you need data to train, usually located in the storage (not in the Docker image itself)
* since the job is killed when it concludes, you cannot directly access the job to retrieve any outputs. So you need to **save your modelweights in your storage** to be able to retrieve them afterwards.

Batch commands
^^^^^^^^^^^^^^

These are the commands your job will execute.
In the configuration form, they can be provided either via a file upload or by adding the commands into an integrated editor.

.. image:: /_static/images/dashboard/batch-configuration.png
   :width: 400 px

In the following dummy example, we can save the current date in our storage, mimicking the saving of the modelweights at the end of a real training.

.. code-block:: bash

   echo "Test started"
   date > /storage/test-batch.txt
   sleep 20


Listing batch jobs
------------------

In the ``Batch`` tab on the left of the Dashboard, you will be able to see what are your current batch jobs, as well as the batch jobs that completed in the last 24 hours.

.. image:: /_static/images/dashboard/batch-table.png

Clicking on the job details you will see the resources as well as the training commands that the job executed.

.. image:: /_static/images/dashboard/batch-details.png
   :width: 400 px

Once you batch job is completed, you should be able to retrieved the modelweights from Nextcloud if you had a saving step in your training script.
Additionally, if your model is :doc:`integrated with MLflow </howtos/develop/mlflow>` you should be able to view your training stats in the MLflow UI.
