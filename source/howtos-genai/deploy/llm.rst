Deploy your own LLM chatbot
===========================

.. admonition:: Requirements
   :class: info

   🔒 You need a :doc:`platform account </getting-started/register>` with :ref:`full access level <reference/user-access-levels:Full access level>`.


In this tutorial, we will guide you on how to deploy your own LLM instance in the platform.

For the moment, due to resource constraints, this tool allows to deploy only small LLMs that can fit in NVIDIA T4s.

.. dropdown:: 🤔 Platform LLM *vs* self-deployed LLM

  We also offer a :ref:`platform-wide LLMs <dashboard/catalog:llms>` (accessible via its own :doc:`chat interface </howtos-genai/use/chat>`) in addition to this self-deployed option.
  Sp which one should you use?

  **Self-deployed LLM**

  * available to :ref:`full access level <reference/user-access-levels:Full access level>` users
  * let's you deploy a wide variety of models from a catalog,
  * resources are exclusively dedicated to you and your selected coworkers,
  * you are the admin, so you can configure model and UI parameters,
  * you are the admin, so you can create your own `Knowledge Bases <https://docs.openwebui.com/features/workspace/knowledge/>`__ as persistent memory banks,
  * you are the admin, so you can use `Functions <https://docs.openwebui.com/features/plugin/functions/>`__ to create your own agents that use custom prompts, custom Knowledge Bases, and custom input/output filtering,

  **Platform LLM**

  * available to all users (:ref:`basic access level <reference/user-access-levels:Basic access level>` and above)
  * uses more powerful GPUs, so it offers bigger and more accurate LLMs,
  * zero configuration needed, access directly with your :doc:`credentials </getting-started/register>`,
  * the backend (VLLM+LiteLLM) is load balanced so it can offer lower latency,
  * comes with some pre-configured helpful agents, like the :ref:`Documentation Assistant <howtos-genai/use/chat:documentation assistant>` that helps you navigate the project's documentation,

  By default, we recommend using the platform LLM, which will offer a better experience for most users. Users with more custom needs should try nevertheless the self-deployment options.

  Anyway, remember that both options are compatible: you can deploy your own LLM and still access the platform-wide one.
  The best of both worlds! 🚀

  Both options offer a **privacy-first** design: once your delete your chats or knowledge bases, the data is immediately wiped out from the platform.


Deploying the LLM
-----------------

In the :ref:`Dashboard Marketplace <dashboard_marketplace>`, go to the **LLM catalog** and click on the model card you want to deploy.
Alternatively, you can go to:  **Tools catalog** → **Deploy your LLM** → **Deploy**.

Once  in the configuration page, the workflow for deploying the LLM is similar to the one for :doc:`deploying a module </dashboard/deployments>`.
In this particular case, during the LLM configuration phase you will need to pay attention to:

* ``type``: choose what to you want to deploy. Options are:

  - ``both``: deploy both the backend and the UI,
  - ``vllm``: deploy only the backend,
  - ``open-webui``: deploy only the UI,

* ``LLM model`` this is the particular model you want to deploy.

  .. dropdown:: ㅤ 💡 What is the best model for my needs?

    For the time being, due to limitations in resources (deployments are made in NVIDIA T4s) we only support small models (eg. `DeepSeek-R1-Distill-Qwen-1.5B <https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B>`__) or medium models that have been quantized (eg. `Qwen2.5-7B-Instruct-AWQ <https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-AWQ>`__).

    Medium-size quantized models are usually more accurate although they can have slightly slower inference speeds (due to the de-quantization process). We recommend using those.

    Among the catalog of models we provide, there are models specialized in solving coding tasks or maths problems, so depending on your usecase you might want to select those.

* ``UI email``, ``UI password``: these are the credentials to log to the UI.
  By default, we use your user email from the platform.

* *(Optional)* ``HF token``: Using some models might require that you provide a valid HuggingFace token to deploy.
  For example, to use `LLama models <https://huggingface.co/meta-llama>`__ you must login to HuggingFace and accept their terms and conditions. Once this is done, you can  :ref:`link HuggingFace in the Dashboard <dashboard/profile:Linked services>` to use Llama models in our platform.

* *(Optional)* ``API key/url``: if you choose to deploy only the UI, you must provide the endpoint and key of an OpenAI compatible endpoint, that the UI can connect to.

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
* :doc:`integrate the model with your own services </howtos-genai/use/api>` (use as code assistant in VSCode, use from Python scripts, etc).
