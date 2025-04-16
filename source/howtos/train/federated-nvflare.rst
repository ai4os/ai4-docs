Federated Learning with NVFLARE
===============================

.. admonition:: Requirements
   :class: info

   🔒 This tutorial requires :ref:`full authentication <getting-started/register:Full authentication>`.





Deploying a Federated server
----------------------------

The workflow for deploying a FL server is similar to the one for
:doc:`deploying a module </reference/dashboard>`.

In this particular case, you will need to pay attention to:

* Your credentials to access the NVFLARE Dashboard and associated Jupyter notebook.

* Whether to make the project public or restrict the training to authorized trusted partners.

* The Docker image that includes all the necessary dependencies and configurations provided by the admin of the project.

* The start and end dates of the training.
  
.. note::

    If you want to give another user access to sign in to the **NVFlare Dashboard** and register sites to the project, please make sure that during the deployment creation, you set **'Make project public'** to true. Otherwise, you can only register the clients from the command line.


.. image:: /_static/images/dashboard/configure_nvflare_1.png

Federated learning Dashboard in AI4EOSC
---------------------------------------

In the :ref:`deployments list <dashboard-manage-deployments>` you will be able to see your newly created NVFLARE instance.
Clicking the ``Quick access`` button, you can see two endpoints:

* **DASHBOARD**: you will directly enter the NVFLARE Dashboard. Enter your credentials from the configuration and voilá, you’re in as the project admin! 
This dashboard is used to generate the startup kits for the server, admins and clients. The **startup kits** include the configurations and certificates required to establish secure connections between the FL servers, FL clients, and admin clients. These files are essential for verifying identity and enforcing authorization policies between the server and clients.
To allow organization admins to register their sites, share the dashboard link with them. Organization  Admins can access the dashboard through this link and click 'Sign Up' to register themself and their sites.

.. note::
   
   A project can have multiple admins. The **Project Admin** is the person who initially created the deployment within the AI4EOSC project. This admin has the authority to approve additional admins as well as their associated sites.
   Each organization participating in the federated training should also designate an **Organization Admin (Org Admin)**. Org Admins are responsible for registering their own organization's sites within the project. There are other rolls that you can check `here <https://nvflare.readthedocs.io/en/2.4/user_guide/dashboard_ui.html#nvflare-dashboard-ui>`__. 

.. image:: /_static/images/dashboard/nvflare_dashboard_login

Follow the instructions in `NVFlare documentation <https://nvflare.readthedocs.io/en/2.4/user_guide/dashboard_ui.html#nvflare-dashboard-ui>`__ to sign up and register the sites.

.. note::

   To register sites, ensure the Role is set to '**Org Admin**'. On the next page, the Org Admin can register their sites, specifying the number of GPUs and the memory capacity for each GPU.
   After completing registration, users must wait for the project's main admin to approve their roles and associated sites.
   Once approved, the organization admins can log into the dashboard, download the startup kits for their sites, and obtain the Docker image shared by the project admin for the project code. Using these startup kits, they can then launch their sites.

.. image:: /_static/images/dashboard/nvflare_dashboard_console

**Connecting the clients and login to Admin console**

After downloading and unzipping the startup package, the Admin can run the following command to start the sites from anywhere in the world and connect to the server hosted on the AI4EOSC Dashboard.

.. code-block:: console

   ./site_name_folder/startup/start.sh 

The Admin can also start the Flare Console by running the following command from the downloaded Flare Console startup kit from anywhere in the world—including via the AI4EOSC Dashboard where the server is running.

.. code-block:: python

   ./admin_email/startup/fl_admin.sh 

You will be prompted to enter a username. Use the email address provided by the admin during registration.

From the admin console, the admin can orchestrate the FL study—this includes starting and stopping the server and clients, checking their status, deploying applications, and managing FL experiments. You can check the list of available admin console commands `here <https://nvflare.readthedocs.io/en/main/real_world_fl/operation.html>`__. 

.. note::

   To maintain a consistent environment, it is advised that the project Admin create a Docker image containing all the necessary dependencies and configurations, and provide it during the deployment of the server on the AI4EOSC Dashboard. This approach ensures reproducibility and simplifies deployment across different sites.

.. image:: /_static/images/dashboard/configure_nvflare_2.png

* **SERVER-JUPYTER:** Provides access to a JupyterLab environment for the server. The password to access this JupyterLab environment is the one provided by the admin during deployment. The server's startup kit is automatically downloaded to the workspace directory within JupyterLab, and the server is already running.

.. note::
   
   If the server is stopped for any reason during the project, you can restart it by executing the script

.. code-block:: python

   workspace/server_address_folder/startup/start.sh 

Federated learning training in AI4EOSC
--------------------------------------
Once a sufficient number of sites are connected to the server, any Admin can log in to the console and submit an FL job. Before doing so, they need to prepare the FL job by converting their existing ML/DL code into an FL-compatible version using NVFLARE. 
We will soon add a simple example for reference! 



For more information on running a training, please follow the official `NVFLARE documentation <https://nvflare.readthedocs.io/en/main/index.html>`__.

We will soon add a simple example for reference! 🚀