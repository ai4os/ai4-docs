AI4OS LLM
=========

As part of the tool repertoire that the AI4OS stack is offering to increase our user's productivity, we are current offering an LLM Chatbot service (*in beta!*) that allows users to summarize information, get code recommendations, ask questions about the documentation, etc.

We care about user privacy, so it's important to notice that your chat history will be erased whenever you delete it, and no data will be retained by the platform (`privacy policy <https://ai4eosc.eu/platform/privacy-policy/>`__).

Login
-----

The service is available at: https://llm.dev.ai4eosc.eu

To access the LLM service, you first need to :ref:`register in the platform <getting-started/register:AI4OS account>`.

.. image:: /_static/images/llm/login.png


Once you login, you will arrive to a landing page where you will be able to select the model which you want to interact with.

.. image:: /_static/images/llm/landing.png

The current available models are:

* ``Nemo-2407``: a small-size model from the `Mistral family <https://mistral.ai/>`__ (12B parameter) with a large context window (128K tokens), released on July 2024,
* ``Small-2409``: a medium-size model from the `Mistral family <https://mistral.ai/>`__ (22B parameters) with a smaller context window (32K tokens), released on September 2024,
* ``Assistant``: our custom model designed to :ref:`help you navigate our documentation <reference/llm:Ask questions about the documentation>`,

Now, let's explore some common usages of the tool. Keep in mind that the AI4OS LLM is built with `OpenWebUI <https://openwebui.com/>`__ so you always find further information in `their documentation <https://docs.openwebui.com/>`__.


Chat with the LLM
-----------------

We can ask generic questions to the model.

.. image:: /_static/images/llm/chat.png

Remember that if you answer relies on up-to-date information, you can always enable :material-outlined:`language;1.5em` ``Web search`` under the :material-outlined:`add_circle;1.5em` button.


Summarize a document
--------------------

Under the :material-outlined:`add_circle;1.5em` button, you can select :material-outlined:`upload_file;1.5em` ``Upload files``.
This will allow you to query a document with questions.

.. image:: /_static/images/llm/upload-files.png


Ask questions about the documentation
-------------------------------------

.. important::

    This service is currently under development, so it might not be accessible to you.

In the upper left corner, you can select the ``AI4EOSC/Assistant`` model to ask questions about the platform. The LLM with use our documentation as knowledge base to provide truthful answers to your questions.

.. image:: /_static/images/llm/assistant.png


Integrate it with your own services
-----------------------------------

Under :material-outlined:`account_circle;1.5em` → :material-outlined:`settings;1.5em` ``Settings`` → :material-outlined:`account_circle;1.5em` ``Account`` you will be able to generate your own API keys to access the service. `Learn more <https://docs.openwebui.com/getting-started/advanced-topics/api-endpoints/>`__ on how to use API keys to integrate the AI4OS LLM into your own services.

.. image:: /_static/images/llm/api-keys.png
