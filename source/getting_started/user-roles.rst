Our different user roles
========================


The AI4OS stack is focused on three different types of users.
Depending on what you want to achieve you should belong into one or more of the following categories:


.. image:: /_static/images/ai4eosc/user-roles.png


The basic user
--------------

This user wants to use modules that are already pre-trained and test them with their data.
Therefore, they don't need to have any particular machine learning knowledge. For example, they can take an already trained module
for `plant classification <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/plants-classification>`__
that has been containerized, and use it to classify their own plant images.

**What AI4OS can offer to you:**

* a :doc:`Dashboard </reference/dashboard>` full of ready-to-use modules to perform inference with your data,
* an :doc:`API </reference/api>` to easily interact with the services,
* solutions to run the inference in the Cloud or in your local resources,
* the ability to develop complex topologies by composing different modules.

.. admonition:: Related HowTo's
   :class: info

   * :doc:`How to try a model </howtos/try/index>`
   * :doc:`How to deploy a model in production </howtos/deploy/index>`


The intermediate user
---------------------

The intermediate user wants to retrain an available module to perform the same task but
fine-tuning it to their own data.
They still might not need high level knowledge on modelling of machine learning problems, but typically do need basic
programming skills to prepare their own data into the appropriate format.
Nevertheless, they can re-use the knowledge being captured in a trained network and adjust the network to their problem
at hand by re-training the network on their own dataset.
An example could be a user who takes the generic `image classifier <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/ai4os-image-classification-tf>`__
model and retrains it to perform `plant classification <https://dashboard.cloud.ai4eosc.eu/marketplace/modules/plant-classification>`__.

**What AI4OS can offer to you:**

* the ability to train out-of-the-box a module of the :doc:`Dashboard </reference/dashboard>`,
* the ability to easily connect your training to your dataset hosted on our :doc:`data storage resources </reference/storage>`,
* the ability to use GPUs to accelerate your training,
* an :doc:`API </reference/api>` to easily interact with the model,
* the ability to deploy the developed service on Cloud resources,
* the ability to share your module with other users in the :ref:`Dashboard Marketplace <dashboard_marketplace>`.

.. admonition:: Related HowTo's
   :class: info

   * :doc:`How to train a model </howtos/train/index>`


The advanced user
-----------------

The advanced users are the ones that will develop their own machine learning models
and therefore need to be competent in machine learning.
This would be the case for example if we provided an image classification model
but the users wanted to perform object localization, which is a fundamentally different task.
Therefore they will design their own neural network architecture, potentially re-using parts of the code from other
models.

**What AI4OS can offer to you:**

* a ready-to-use environment with the main DL frameworks (Pytorch, Tensorflow) as well as the main IDEs (VScode, Jupyterlab),
* the ability to easily connect your environment to your dataset hosted on our :doc:`data storage resources </reference/storage>`,
* the ability to use GPUs to accelerate your training and development,
* the possibility to :ref:`integrate your module with the API <deepaas-integrate>` to enable easier user interaction,
* the ability to deploy the developed module on Cloud resources,
* the ability to share your module with other users in the :ref:`Dashboard Marketplace <dashboard_marketplace>`.

.. admonition:: Related HowTo's
   :class: info

   * :doc:`How to develop a model </howtos/develop/index>`
