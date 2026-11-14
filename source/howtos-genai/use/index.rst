Use AI4EOSC GenAI assets
^^^^^^^^^^^^^^^^^^^^^^^^

This section will guide you through the process of using the GenAI assets (LLMs, MCPs, Agents) available in the AI4EOSC platform.

This includes both:

* **platform-wide assets**: those are assets that are publicly available to all users
* **user-specific assets**: those are the assets that you have :doc:`deployed yourself </howtos/deploy/index>`, for your private usage


.. _genai_budget:

.. dropdown:: ㅤ ℹ️ Budgets and rate limits

  Each time you make a call to an LLM or agent, you will be consuming your **daily** budget.
  When you consume all your budget you will no longer be able to make further requests.
  After each day, your budget will be reset and you will be able to make calls again.

  If you create different keys, both keys will consume the same budget.

  Your budget depends on your current :doc:`user access level </reference/user-access-levels>`.

  .. container:: table-title

    *(TPM = Tokens Per Minute, RPM = Requests Per Minute)*

  .. list-table::
    :header-rows: 1
    :align: center

    * - Group
      - Budget (credits) / day / user
      - TPM Limit / user
      - RPM Limit / user
    * - ap-a
      - 0.05
      - 1000
      - 2
    * - ap-a1
      - 0.075
      - 1500
      - 2
    * - ap-b
      - 0.1
      - 2000
      - 2
    * - ap-u
      - 1
      - 20000
      - 20
    * - ap-d
      - 1.5
      - 30000
      - 30

  .. raw:: html

    <br/>

  Each model will consume a different amount of resources.
  As a general rule of thumb:

  * small models (like `Smol` or `OLMo`) consume around ``1e-8`` per input token and ``2e-8`` per output token.
  * large models (like Mistral Small or Qwen 3) consume around ``1e-7`` per input token and ``3e-7`` per output token.
  * embedding models (like Qwen3 Embeddings) consume around ``2e-8`` per input token.

  You can use `OpenAI tokenizer <https://platform.openai.com/tokenizer>`__ to get a rough estimate of how a given text maps into tokens.

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
