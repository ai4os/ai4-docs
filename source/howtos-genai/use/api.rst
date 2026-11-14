Use GenAI assets via API
========================

You can access the GenAI assets (LLMs/MCPs/Agents) via an OpenAI-compatible API for an easier integration with your own services.

.. admonition:: Requirements
   :class: info

   🔓 You need a :doc:`platform account </getting-started/register>` with :ref:`intermediate access level <reference/user-access-levels:Intermediate access level>` or above.

To prevent name changes from breaking user workflows, we serve some persistent model names, namely ``AI4EOSC/default`` (for chat completions) and ``AI4EOSC/default-embeddings`` (to generate embeddings). Those aliases will point always to the latest models.

Retrieve the API credentials
----------------------------

The API endpoint to query the models is:

  https://vllm.cloud.ai4eosc.eu

To generate the API keys go to the :ref:`Dashboard profile <dashboard/profile:API keys>`.
There you will be able to create a new API key selecting the name and the expiration date.

Use it as a code assistant with VScode
--------------------------------------

It's very easy to use the LLM as a code assistant, both locally and in :doc:`the Development Environment </howtos/develop/dashboard>`.
To configure it:

1. In VScode, install the `Continue.dev <https://www.continue.dev/>`__ extension.
2. Open the Continue config file: ``/home/<user>/.continue/config.yaml``
3. Modify it to add the LLM model, :ref:`using your API key <howtos-genai/use/api:retrieve the api credentials>`:

  .. code-block:: yaml

      models:
        - name: AI4EOSC LLM
          provider: openai
          model: AI4EOSC/default  # or manually select you model
          apiKey: "sk-************************************"
          apiBase: https://vllm.cloud.ai4eosc.eu/
          roles:
            - chat
            - edit
            - apply

.. We use '"useLegacyCompletionsEndpoint": false' to force the usage of chat/completions instead of completions endpoint
.. ref: https://docs.continue.dev/customize/model-providers/openai

4. Voilá, you are done! Check the `Continue short tutorial <https://www.youtube.com/watch?v=V3Yq6w9QaxI>`__ for a quick overview on how to use it.

.. image:: /_static/images/endpoints/continue.png


Use it from within your Python code
-----------------------------------

To use the LLM from your Python scripts you need to install the `openai <https://github.com/openai/openai-python>`__ Python package.
Then you can use the LLM as following:


.. code-block:: python

    from openai import OpenAI


    client = OpenAI(
        base_url="https://vllm.cloud.ai4eosc.eu",
        api_key="sk-************************************",
    )

    completion = client.chat.completions.create(
        model="AI4EOSC/default",  # or manually select you model
        messages=[{"role": "user", "content": "What is the capital of France?"}]
    )

    print(completion.choices[0].message.content)


.. dropdown:: ㅤ ⚠️ Query token limit

  The models served have a typical token limit per call. If your query exceeds this token
  limit, you will get an error message similar to:

  .. code-block:: console

    BadRequestError: Error code: 400 - {'object': 'error', 'message': 'max_tokens must be at least 1, got -30979.', 'type': 'BadRequestError', 'param': None, 'code': 400}


Implement a RAG pipeline
------------------------

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
      api_key="sk-************************************",
      model_name="AI4EOSC/default-embeddings",  # or manually select you model
  )
  Settings.llm = OpenAILike(
      api_base="https://vllm.cloud.ai4eosc.eu",
      api_key="sk-************************************",
      model="AI4EOSC/default",  # or manually select you model
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
