AI4EOSC Code assistant
======================

We have integrated the :ref:`platform LLMs <dashboard/catalog:llms>` into :ref:`development environment <howtos/develop/dashboard:2. prepare your development environment>`.
This should help users to streamline the model development.

There are currently three options to use Code Assistants in the development environment, all leveraging `OpenCode <https://opencode.ai/>`__.
All three come automatically preconfigured to use the platform LLMs, so no configuration setup is needed from the user.

Using within VScode
-------------------

When :ref:`configuring the deployment <dashboard/deployments:general configuration>`, select the ``VScode`` option.

The code assistant will be available from inside VScode with the `OpenChamber extension <https://marketplace.visualstudio.com/items?itemName=FedaykinDev.openchamber>`__.
To enable the extension, you have to trust the workspace:

* ``Restricted Mode is intended for safe code browsing. Trust this folder to enable all features.`` → ``Manage`` → ``Trust``

Then a small green cube will appear in the top right corner. Click it to open a session.

.. image:: /_static/images/endpoints/vscode-openchamber-open.png

Then start chatting about your new project:

.. image:: /_static/images/endpoints/vscode-openchamber-session.png


Using within JupyterLab
-----------------------

When :ref:`configuring the deployment <dashboard/deployments:general configuration>`, select the ``JupyterLab`` option.

Then open a terminal to start using OpenCode:

.. image:: /_static/images/endpoints/jupyter-opencode.png


Using within OpenCode Web UI
----------------------------

When :ref:`configuring the deployment <dashboard/deployments:general configuration>`, select the ``OpenCode`` option.

In the login window, select the ``Use password`` option and input the password you selected at configuration time:

.. image:: /_static/images/endpoints/opencode-login.png
   :width: 300 px
   :align: center


Then start chatting about your new project:

.. image:: /_static/images/endpoints/opencode-session.png