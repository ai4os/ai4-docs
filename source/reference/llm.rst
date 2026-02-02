AI4OS LLM
=========

As part of the tool repertoire that the AI4OS stack is offering to increase our user's productivity, we are current offering an LLM Chatbot service that allows users to summarize information, get code recommendations, ask questions about the documentation, etc.

We care about user privacy, so it's important to notice that your chat history will be erased whenever you delete it, and no data will be retained by the platform (`privacy policy <https://ai4eosc.eu/platform/privacy-policy/>`__).

.. admonition:: Requirements
   :class: info

   🔓 You need a :doc:`platform account </getting-started/register>` with :ref:`basic access level <reference/user-access-levels:Basic access level>`.

AI4OS LLM vs self-deployed LLM
------------------------------

We also offer a :doc:`self-deployed LLM option </howtos/deploy/llm>`, so which one should you choose?

**Self-deployed LLM**

* available to :ref:`full access level <reference/user-access-levels:Full access level>` users
* let's you deploy a wide variety of models from a catalog,
* resources are exclusively dedicated to you and your selected coworkers,
* you are the admin, so you can configure model and UI parameters,
* you are the admin, so you can create your own `Knowledge Bases <https://docs.openwebui.com/features/workspace/knowledge/>`__ as persistent memory banks,
* you are the admin, so you can use `Functions <https://docs.openwebui.com/features/plugin/functions/>`__ to create your own agents that use custom prompts, custom Knowledge Bases, and custom input/output filtering,

**AI4OS LLM (platform wide)**

* available to all users (:ref:`basic access level <reference/user-access-levels:Basic access level>` and above)
* uses more powerful GPUs, so it offers bigger and more accurate LLMs,
* zero configuration needed, access directly with your :doc:`AI4OS credentials </getting-started/register>`,
* the backend (VLLM) is load balanced so it can offer lower latency,
* comes with some pre-configured helpful agents, like the :ref:`AI4EOSC Assistant <reference/llm:Ask questions about the documentation>` that helps you navigate the project's documentation,

By default, we recommend using the AI4OS LLM, which will offer a better experience for most users. Users with more custom needs should try nevertheless the self-deployment options.

Anyway, remember that both options are compatible: you can deploy your own LLM and still access the platform-wide one.
The best of both worlds! 🚀

Both options offer a **privacy-first** design: once your delete your chats or knowledge bases, the data is immediately wiped out from the platform.

Login
-----

Login into: https://chat.cloud.ai4eosc.eu

.. image:: /_static/images/llm/login.png


Once you login, you will arrive to a landing page where you will be able to select the model which you want to interact with.

.. image:: /_static/images/llm/landing.png

The current available models are:

* **Small**: a medium-size model from the `Mistral family <https://mistral.ai/>`__ (Mistral 3.1, 24B parameters).
  This is the default model.
* **Qwen 3**: a smaller model from the `Qwen family <https://huggingface.co/collections/Qwen/qwen3-67dd247413f0e2e4f653967f>`__ (14B parameters).
* **Assistant**: our custom model designed to :ref:`help you navigate our documentation <reference/llm:Ask questions about the documentation>`,

Now, let's explore some common usages of the tool. Keep in mind that the AI4OS LLM is built with `OpenWebUI <https://openwebui.com/>`__ so you always find further information in `their documentation <https://docs.openwebui.com/>`__.


Using the AI4OS LLM
-------------------

Chat with the LLM
^^^^^^^^^^^^^^^^^

We can ask generic questions to the model.

.. image:: /_static/images/llm/chat.png

Remember that if you answer relies on up-to-date information, you can always enable :material-outlined:`language;1.5em` ``Web search`` under the :material-outlined:`add_circle;1.5em` button.


Summarize a document
^^^^^^^^^^^^^^^^^^^^

Under the :material-outlined:`add_circle;1.5em` button, you can select :material-outlined:`upload_file;1.5em` ``Upload files``.
This will allow you to query a document with questions.

.. image:: /_static/images/llm/upload-files.png


Ask questions about the documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the upper left corner, you can select the ``AI4EOSC/Assistant`` model to ask questions about the platform. The LLM with use our documentation as knowledge base to provide truthful answers to your questions.

.. image:: /_static/images/llm/assistant.png


Use Vision models
^^^^^^^^^^^^^^^^^

In the model menu, select any model with the ``VISION`` tag. Then you will be able to upload images to the model and ask questions about them.
To upload an image click the :material-outlined:`add_circle;1.5em` and you will be offered the possibility of either :material-outlined:`add_a_photo;1.5em` ``Capture`` an image or :material-outlined:`upload_file;1.5em` ``Upload`` an image.

Here are some ideas on how to incorporate this into a scientific workflow:

.. dropdown:: :material-outlined:`lightbulb;1.5em` Detexify a LaTeX equation

   ``Generate latex code for the above picture and render it below.``

   .. figure:: /_static/images/llm/vision-detexify.png

.. dropdown:: :material-outlined:`lightbulb;1.5em` Digitize your handwritten notes

   ``Can you generate a Mermaid graph from this sketch? To ensure valid code, make sure that text inside boxes follows the format `letter{…}`. For example `B{Some text}`.``

   .. figure:: /_static/images/llm/vision-mermaid.png

Do you use it in other ways? `We are happy to hear! <https://community.cloud.ai4eosc.eu/>`__



Integrate it with your own services
-----------------------------------

You can access the LLM models via an OpenAI-compatible API for an easier integration with your own services.

.. admonition:: Requirements
   :class: info

   🔓 You need a :doc:`platform account </getting-started/register>` with :ref:`intermediate access level <reference/user-access-levels:Intermediate access level>` or above.

Retrieve the API endpoint/key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The API endpoint to query the models is:

  https://vllm.cloud.ai4eosc.eu

To generate the API keys go to the :ref:`Dashboard profile <dashboard_profile>`, to the ``Secrets and API keys`` section.
There you will be able to create a new API key selecting the name and the expiration date.

.. image:: /_static/images/llm/api-keys-dashboard.png

.. dropdown:: ㅤ ℹ️ Budgets and rate limits

  Each time you use an API key you will be consuming your **daily** budget.
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
      - 0.75
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

  * small models (like Smol or OLMo) consume around ``1e-8`` per input token and ``2e-8`` per output token.
  * large models (like Mistral Small or Qwen 3) consume around ``1e-7`` per input token and ``3e-7`` per output token.
  * embedding models (like Qwen3 Embeddings) consume around ``2e-8`` per input token.

  You can use `OpenAI tokenizer <https://platform.openai.com/tokenizer>`__ to get a rough estimate of how a given text maps into tokens.

Use it as a code assistant with VScode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It's very easy to use the AI4OS LLM as a code assistant, both locally and in :doc:`the AI4OS Development Environment </howtos/develop/dashboard>`.
To configure it:

1. In VScode, install the `Continue.dev <https://www.continue.dev/>`__ extension.
2. Open the Continue config file: ``/home/<user>/.continue/config.yaml``
3. Modify it to add the AI4OS LLM model, :ref:`using your API key <reference/llm:Retrieve the API endpoint/key>`:

  .. code-block:: yaml

      models:
        - name: AI4OS LLM
          provider: openai
          model: AI4EOSC/Small
          apiKey: "************************************"
          apiBase: https://vllm.cloud.ai4eosc.eu/
          roles:
            - chat
            - edit
            - apply

.. We use '"useLegacyCompletionsEndpoint": false' to force the usage of chat/completions instead of completions endpoint
.. ref: https://docs.continue.dev/customize/model-providers/openai

4. Voilá, you are done! Check the `Continue short tutorial <https://www.youtube.com/watch?v=V3Yq6w9QaxI>`__ for a quick overview on how to use it.

.. image:: /_static/images/llm/continue.png


Use it from within your Python code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To use the LLM from your Python scripts you need to install the `openai <https://github.com/openai/openai-python>`__ Python package.
Then you can use the LLM as following:


.. code-block:: python

    from openai import OpenAI


    client = OpenAI(
        base_url="https://vllm.cloud.ai4eosc.eu",
        api_key="************************************",
    )

    completion = client.chat.completions.create(
        model="AI4EOSC/Small",
        messages=[{"role": "user", "content": "What is the capital of France?"}]
    )

    print(completion.choices[0].message.content)


.. dropdown:: ㅤ ⚠️ Query token limit

  The models served have a typical token limit per call. If your query exceeds this token
  limit, you will get an error message similar to:

  .. code-block:: console

    BadRequestError: Error code: 400 - {'object': 'error', 'message': 'max_tokens must be at least 1, got -30979.', 'type': 'BadRequestError', 'param': None, 'code': 400}


Implement a RAG pipeline
^^^^^^^^^^^^^^^^^^^^^^^^

We also have a dedicated **embeddings model** that let's you perform Retrieval Augmented Generation (RAG).
This allows the model to ground its answers on the specific documents you pass to it.
You can implement a RAG pipeline using the `llama-index <https://www.llamaindex.ai/>`__ Python package, for example.

After installing the required packages,

.. code-block:: bash

  pip install llama-index
  pip install llama-index-llms-openai-like
  pip install llama-index-embeddings-openai-like

define your demo pipeline:

.. code-block:: python

  from llama_index.core import Settings, VectorStoreIndex, Document, SimpleDirectoryReader
  from llama_index.llms.openai_like import OpenAILike
  from llama_index.embeddings.openai_like import OpenAILikeEmbedding


  Settings.embed_model = OpenAILikeEmbedding(
      api_base="https://vllm.cloud.ai4eosc.eu",
      api_key="************************************",
      model_name="AI4EOSC/Qwen3-Embedding",
  )
  Settings.llm = OpenAILike(
      api_base="https://vllm.cloud.ai4eosc.eu",
      api_key="************************************",
      model="AI4EOSC/Small",
      context_window=25000,
      is_chat_model=True,
      is_function_calling_model=False,
  )

  # Simple document example 📄️
  text_to_embed = "My favorite fruit are apples."
  documents = [Document(text=text_to_embed)]

  # But you can also load entire document folders 📂️
  # documents = SimpleDirectoryReader(input_dir="/path/to/your/document/folder").load_data()

  # Build index and query engine
  index = VectorStoreIndex.from_documents(documents)
  query_engine = index.as_query_engine()

  # Ask the LLM a question
  response = query_engine.query("What is my favorite fruit?")
  print(response)

  # > Apples are your favorite fruit.
