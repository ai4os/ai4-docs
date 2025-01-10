Concepts and Terminology
========================

There are several different components in the AI4OS stack that are relevant for the users.
Later on you will see how each :doc:`different type of user <user-roles>` can take advantage of the different components.

The Dashboard
-------------

The :doc:`AI4OS dashboard </reference/dashboard>`. allow users to access computing resources to deploy, perform inference and train AI modules.
The Dashboard simplifies the deployment and hides some of the technical parts that most users do not need to worry about.


The AI modules
--------------

The :doc:`AI modules </reference/modules>` are developed both by the platform and by users.
For creating modules, we provide the :doc:`AI4OS Modules Template </reference/cookiecutter-template>`
as a starting point.

In addition to AI modules, the Dashboard also allows to deploy tools
(eg. a :doc:`Federated Server </howtos/train/federated-server>`).


The DEEPaaS API
---------------

The :doc:`DEEPaaS API </reference/api>` is a key component for making the modules accessible to everybody (including non-experts), as it
provides a consistent and easy to use way to access the model's functionality. It is available for both inference and training.

Advanced users that want to create new modules can make them :ref:`compatible with the API <deepaas-integrate>`
to make them available to the whole community. This can be easily done, since it only requires minor changes in user's code.


The data storage resources
--------------------------

:doc:`Storage </reference/storage>` is essential for users that want to create new services by training modules on their custom data. For the moment
we support hosting data in `AI4OS Nextcloud <https://share.services.ai4os.eu/>`__  instance.

In the future we will try to integrate as well with popular cloud storage options like  `Google Drive <https://www.google.com/drive/>`__,
`Dropbox <https://www.dropbox.com/>`__, `Amazon S3 <https://aws.amazon.com/s3/>`__ and `many more <https://rclone.org/>`__.


The Inference Platform (OSCAR)
------------------------------

The :doc:`Inference platform (OSCAR) </howtos/deploy/oscar>` is a fully managed service to facilitate users to deploy pre-trained AI models with horizontal scalability thanks to a serverless approach.

User can also compose those models in :doc:`complex AI workflow </howtos/pipelines/flowfuse>`


More info
---------

If you are curious this is a very high level overview of how the platform is structured:

.. image:: /_static/images/ai4eosc/architecture.png

And if you are feeling super-nerdy 🤓️, these are the low-level
`C4 architecture diagrams <https://structurizr.com/share/73873/2f769b91-f208-41b0-b79f-5e196435bdb1>`__
of the platform.
