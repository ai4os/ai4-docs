Authentication
==============

The authentication for the AI4OS stack depends on the platform it is deployed.

Current supported platforms use the following Identity providers:

.. * **AI4EOSC**: :ref:`EGI Check-In (demo)  <user/overview/auth:EGI Check-In (demo)>`
.. * **iMagine**: :ref:`EGI Check-In (demo)  <user/overview/auth:EGI Check-In (demo)>`

* **AI4EOSC**: :ref:`EGI Check-In (prod)  <user/overview/auth:EGI Check-In (prod)>`
* **iMagine**: :ref:`EGI Check-In (prod)  <user/overview/auth:EGI Check-In (prod)>`

Some services (eg. Nextcloud) still rely on the :ref:`DEEP IAM  <user/overview/auth:DEEP IAM>` provider.


How to create an account
------------------------

.. EGI Check-In (demo)
.. ^^^^^^^^^^^^^^^^^^^

.. Go to the `EGI Check-In (demo) <https://aai-demo.egi.eu/>`__ and login ith your
.. preferred account (university, Github, ORCID, Google, etc).
.. This will automatically create your new account.

.. Now you have to enroll in one of the Virtual Organizations (VO) supported by the project:

.. * `AI4EOSC <https://aai-demo.egi.eu/registry/co_petitions/start/coef:179>`__ (``vo.ai4eosc.eu``)
.. * `iMagine <https://aai-demo.egi.eu/registry/co_petitions/start/coef:181>`__ (``vo.imagine-ai.eu``)
.. * `Tutorials <https://aai-demo.egi.eu/registry/co_petitions/start/coef:10>`__ (``training.egi.eu``): reserved for people who will experiment with the platform during a tutorial

.. You will need to wait until you are **approved** before being able to start using the services (eg. the :doc:`AI4OS Dashboard <dashboard>`).

EGI Check-In (prod)
^^^^^^^^^^^^^^^^^^^

Go to the `EGI Check-In (prod) <https://aai.egi.eu/>`__ and login preferably with your **institutional 
account** (university, research center). If this is not possible, please, use one of **Github** or **ORCID** 
but with the E-Mail domain which identifies your organisation.
This will automatically create your new account at EGI Check-In.

Now you have to enroll in one of the Virtual Organizations (VO) supported by the project:

* `AI4EOSC <https://aai.egi.eu/registry/co_petitions/start/coef:550>`__ (``vo.ai4eosc.eu``)
* `iMagine <https://aai.egi.eu/registry/co_petitions/start/coef:546>`__ (``vo.imagine-ai.eu``)
* `Tutorials <https://aai.egi.eu/registry/co_petitions/start/coef:10>`__ (``training.egi.eu``): reserved for people who will experiment with the platform during a tutorial

You will need to wait until you are **approved** before being able to start using the services (eg. the :doc:`AI4OS Dashboard <dashboard>`).

.. warning::
    You have to provide (e.g. in "Comments") the following information:
    * Reason to use the platform (e.g. use case)
    * Your institution or organisation
    * How did you learn about the platform


DEEP IAM
^^^^^^^^

Go to the `DEEP IAM <https://iam.deep-hybrid-datacloud.eu/login>`__ and select
``Apply for an account``.
