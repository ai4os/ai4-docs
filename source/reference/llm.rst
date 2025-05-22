AI4OS LLM
=========

As part of the tool repertoire that the AI4OS stack is offering to increase our user's productivity, we are current offering an LLM Chatbot service (*in beta!*) that allows users to summarize information, get code recommendations, ask questions about the documentation, etc.

We care about user privacy, so it's important to notice that your chat history will be erased whenever you delete it, and no data will be retained by the platform (`privacy policy <https://ai4eosc.eu/platform/privacy-policy/>`__).


AI4OS LLM vs self-deployed LLM
------------------------------

We also offer a :doc:`self-deployed LLM option </howtos/deploy/llm>`, so which one should you choose?

**Self-deployed LLM**

* let's you deploy a wide variety of models from a catalog,
* resources are exclusively dedicated to you and your selected coworkers,
* you are the admin, so you can configure model and UI parameters,
* you are the admin, so you can create your own `Knowledge Bases <https://docs.openwebui.com/features/workspace/knowledge/>`__ as persistent memory banks,
* you are the admin, so you can use `Functions <https://docs.openwebui.com/features/plugin/functions/>`__ to create your own agents that use custom prompts, custom Knowledge Bases, and custom input/output filtering,

**AI4OS LLM (platform wide)**

* uses more powerful GPUs, so it offers bigger and more accurate LLMs,
* zero configuration needed, access directly with your :doc:`AI4OS credentials </getting-started/register>`,
* the backend (VLLM) is load balanced so it can offer lower latency,
* has a dedicated RAG instance for faster queries,
* comes with some pre-configured helpful agents, like the :ref:`AI4EOSC Assistant <reference/llm:Ask questions about the documentation>` that helps you navigate the project's documentation,

By default, we recommend using the AI4OS LLM, which will offer a better experience for most users. Users with more custom needs should try nevertheless the self-deployment options.

Anyway, remember that both options are compatible: you can deploy your own LLM and still access the platform-wide one.
The best of both worlds! 🚀

Both options offer a **privacy-first** design: once your delete your chats or knowledge bases, the data is immediately wiped out from the platform.


Login
-----

The service is available at: https://llm.dev.ai4eosc.eu

To access the LLM service, you first need to :ref:`register in the platform <getting-started/register:AI4OS account>`.

.. image:: /_static/images/llm/login.png


Once you login, you will arrive to a landing page where you will be able to select the model which you want to interact with.

.. image:: /_static/images/llm/landing.png

The current available models are:

* ``Small-2409``: a medium-size model from the `Mistral family <https://mistral.ai/>`__ (22B parameters) with a smaller context window (32K tokens), released on September 2024.
  This is the **default** model.
* ``DeepSeek-R1-Distill-Llama-8B``: a small distillation (8B parameters) of the `original DeepSeek R1 model <https://huggingface.co/deepseek-ai/DeepSeek-R1>`__, released on January 2025.
  The distillation is nowhere as performant as the original model, but it serves a nice demo of a thinking model.
* ``Assistant``: our custom model designed to :ref:`help you navigate our documentation <reference/llm:Ask questions about the documentation>`,
* ``Qwen2.5-VL-7B-Instruct``: a small model for vision related tasks, released in August 2024.

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

.. important::

    This service is currently under development, so it might not be accessible to you.

In the upper left corner, you can select the ``AI4EOSC/Assistant`` model to ask questions about the platform. The LLM with use our documentation as knowledge base to provide truthful answers to your questions.

.. image:: /_static/images/llm/assistant.png


Use Vision models
^^^^^^^^^^^^^^^^^

If you select the ``Qwen2.5-VL-7B-Instruct``, you can upload images to the model and ask questions about them.
To upload an image click the :material-outlined:`add_circle;1.5em` and you will be offered the possibility of either :material-outlined:`add_a_photo;1.5em` ``Capture`` an image or :material-outlined:`upload_file;1.5em` ``Upload`` an image.

Here are some ideas on how to incorporate this into a scientific workflow:

.. dropdown:: :material-outlined:`lightbulb;1.5em` Detexify a LaTeX equation

   ``Generate latex code for the above picture and render it below.``

   .. figure:: /_static/images/llm/vision-detexify.png

.. dropdown:: :material-outlined:`lightbulb;1.5em` Digitize your handwritten notes

   ``Can you generate a Mermaid graph from this sketch? To ensure valid code, make sure that text inside boxes follows the format `letter{…}`. For example `B{Some text}`.``

   .. figure:: /_static/images/llm/vision-mermaid.png

Do you use it in other ways? `We are happy to hear! <https://github.com/ai4os/ai4-docs/issues/new>`__



Integrate it with your own services
-----------------------------------

Retrieve the API endpoint/key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To integrate LLM completions into your workflow you need an API endpoint and an API key.
There are two API options:

* **vLLM API** (:material-outlined:`verified;1.5em` *recommended*): faster (load balanced), supports chat completions

  - **API endpoint**: https://llm.dev.ai4eosc.eu:8000.
  - **API key**: `AI4EOSC Keycloak <https://login.cloud.ai4eosc.eu/realms/ai4eosc/account>`__ → ``Personal Info`` → ``User metadata`` → ``LLM API key``

  .. figure:: /_static/images/llm/api-keys-keycloak.png
     :width: 500 px

* **OpenWebUI API**: supports chat completions, supports Retrieval Augmented Generation

  - **API endpoint**: https://llm.dev.ai4eosc.eu/api
  - **API key**: `AI4OS LLM <https://llm.dev.ai4eosc.eu>`__ → :material-outlined:`account_circle;1.5em` → :material-outlined:`settings;1.5em` ``Settings`` → :material-outlined:`account_circle;1.5em` ``Account``

  .. figure:: /_static/images/llm/api-keys-openwebui.png
     :width: 500 px

`Learn more <https://docs.openwebui.com/getting-started/advanced-topics/api-endpoints/>`__ on how to use API keys to integrate the AI4OS LLM into your own services (endpoints are compatible with the OpenAI API spec).

Use it as a code assistant with VScode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It's very to use the AI4OS LLM as a code assistant, both locally and in :doc:`the AI4OS Development Environment </howtos/develop/dashboard>`.
To configure it:

1. In VScode, install the `Continue.dev <https://www.continue.dev/>`__ extension.
2. On the left handside bar, click the Continue icon. Then, in the panel, click the ⚙️ ``Open Continue Config``.
3. Modify the ``config.json`` to add the AI4OS LLM model, :ref:`using your API key <reference/llm:Retrieve the API endpoint/key>`:

   .. code-block:: json

     {
        "models": [
            {
            "title": "AI4OS LLM",
            "provider": "openai",
            "model": "AI4EOSC/DeepSeek-R1-Distill-Llama-8B",
            "apiKey": "sk-********************************",
            "apiBase": "https://llm.dev.ai4eosc.eu/api",
            "useLegacyCompletionsEndpoint": false
            }
        ]
     }

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
        base_url="https://llm.dev.ai4eosc.eu/api",
        api_key="******************",
    )

    completion = client.chat.completions.create(
        model="AI4EOSC/Small",
        messages=[{"role": "user", "content": "What is the capital of France?"}]
    )

    print(completion.choices[0].message.content)