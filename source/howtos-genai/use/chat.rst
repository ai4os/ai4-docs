Use GenAI assets via chat
=========================

The AI4EOSC GenAI chat is the simplest way to use all the GenAI services the AI4EOSC platform has to offer.
The services aim to assist researches during the whole research lifecycle from literature review to publication.

.. admonition:: Requirements
   :class: info

   🔓 You need a :doc:`platform account </getting-started/register>` with :ref:`intermediate access level <reference/user-access-levels:Intermediate access level>`.


Login
-----

Login into: https://genai.dev.ai4eosc.eu/

.. image:: /_static/images/genai-ui/login.png


Once you login, you will arrive to a landing page where you will be able to select the model which you want to interact with.

.. image:: /_static/images/genai-ui/landing.png

On the left panel, you can see the history of your conversations, with options to delete past conversations.
We care about user privacy, so it's important to notice that your chat history (and attached documents) will be completely erased as soon as you delete it, and no data will be retained by the platform (see `our privacy policy <https://ai4eosc.eu/platform/privacy-policy/>`__).


Using the LLMs
--------------

Model catalog
^^^^^^^^^^^^^
The AI4EOSC LLM catalog is always evolving, as we are constantly deploying newer, better and more efficient models. We typically serve open-source/open-weights models from
the `Mistral family <https://mistral.ai/>`__,
the `Qwen family <https://huggingface.co/collections/Qwen/qwen3-67dd247413f0e2e4f653967f>`__,
the `Gemma family <https://huggingface.co/google>`__,
the `DeepSeek family <https://huggingface.co/deepseek-ai>`__,
the `Minimax family <https://huggingface.co/MiniMaxAI>`__,
etc.

Each model comes with its own model card.

.. image:: /_static/images/genai-ui/llm-details.png
   :width: 600 px

The card provides information like:

* **model capabilities**: including whether the model support chain-of-thought, tools, or has vision capabilities.
* **token cost**: how much chatting with the each models actually costs (see :ref:`budget information <genai_budget>`)
* **status**: whether the model is currently reachable or not

In addition to standard chatting, the UI offers the following features.

Upload files to the conversation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Under the :material-outlined:`add_circle;1.5em` button, you can select :material-outlined:`upload_file;1.5em` ``Upload files``.
This will allow you to query a document with questions.

.. image:: /_static/images/genai-ui/file-upload.png

If the model supports vision, you can also upload images.
Under the :material-outlined:`add_circle;1.5em` button, you can select :material-outlined:`photo;1.5em` ``Add image``.

Here are some ideas on how to incorporate this into a scientific workflow:

.. dropdown:: :material-outlined:`lightbulb;1.5em` Detexify a LaTeX equation

   ``Generate latex code for the above equation and render it below.``

   .. image:: /_static/images/genai-ui/vision-detexify.png

.. dropdown:: :material-outlined:`lightbulb;1.5em` Digitize your handwritten notes

   ``Can you generate a Mermaid graph from this sketch? To ensure valid code, make sure that text inside boxes follows the format `letter{…}`. For example `B{Some text}`.``

   .. image:: /_static/images/genai-ui/vision-mermaid.png

Do you use vision capabilities in other ways? `We are happy to hear! <https://community.cloud.ai4eosc.eu/>`__

Use AI4EOSC public knowledge bases
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On the right panel, you are shown all the public knowledge collections that AI4EOSC offers to users. Those collections form the knowledge base that the different AI4EOSC agents leverage to provide useful answers to users.

Select a particular collection so that you questions to the LLM are grounded on the documents contained in that collection:

.. image:: /_static/images/genai-ui/knowledge-public.png

Clicking on a particular collection will show you what are the documents that are part of that collection.

.. image:: /_static/images/genai-ui/knowledge-files.png
   :width: 500 px

Create your private knowledge base
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In addition to public collections, you can create your private ones. For this, on the right panel, click on :material-outlined:`add_circle;1.5em` ``Create collection``. This will open a small window to create the collection:

.. image:: /_static/images/genai-ui/knowledge-creation.png
   :width: 500 px

Then you can clik again on the newly created collection, and a new window will pop up where you will be able to upload documents:

.. image:: /_static/images/genai-ui/knowledge-upload.png
   :width: 500 px

Then, with the collection selected, you will be able to query your LLM grounding the responses on the documents contained in that selection:


.. image:: /_static/images/genai-ui/knowledge-private.png


Using generalist agents
-----------------------

AI4EOSC generalist agents are meant for cross-cutting tasks that are not necessarily part of the scientific research process. They aim to provide general-purpose assistance, such as answering questions, searching the web, and navigating AI4EOSC documentation.

Each agent comes with each own agent card.

.. image:: /_static/images/genai-ui/agent-details.png
   :width: 600 px

The card provides information like:

* **description**: brief description of the agent capabilities, along with relevant tags.
* **token cost**: how much chatting with the each agent actually costs (see :ref:`budget information <genai_budget>`)
* **status**: the current development status of each agent: ``beta`` for very preliminary agents only accessible to developers, ``alpha`` for agents that are released to internal users and ``production`` is used for stable agent open to the general public.

Default
^^^^^^^
The ``default`` agent is a central entry point for the AI4EOSC agent ecosystem. It understands user requests and brings together the most relevant specialized agents to find information, perform research, and solve complex tasks.

.. image:: /_static/images/genai-ui/agents-default.png

Web search
^^^^^^^^^^
The ``web-search`` research assistant helps with finding up-to-date and verifiable information. It searches across multiple sources and search engines to investigate complex questions, verify facts, and provide answers grounded in current online information.

.. image:: /_static/images/genai-ui/agents-web.png

AI4EOSC Documentation Assistant
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The ``documentation-assistant`` is an intelligent guide to the AI4EOSC ecosystem. It navigates the available documentation to help the AI4EOSC community understand how the platform works, providing answers grounded in official AI4EOSC resources.

.. image:: /_static/images/genai-ui/agents-docs.png

Using scientific agents
-----------------------

The AI4EOSC agents aim to assist scientists during the whole research lifecycle. Those currently include the following agents.

Literature review
^^^^^^^^^^^^^^^^^
The ``literature-review`` agent acts as an agentic research fellow for the scientific community. It continuously explores papers from `arXiv <https://arxiv.org/>`__, `DIGITAL.CSIC <https://digital.csic.es/>`__ and `HAL <https://hal.science/>`__ to discover relevant literature with verified sources.

.. image:: /_static/images/genai-ui/agents-literature.png

Dataset search
^^^^^^^^^^^^^^
The ``dataset-search`` is a conversational gateway to public scientific datasets. It helps discover government datasets, retrieve relevant information, and explore data published by official French sources (`Data Gouv <https://www.data.gouv.fr/>`__), and scientific datasets published in `DIGITAL.CSIC <https://digital.csic.es/>`__.

.. image:: /_static/images/genai-ui/agents-datasets.png
