Our different user roles
========================

The AI4OS stack is focused on three different types of users.
Depending on what you want to achieve you should belong into one or more of the following categories:


.. image:: /_static/images/ai4eosc-user-roles.png


The basic user
--------------

This user wants to use modules that are already pre-trained and :doc:`test them with their data </user/howto/try/dashboard>`,
and therefore don't need to have any machine learning knowledge. For example, they can take an already trained module
for `plant classification <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/deep-oc-plants-classification-tf>`__
that has been containerized, and use it to classify their own plant images.

**What AI4OS can offer to you:**

* a :doc:`Dashboard <dashboard>` full of ready-to-use modules to perform inference with your data
* an :doc:`API <api>` to easily interact with the services
* solutions to run the inference in the Cloud or in your local resources
* the ability to develop complex topologies by composing different modules

**Related HowTo's:**

* :doc:`How to try a model in the Dashboard </user/howto/try/dashboard>`
* :doc:`How to try a model locally </user/howto/try/locally>`


The intermediate user
---------------------

The intermediate user wants to :doc:`retrain an available module </user/howto/train/dashboard>` to perform the same
task but fine tuning it to their own data.
They still might not need high level knowledge on modelling of machine learning problems, but typically do need basic
programming skills to prepare their own data into the appropriate format.
Nevertheless, they can re-use the knowledge being captured in a trained network and adjust the network to their problem
at hand by re-training the network on their own dataset.
An example could be a user who takes the generic `image classifier <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/ai4os-image-classification-tf>`__
model and retrains it to perform `seed classification <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/seeds-classification-tf>`__.

**What AI4OS can offer to you:**

* the ability to train out-of-the-box a module of the :doc:`Dashboard <dashboard>` on your personal dataset
* an :doc:`API <api>` to easily interact with the model
* :ref:`data storage resources <user/overview/architecture:The data storage resources>` to access your dataset
  using the `AI4OS Nextcloud <https://share.services.ai4os.eu/>`__ (up to 2 Terabytes by default)
* integration with popular cloud storage options like
  `Google Drive <https://www.google.com/drive/>`__, `Dropbox <https://www.dropbox.com/>`__,
  `Amazon S3 <https://aws.amazon.com/s3/>`__ and `many more <https://rclone.org/>`__
* the ability to deploy the developed service on Cloud resources
* the ability to share the service with other users in the user's catalogue

**Related HowTo's:**

* :doc:`How to train a model locally </user/howto/train/locally>`
* :doc:`How to train a model remotely </user/howto/train/dashboard>`


The advanced user
-----------------

The advanced users are the ones that will :doc:`develop their own machine learning models </user/howto/develop/dashboard>`
and therefore need to be competent in machine learning. This would be the case for example if we provided an image
classification model but the users wanted to perform object localization, which is a fundamentally different task.
Therefore they will design their own neural network architecture, potentially re-using parts of the code from other
models.

**What AI4OS can offer to you:**

* a ready-to-use environment with the main DL frameworks running in a dockerized solution running on different types of
  hardware (CPUs, GPUs, etc)
* :ref:`data storage resources <user/overview/architecture:The data storage resources>` to access your dataset
  using the `AI4OS Nextcloud <https://share.services.ai4os.eu/>`__ (up to 2 Terabytes by default)
* integration with popular cloud storage options like
  `Google Drive <https://www.google.com/drive/>`__, `Dropbox <https://www.dropbox.com/>`__,
  `Amazon S3 <https://aws.amazon.com/s3/>`__ and `many more <https://rclone.org/>`__
* the ability to deploy the developed module on Cloud resources
* the ability to share the module with other users in the :doc:`Dashboard <dashboard>`
* the possibility to :ref:`integrate your module with the API <user/overview/api:Integrate your model with the API>`
  to enable easier user interaction


**Related HowTo's:**

* :doc:`How to use the AI4OS Modules Template for model development <cookiecutter-template>`
* :doc:`How to develop your own machine learning model </user/howto/develop/dashboard>`
* :ref:`How to integrate your model with the DEEPaaS API <user/overview/api:Integrate your model with the API>`
