Register an account
===================

The `AI4OS Login <https://login.cloud.ai4eosc.eu/realms/ai4eosc/account>`__ uses Keycloak to federate different Identity providers, allowing to easily onboard new external communities with their own authentication systems.

.. image:: /_static/images/ai4eosc/keycloak.png
   :width: 300 px
   :align: center

There are two options to create AI4OS accounts.


Option 1. Use a federated identity
----------------------------------

.. |egicheckin| image:: /_static/images/favicons/egicheckin.png
   :height: 1em
   :alt: Button icon
   :class: no-scaled-link

.. |myaccessid| image:: /_static/images/favicons/myaccessid.png
   :height: 1em
   :alt: Button icon
   :class: no-scaled-link

.. |ifca| image:: /_static/images/favicons/ifca.png
   :height: 1em
   :alt: Button icon
   :class: no-scaled-link

.. |ai4eosc| image:: /_static/images/favicons/ai4eosc.png
   :height: 1em
   :alt: Button icon
   :class: no-scaled-link

.. |orcid| image:: /_static/images/favicons/orcid.ico
   :height: 1em
   :alt: Button icon
   :class: no-scaled-link


.. todo add favicons before naming the different identities

This is the :material-outlined:`verified;1.5em` **recommended option** for:

* users coming from |egicheckin| `EGI-CheckIn <https://aai.egi.eu>`__ authentication (like AI4EOSC, iMagine and AI4life users).
  This is because Keycloak will automatically detect your EGI VO memberships
  (eg. ``vo.ai4eosc.eu``, ``vo.imagine-ai.eu``) and will grant your the proper platform full rights by default.

  .. dropdown:: ㅤ 💡 Open an |egicheckin| EGI Check-In account

    This mini tutorial is dedicated to users of the following projects:

    * `AI4EOSC <https://ai4eosc.eu/>`__: AI for the European Open Science Cloud
    * `iMagine <https://imagine-ai.eu/>`__: Imaging data and services for aquatic science
    * `AI4Life <https://ai4life.eurobioimaging.eu/>`__: AI models and methods for the life sciences

    To access this authentication level, go to the `EGI Check-In (prod) <https://aai.egi.eu/>`__
    and login preferably with your **institutional account** (university, research center).
    If this is not possible, please, use one of **Github** or **ORCID** but with the email
    domain which identifies your organisation.
    This will automatically create your new account at EGI Check-In.

    Then you have to enroll in one of the Virtual Organizations (VO) supported by the project.
    Please :doc:`ask support </help/index>` for the request link of your Virtual Organization.

    When enrolling, you have to provide the following information in ``Comments``:

    * Reason to use the platform (e.g. use case)
    * Your institution or organization
    * How did you learn about the platform

    You will need to wait until you are **approved** before being a full member of the VO.


* researchers with |myaccessid| `EduGain <https://edugain.org/>`__ credentials, as you will be granted increased privileges due to your trusted researcher status

Additionally, we offer several federated authentication options including:
:fab:`github` `Github <https://github.com/>`__,
:fab:`google` `Google <https://accounts.google.com/>`__,
|ifca| `IFCA SSO <https://sso.ifca.es>`__ and
|orcid| `ORCID <https://orcid.org/>`__.

.. tip::

  Accounts are mapped by email. So you can authenticate the first time with EGI Check-In, then can subsequently authenticate with any other option (eg. Github), as long as they share the same email.

Each authentication system will grant different :doc:`user access levels </reference/user-access-levels>`.
In short:

* users coming from the (`AI4EOSC <https://ai4eosc.eu/>`__, `iMagine <https://imagine-ai.eu/>`__, `AI4Life <https://ai4life.eurobioimaging.eu/>`__) projects will have **full access** level.
* user coming from EduGain will have **intermediate access** level.
* remaining users (eg. Github, Google) will only have **basic access** level (observers).

Find how to :ref:`upgrade you access level <reference/user-access-levels:Upgrading your access level>`.


Option 2. Register a new account
--------------------------------

It is also possible to manually registering new account, although *this is not
recommended* as the process is slower, since requests need to be manually approved by
an administrator.

To register a new account manually:

* Click on the ``Register`` link on the login page,
* Please provide all the details that are listed in the registration form and preferably
  use your **institutional account** (university, research center). This will speed up the
  approval process.
* After you have filled in all the details, click on the ``Register`` button. You will
  receive an email with a link to confirm your registration. Click on the link to confirm
  your registration and then you will be approved by an administrator.

Accounts created this way will have **basic access** level by default (see :doc:`user access levels </reference/user-access-levels>`).

Once created, you can input your credentials using the ``Sign In`` option, at the top of the page.


Login to the platform
=====================

Once registered, you can directly head to the :doc:`/reference/dashboard` page and login to the platform.
