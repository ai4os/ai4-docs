:orphan:

Federated Learning with NVFLARE
===============================

In this tutorial, we will guide you on how to use the Federated Learning (FL) server in the AI4OS platform to perform FL training with `NVFlare <https://developer.nvidia.com/flare>`__.

.. admonition:: Requirements
   :class: info

   🔒 You need a :doc:`platform account </getting-started/register>` with :ref:`full access level <reference/user-access-levels:Full access level>`.


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

    If you want to give another user access to sign in to the **NVFlare Dashboard** and register sites to the project, please make sure that during the deployment creation, you set **'Make project public'** to ``True``. Otherwise, you can only register the clients from the command line.


.. image:: /_static/images/dashboard/configure_nvflare_1.png


Preparing the training environment
----------------------------------

In the :ref:`deployments list <dashboard-manage-deployments>` you will be able to see your newly created NVFLARE instance.

The NVFLARE endpoints
^^^^^^^^^^^^^^^^^^^^^

Clicking the ``Quick access`` button, you can see two endpoints:

* **DASHBOARD**:

  This allows you to access the NVFLARE Dashboard.

  .. image:: /_static/images/endpoints/nvflare_dashboard_login.png

  Enter your credentials from the configuration step and voilá, you're in as the project admin!

  This dashboard is used to generate **the startup kits** for the server, admins and clients.
  The startup kits include the configurations and certificates required to establish secure connections between the FL servers, FL clients, and admin clients.
  These files are essential for verifying identity and enforcing authorization policies between the server and clients.

* **SERVER-JUPYTER:**

  This provides access to a JupyterLab environment for the server, also protected by your admin credentials.
  The server's startup kit is automatically downloaded to the workspace directory within JupyterLab, and the server is already running.

  If the server is stopped for any reason during the project, you can restart it by executing the following script:

  .. code-block:: console

      $ sh workspace/server_address_folder/startup/start.sh

Adding new clients to the training
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A project can have multiple admins (among `other roles <https://nvflare.readthedocs.io/en/2.4/user_guide/dashboard_ui.html#nvflare-dashboard-ui>`__).
The **Project Admin** is the person who initially created the deployment within the AI4OS Dashboard.
Each organization participating in the federated training should also designate an **Organization Admin** (Org Admin). Org Admins are responsible for registering their own organization's sites within the project.
The Project Admin has the authority to approve Organization Admins as well as their associated sites.

To allow organization admins to register their sites, share the dashboard link with them.
Organization Admins can access the dashboard through this link and click ``Sign Up`` to register themselves and their sites (`detailed instructions <https://nvflare.readthedocs.io/en/2.4/user_guide/dashboard_ui.html#nvflare-dashboard-ui>`__).
To register sites, ensure the Role is set to **'Org Admin'**. On the next page, the Org Admin can register their sites, specifying the number of GPUs and the memory capacity for each GPU.

After completing registration, users must wait for the project's main admin to approve their roles and associated sites.
Once approved, the organization admins can log into the dashboard, download the startup kits for their sites, and obtain the Docker image shared by the project admin for the project code.
Using these startup kits, they can then launch their sites.

.. image:: /_static/images/endpoints/nvflare_dashboard_console.png

After downloading and unzipping the startup package, the Admin can run the following command to start the sites from anywhere in the world and connect to the server hosted in the AI4OS Platform.

.. code-block:: console

    $ sh ./site_name_folder/startup/start.sh

The Admin can also start the Flare Console by running the following command from the downloaded Flare Console startup kit from anywhere in the world.

.. code-block:: console

    $ sh ./admin_email/startup/fl_admin.sh

You will be prompted to enter a username. Use the email address provided by the admin during registration.

From the admin console, the admin can orchestrate the FL study—this includes starting and stopping the server and clients, checking their status, deploying applications, and managing FL experiments (`available commands <https://nvflare.readthedocs.io/en/main/real_world_fl/operation.html>`__).

.. note::

  To maintain a consistent environment, it is advised that the project Admin create a Docker image containing all the necessary dependencies and configurations, and provide it during the deployment of the server on the AI4OS Dashboard. This approach ensures reproducibility and simplifies deployment across different sites.

  By default we provide such an image during the configuration step:

  .. image:: /_static/images/dashboard/configure_nvflare_2.png


Start your Federated Learning training
--------------------------------------

Once a sufficient number of sites are connected to the server, any Admin can log in to the console and submit an FL job.
Before doing so, they need to prepare the FL job by converting their existing ML/DL code into an FL-compatible version using NVFLARE.

Please take a look at the following examples:

- Check the `getting_started <https://github.com/NVIDIA/NVFlare/tree/fd3b74ff4e561447e6769259dd4903174e466a3e/examples/getting_started>`__ examples in the NVFLARE repository.
- Check the `ml-to-fl <https://github.com/NVIDIA/NVFlare/tree/fd3b74ff4e561447e6769259dd4903174e466a3e/examples/hello-world/ml-to-fl>`__ examples demonstrating how to transition simple ML/DL projects to NVFLARE.
- We provide a **simple** `hello numpy example  <https://github.com/ai4os/ai4os-nvflare-test?tab=readme-ov-file#running-a-sample-fl-job>`__.
- For an **advanced** example, you can check the `phyto-plankton-classification <https://dashboard.cloud.ai4eosc.eu/catalog/modules/phyto-plankton-classification>`__ module that has been adapted to NVFLARE.

For more information, please refer to the official `NVFLARE documentation <https://nvflare.readthedocs.io/en/main/index.html>`__.
