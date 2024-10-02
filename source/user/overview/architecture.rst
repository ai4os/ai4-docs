Architecture overview
=====================

There are several different components in the AI4OS stack that are relevant for the users.
Later on you will see how each :doc:`different type of user <user-roles>` can take advantage of the different components.

The Dashboard
-------------

The :doc:`AI4OS dashboard <dashboard>`. allow users to access computing resources to deploy, perform inference and train AI modules.
The Dashboard simplifies the deployment and hides some of the technical parts that most users do not need to worry about.


..
  TODO: uncomment when OSCAR is ready

  DEEP as a Service
  -----------------

  `DEEP as a Service (or DEEPaaS) <https://docs.ai4eosc.eu/projects/deepaas/en/stable/>`__ is a fully managed service that allows
  to easily and automatically deploy developed applications as services, with horizontal scalability thanks to a
  serverless approach. Module owners only need to care about the application development process, and incorporate
  new features that the automation system receives as an input.

  The serverless framework allows any user to automatically deploy from the browser any module in real time to try it.
  It only supports prediction. For training, which is more resource consuming, users must use the AI4OS Dashboard.


The AI modules
--------------

The :doc:`AI modules <modules>` are developed both by the platform and by users.
For creating modules, we provide the :doc:`AI4OS Modules Template <cookiecutter-template>`
as a starting point.

In addition to AI modules, the Dashboard also allows to deploy tools
(eg. a :doc:`Federated Server </user/howto/train/federated-server>`).


The DEEPaaS API
---------------

The :doc:`DEEPaaS API <api>` is a key component for making the modules accessible to everybody (including non-experts), as it
provides a consistent and easy to use way to access the model's functionality. It is available for both inference and training.

Advanced users that want to create new modules can make them :ref:`compatible with the API <user/overview/api:Integrate your model with the API>`
to make them available to the whole community. This can be easily done, since it only requires minor changes in user's code.


The data storage resources
--------------------------

:doc:`Storage <storage>` is essential for users that want to create new services by training modules on their custom data. For the moment
we support hosting data in `AI4OS Nextcloud <https://share.services.ai4os.eu/>`__  instance.

In the future we will try to integrate as well with popular cloud storage options like  `Google Drive <https://www.google.com/drive/>`__,
`Dropbox <https://www.dropbox.com/>`__, `Amazon S3 <https://aws.amazon.com/s3/>`__ and `many more <https://rclone.org/>`__.


The Inference Platform (OSCAR)
------------------------------

The :doc:`Inference platform (OSCAR) </user/howto/deploy/oscar>` is a fully managed service to facilitate users to deploy pre-trained AI models with horizontal scalability thanks to a serverless approach.

User can also compose those models in :doc:`complex AI workflow </user/howto/pipelines/flowfuse>`


More info
---------

If you are curious this is a very high level overview of how the platform is structured:

.. image:: /_static/images/ai4eosc/architecture.png

And if you are feeling super-nerdy 🤓️, these are the low-level
`C4 architecture diagrams <https://structurizr.com/share/73873/2f769b91-f208-41b0-b79f-5e196435bdb1>`__
of the platform.
