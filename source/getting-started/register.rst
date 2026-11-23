Access the platform
===================

Register an account
-------------------

The `AI4EOSC Login <https://login.cloud.ai4eosc.eu/realms/ai4eosc/account>`__ uses Keycloak to federate different Identity providers, allowing to easily onboard new external communities with their own authentication systems.

.. image:: /_static/images/ai4eosc/keycloak.png
   :width: 300 px
   :align: center

AI4EOSC federates a set of identity providers in order to grant access to the platform.
For first time users, we recommend login with either one of the following two providers:

* |myaccessid| `EduGain <https://edugain.org/>`__: this is the :material-outlined:`verified;1.5em` **recommended option for most users** as you will be granted increased privileges (:doc:`intermediate access level </reference/user-access-levels>`) due to your trusted researcher status.

  .. dropdown:: ㅤ 💡 Login with EduGain: University of Cantabria example

    Start by searching for your institution in the search bar (in this case we search for the ``University of Cantabria``):

    .. image:: /_static/images/others/edugain-search.png
       :width: 400 px
       :align: center

    Then, you should be redirected to your institution page to provide your credentials:

    .. image:: /_static/images/others/edugain-unican.png
       :width: 400 px
       :align: center

    Sometimes you are shown the following error message:
    ``Unable to submit the form. You are not authorized to server. Your session might have expired. Please refresh the browser window to re-login.``

    To fix this, please try:

    * **Hard Refresh & Clear State**: close the tab entirely, open a fresh Incognito / Private Browsing window (or clear your browser cache/cookies for myaccessid.org), and try the login flow again from scratch.
    * **Disable Extensions Temporarily**: Disable strict ad-blockers (like Firefox's Enhanced Tracking Protection or Brave's Shields), or third-party cookie blockers frequently break SAML/OIDC federated redirects between eduGAIN and MyAccessID. Disable them for the duration of the login.


* |egicheckin| `EGI-CheckIn <https://aai.egi.eu>`__: this is the path for users of specific projects (like iMagine).
  This is because Keycloak will automatically detect your EGI VO memberships
  (eg. ``vo.imagine-ai.eu``) and will grant your the proper platform full rights by default.

  .. dropdown:: ㅤ 💡 Open an |egicheckin| EGI Check-In account

    This mini tutorial is dedicated to users of the `iMagine project <https://imagine-ai.eu/>`__.

    To access this authentication level, go to the `EGI Check-In (prod) <https://aai.egi.eu/>`__
    and login preferably with your **institutional account** (university, research center).
    If this is not possible, please, use one of **Github** or **ORCID** but with the email
    domain which identifies your organization.
    This will automatically create your new account at EGI Check-In.

    Then you have to enroll in one of the Virtual Organizations (VO) supported by the project.
    Please :doc:`ask support </help/index>` for the request link of your Virtual Organization.

    When enrolling, you have to provide the following information in ``Comments``:

    * Reason to use the platform (e.g. use case)
    * Your institution or organization
    * How did you learn about the platform

    You will need to wait until you are **approved** before being a full member of the VO.


Additionally, we offer other options for first-time registration including:
|ifca| `IFCA SSO <https://sso.ifca.es>`__.

.. admonition:: Subsequent logins
   :class: info

   Since the platform aims at people registering with their institutional accounts, the
   :fab:`github` `Github <https://github.com/>`__ and
   :fab:`google` `Google <https://accounts.google.com/>`__ are **not allowed for first-time account creation**.
   This means that if you try to use them for registering a new account, you will be shown an error message similar to:

   ``We are sorry... User ***@gmail.com authenticated with identity provider google does not exist. Please contact your administrator.``

   So you will need to first create an account with one of the above options.
   However :fab:`github` `Github <https://github.com/>`__ and :fab:`google` `Google <https://accounts.google.com/>`__  are *allowed for subsequent logins*, as long as they share the **same institutional email with you initial identity provider**.
   
   So you can authenticate the first time with EduGain, then can subsequently authenticate with any other option (eg. Github), as long as they share the same email.
   If you prefer, you can also manually link your accounts in the `AI4EOSC Profile manager <https://login.cloud.ai4eosc.eu/realms/ai4eosc/account/#/account-security/linked-accounts>`__.

In summary, each authentication flow will grant different :doc:`user access levels </reference/user-access-levels>`.
In short:

* users coming from the of the supported projects will have **full access** level.
  Nevertheless they might start with *intermediate access* level at registration time (if no explicit membership from the institutional credentials to a project is in place) and will therefore need to ask to manually :ref:`upgrade their access level <reference/user-access-levels:Option 1. Being part of a supported project>`.

  .. include:: /snippets/supported-projects.rst

* user coming from |myaccessid| `EduGain <https://edugain.org/>`__ will have **intermediate access** level.
* remaining users (eg. |ifca| `IFCA SSO <https://sso.ifca.es>`__) will only have **basic access** level (observers).

We are also able to :ref:`upgrade the access level of selected users <reference/user-access-levels:Option 2. Make a special request>` with interesting usecases, even if they are not members of a selected project.


Login to the platform
---------------------

Once registered, you can directly head to the :ref:`Dashboard <dashboard>` page, login and check your :ref:`profile page <dashboard/profile:profile>` to see your access level.

.. image:: /_static/images/dashboard/profile/overview.png








.. |egicheckin| image-ori:: /_static/images/favicons/egicheckin.png
   :height: 1em
   :alt: Button icon
   :class: no-scaled-link

.. |myaccessid| image-ori:: /_static/images/favicons/myaccessid.png
   :height: 1em
   :alt: Button icon
   :class: no-scaled-link

.. |ifca| image-ori:: /_static/images/favicons/ifca.png
   :height: 1em
   :alt: Button icon
   :class: no-scaled-link

.. |ai4eosc| image-ori:: /_static/images/favicons/ai4eosc.png
   :height: 1em
   :alt: Button icon
   :class: no-scaled-link

.. |orcid| image-ori:: /_static/images/favicons/orcid.ico
   :height: 1em
   :alt: Button icon
   :class: no-scaled-link