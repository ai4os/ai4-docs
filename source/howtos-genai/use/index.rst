Use AI4EOSC GenAI assets
========================

This section will guide you through the process of using the GenAI assets (LLMs, MCPs, Agents) available in the AI4EOSC platform.

This includes both:

* **platform-wide assets**: those are assets that are publicly available to all users
* **user-specific assets**: those are the assets that you have :doc:`deployed yourself </howtos/deploy/index>`, for your private usage


.. grid:: 1
    :gutter: 3

    .. grid-item-card:: :fas:`comments;fa-lg sd-mr-2` Use via chat
        :link: chat
        :link-type: doc

        Access our user-friendly chat interface to talk to our LLMs and agents

    .. grid-item-card:: :fas:`plug;fa-lg sd-mr-2` Use via API
        :link: api
        :link-type: doc

        Generate your own API keys and use our OpenAI-compatible endpoint to integrate our assets into your services

    .. grid-item-card:: :fas:`terminal;fa-lg sd-mr-2` Use via Code Assistant
        :link: devenv
        :link-type: doc

        Use the code assistant integrate in the AI4EOSC development environment for a streamlined coding experience

.. toctree::
   :caption: Use a GenAI asset
   :maxdepth: 1
   :titlesonly:
   :hidden:

   Use via chat <chat>
   Use via API <api>
   Use via Code Assistant <devenv>

.. _genai_budget:

Budgets and rate limits
-----------------------

Each of the different methods to access GenAI assets will consume credits from your same single user pool.
Similarly, if you :doc:`create different API keys </howtos-genai/use/api>`, all keys will consume from that same budget.

Your budget and rate limits depends on your current :doc:`user access level </reference/user-access-levels>`.
Numbers are designed so that:

* Intermediate level users (``ap-a``, ``ap-a1``, ``ap-b``) should be able to :doc:`query models via chat </howtos-genai/use/chat>` without experiencing restrictions
* Full-access level users (``ap-u``, ``ap-d``) should be able to carry out most agentic workflows (via :doc:`chat </howtos-genai/use/chat>`, :doc:`API </howtos-genai/use/api>` or :doc:`development environment </howtos-genai/use/devenv>`) without experiencing restrictions, under reasonable use

.. admonition:: :fas:`scale-balanced;fa-lg sd-mr-2` Increasing your budget and limits
   :class: tip

   If you find that your current budget and rate limits are blocking your application development experience, please consider:

   * :ref:`upgrading your access level <reference/user-access-levels:upgrading your access level>`,
   * if you already have the maximum access level (``ap-u``), you might :doc:`ask support </help/index>` to have your individual limits increased further. In the contact form, please provide details on why your application needs higher limits.

.. container:: table-title

  *(TPM = Tokens Per Minute (input+output), RPM = Requests Per Minute)*

.. list-table::
  :header-rows: 1
  :align: center

  * - Group
    - Budget (credits) / day / user
    - TPM Limit / user
    - RPM Limit / user
  * - ap-a
    - 0.1
    - 20000
    - 5
  * - ap-a1
    - 0.2
    - 30000
    - 8
  * - ap-b
    - 0.3
    - 50000
    - 10
  * - ap-u
    - 3
    - 1000000
    - 50
  * - ap-d
    - 5
    - 1200000
    - 60

.. raw:: html

  <br/>


Your daily budget
^^^^^^^^^^^^^^^^^

Each time you make a call to an LLM or agent, you will be consuming your **daily** budget.
When you consume all your budget you will no longer be able to make further requests.
After each day, your budget will be reset and you will be able to make calls again.


Regarding user credits, each asset will consume a different amount of credits.
As a general rule of thumb:

* small models (like `Smol` or `OLMo`) consume around ``1e-8`` per input token and ``2e-8`` per output token.
* large models (like Mistral Small or Qwen 3) consume around ``1e-7`` per input token and ``3e-7`` per output token.
* embedding models (like Qwen3 Embeddings) consume around ``2e-8`` per input token.
* agents calls typically consume the same amount as the underlying model they use.
* MCP call typically do not consume credits.

You can use `OpenAI tokenizer <https://platform.openai.com/tokenizer>`__ to get a rough estimate of how a given text maps into tokens.


Your rate limits
^^^^^^^^^^^^^^^^

The above rate limits (Tokens Per Minute, Requests Per Minute) are enforced to ensure fair access to resources to all users.
If you exceed those limits, you will be returned an error similar to:

.. code::

  error 429: Rate limit exceeded for team_member: ap-d:********************. Limit type: tokens. Current limit: 150000, Remaining: 40169. Limit resets at: 2026-11-23 23:43:33 UTC"

and you will need to wait few minutes until your access is resumed.