AI4OS Access Policies
=====================

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

Our access levels are aligned with the `EOSC EU Node Access Levels <https://open-science-cloud.ec.europa.eu/about/access-policy>`__ (Observer, Explorer, Collaborator and Investigator).

Depending how your :doc:`registration credentials </getting-started/register>`, you will be granted a particular access level.
Each level gives access to a set of AI4OS services.
Each level includes access to the services of the previous levels.

AI4OS access levels
-------------------

Non-registered users
^^^^^^^^^^^^^^^^^^^^
.. card::

    Non-registered anonymous users are able to:

    * :ref:`Browse our public catalog of services <reference/dashboard:Navigating the Marketplace>`
    * `Browse our educational materials <https://www.youtube.com/@ai4eosc>`__
    * `Browse our open-source software <https://github.com/ai4os>`__

Basic access level
^^^^^^^^^^^^^^^^^^
.. card::

    Registered users with basic access level (``ap-0``) can:

    * :doc:`Deploy an AI model in their own cloud </howtos/deploy/cloud>`

    **Granted to**: any registered user (e.g. via :fab:`github` `Github <https://github.com/>`__,
    :fab:`google` `Google <https://accounts.google.com/>`__,
    |ifca| `IFCA SSO <https://sso.ifca.es>`__ and
    |orcid| `ORCID <https://orcid.org/>`__.
    )

Intermediate access level
^^^^^^^^^^^^^^^^^^^^^^^^^
.. card::

    Registered users with intermediate access level can:

    * :doc:`Try an AI model in the Dashboard </howtos/try/index>`
    * :doc:`Chat with the AI4OS LLM </reference/llm>`

    **Granted to**: researchers with |myaccessid| `EduGain <https://edugain.org/>`__ credentials.
    More finegrained permissions are granted based on membership:

    * ``ap-a``: any person with EduGain credentials
    * ``ap-a1``: any person with EduGain credentials that is employed by an organization
    * ``ap-b``: any person with EduGain credentials that is an employed researcher

Full access level
^^^^^^^^^^^^^^^^^

.. card::

    Registered users with full access level can use all the features the AI4OS stack
    has to offer, including:

    * :doc:`Developing AI models in the Dashboard </howtos/develop/index>`
    * :doc:`Training AI models in the Dashboard </howtos/train/index>`
    * :doc:`Deploying AI models in production </howtos/deploy/index>`
    * :doc:`Accessing the AI4OS storage </reference/storage>`

    **Granted to**: This access level is usually reserved to developers (``ap-d``) or members of one of the supported projects (``ap-u``):

    * `AI4EOSC <https://ai4eosc.eu/>`__: AI for the European Open Science Cloud
    * `iMagine <https://imagine-ai.eu/>`__: Imaging data and services for aquatic science
    * `AI4Life <https://ai4life.eurobioimaging.eu/>`__: AI models and methods for the life sciences


Upgrading your access level
---------------------------

Any user is, in principle, candidate to upgrade to full access.
There are two main entrypoints to full access:

Option 1. Join a supported project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Members of the following projects get full access level:

* `AI4EOSC <https://ai4eosc.eu/>`__: AI for the European Open Science Cloud
* `iMagine <https://imagine-ai.eu/>`__: Imaging data and services for aquatic science
* `AI4Life <https://ai4life.eurobioimaging.eu/>`__: AI models and methods for the life sciences

Consider joining these projects via their *Open calls for external usecases*.
More information about the calls can be found in their respective project's homepages.

Option 2. Make a special requests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sometimes joining a project is a lengthy process.
We are also able to upgrade user access level case by case. Feel free to :doc:`contact support </help/index>` explaining why would you need full access and what do you plan to do with it.
Due to the limited amount of resources, the team will carefully study your request before granting you full access.

.. admonition:: Credit system
   :class: info

   In order to improve the management of compute resources, we are in the process to adopt a credit system, thus fully aligning with the  `EOSC EU Node Access Policies <https://open-science-cloud.ec.europa.eu/about/access-policy>`__.
   Stay tuned!
