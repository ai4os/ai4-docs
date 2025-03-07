Deploy your own LLM chatbot
===========================

.. admonition:: Requirements
   :class: info

   🔒 This tutorial requires :ref:`full authentication <getting-started/register:Full authentication>`.


In this tutorial, we will guide you on how to deploy your own LLM instance in the AI4OS Platform.

For the moment, due to resource constraints, this tool allows to deploy only small LLMs that can fit in NVIDIA T4s.
If you want to use bigger LLMs on faster resources, please :doc:`use the AI4OS LLM </reference/llm>`!

Deploying the LLM
-----------------

The LLM Chatbot is located at the top of the :ref:`Marketplace <dashboard_marketplace>`, in the ``Tools`` section.

The workflow for deploying the LLM is similar to the one for :doc:`deploying a module </reference/dashboard>`.
In this particular case, during the LLM configuration phase you will need to pay attention to:

* ``type``: choose what to you want to deploy. Options are:

  - ``both``: deploy both the backend and the UI,
  - ``vllm``: deploy only the backend,
  - ``open-webui``: deploy only the UI,

* ``LLM model`` this is the particular model you want to deploy.

  For the time being, due to limitations in resources (deployments are made in NVIDIA T4s) we only support small models (eg. `DeepSeek-R1-Distill-Qwen-1.5B <https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B>`__) or medium models that have been quantized (eg. `Qwen2.5-7B-Instruct-AWQ <https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-AWQ>`__).

  Medium-size quantized models are usually more accurate although they can have slightly slower inference speeds (due to the de-quantization process). We recommend using those.

  Among the catalog of models we provide, there are models specialized in solving coding tasks or maths problems.

* ``UI email``, ``UI password``: these are the credentials to log to the UI.
  By default, we use your user email from the platform.

* (Optional) ``HF token``: Using some models might require that you provide a valid HuggingFace token to deploy.

  For example, to use `LLama models <https://huggingface.co/meta-llama>`__ you must login to HuggingFace and accept their terms and conditions. Once this is done, you can `generate a token in Huggingface <https://huggingface.co/docs/hub/security-tokens>`__ to use it in our platform.

* (Optional) ``API key/url``: if you choose to deploy only the UI, you must provide the endpoint and key of an OpenAI compatible endpoint, that the UI can connect to.

Using the LLM
-------------


In the :ref:`deployments list <dashboard-manage-deployments>` you will be able to see your newly created LLM instance.
Clicking the ``Quick access`` button, you will directly enter the Open-WebUI login screen.

.. image:: /_static/images/endpoints/openwebui-login.png

The enter you ``UI email``  and ``UI password`` and voilá, you're in!

.. image:: /_static/images/endpoints/openwebui-landing.png

You are the admin of the instance, so you can create new users for other people in your team.

Go to the `Open-WebUI documentation <https://openwebui.com/>`__ to further configure your instance.
For example, you can:

* customize the UI appearance: since current models do not have vision capabilities, so you can disable image upload for users going to :material-outlined:`account_circle;1.5em` ``Admin Panel`` → ``Settings`` → ``Models`` → ``<model-name>`` → ``Capabilities`` → :material-outlined:`check_box;1.5em` ``Vision``
* create your own `Knowledge Bases <https://docs.openwebui.com/features/workspace/knowledge/>`__ as persistent memory banks,
* use `Functions <https://docs.openwebui.com/features/plugin/functions/>`__ to create your own agents that use custom prompts, custom Knowledge Bases, and custom input/output filtering,