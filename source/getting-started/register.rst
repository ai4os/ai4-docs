Register an account
===================

We current are current transitioning from :ref:`EGI accounts (current) <getting-started/register:EGI account>` to our own :ref:`AI4OS accounts (beta) <getting-started/register:AI4OS account>`.

We recommend that you register for both accounts, so that you will be able to access
both migrated and non-migrated services at all times.
If you already have an :ref:`EGI account <getting-started/register:EGI account>`, it is straightforward to use it as a :ref:`federated identity <getting-started/register:Use a federated identity>` for AI4OS accounts.

.. TODO: basic/full authentication info is duplicated with info in user-access-levels.
.. But we leave i

EGI account
-----------

We offer two levels of authentication, depending on the services you want to access.
Find more about the services you can access with each authentication level.

Basic authentication
^^^^^^^^^^^^^^^^^^^^

This authentication level will let use some basic features like:

* :doc:`Try a model in the Dashboard </howtos/try/index>`
* :doc:`Deploy a model in your own cloud </howtos/deploy/cloud>`

To access this authentication level, go to the `EGI Check-In (prod) <https://aai.egi.eu/>`__
and login preferably with your **institutional account** (university, research center).
If this is not possible, please, use one of **Github** or **ORCID** but with the email
domain which identifies your organisation.
This will automatically create your new account at EGI Check-In.

Full authentication
^^^^^^^^^^^^^^^^^^^

This authentication level will let use all the features the AI4OS stack has to offer, including:

* :doc:`Developing a model in the Dashboard </howtos/develop/index>`
* :doc:`Training a model in the Dashboard </howtos/train/index>`
* :doc:`Deploying a model in production </howtos/deploy/index>`
* :doc:`Accessing the AI4OS storage </reference/storage>`

To access this authentication level, you need to be a `member` of either one of the following
projects:

* `AI4EOSC <https://ai4eosc.eu/>`__: AI for the European Open Science Cloud
* `iMagine <https://imagine-ai.eu/>`__: Imaging data and services for aquatic science
* `AI4Life <https://ai4life.eurobioimaging.eu/>`__: AI models and methods for the life sciences

.. admonition:: External users
   :class: info

   If you are not a member of the above projects, consider joining either one of them
   by applying to the *Open calls for external usecases*.
   More information about the Calls can be found in their respective project's homepages.

   If you were not able to apply in time to an Open Call, you can always try to `reach us <https://ai4eosc.eu/contact/>`__
   explaining why and how you would like to use the platform.

To achieve full authentication, first create an account following the :ref:`Basic authentication <getting-started/register:Basic authentication>` steps.
Then you have to enroll in one of the Virtual Organizations (VO) supported by the project.
Please :doc:`ask support </help/index>` for the request link of your Virtual Organization.

When enrolling, you have to provide the following information in ``Comments``:

* Reason to use the platform (e.g. use case)
* Your institution or organization
* How did you learn about the platform

You will need to wait until you are **approved** before being able to start using the
services.


AI4OS account
-------------

For the time being, this account is used to access the following services:

* :doc:`AI4OS LLM service </reference/dashboard>`

There are two options to create AI4OS accounts.

Use a federated identity
^^^^^^^^^^^^^^^^^^^^^^^^

This is the **preferred option**, especially for users coming from EGI Check-In authentication.
This is because Keycloak will automatically detect your EGI VO memberships (eg. ``vo.ai4eosc.eu``, ``vo.imagine-ai.eu``) and will grant your the proper platform full rights by default.

We currently offer several federated authentication options including:
`EGI-CheckIn <https://aai.egi.eu>`__,
`Github <https://github.com/>`__,
`Google <https://accounts.google.com/>`__,
and `IFCA SSO <https://sso.ifca.es>`__.

Accounts are mapped by email. So, for EGI Check-In users, we recommend authenticating the first time with EGI Check-In. Then, they can subsequently authenticate with any other option (eg. Github) as long as they share the same email.

Register a new account
^^^^^^^^^^^^^^^^^^^^^^

In order to register to the AI4OS platform you need to get an account on our `AI4OS SSO <https://login.cloud.ai4eosc.eu/realms/ai4eosc/account>`_. You can do this by
clicking on the ``Register`` link on the login page.

Please provide all the details that are listed in the registration form and preferably
use your **institutional account** (university, research center). This will speed up the
approval process.

After you have filled in all the details, click on the ``Register`` button. You will
receive an email with a link to confirm your registration. Click on the link to confirm
your registration and then you will be approved by an administrator.

Please remember that the approval process can take some time, so please be patient.
Also, be aware that just registering does not grant you access to the whole AI4OS platform, just some access to basic services.

Please request an upgrade if you need access to the full platform.


Login to the platform
=====================

Once registered and approved, you can directly head to the :doc:`/reference/dashboard`
page and login to the platform.
