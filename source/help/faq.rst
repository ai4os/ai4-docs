Frequently Asked Questions (FAQ)
================================

This page gathers know issues of the platform, along with possible solutions.
If your issue does not appear here, please :doc:`contact support </help/index>`.

.. TODO: check if the FAQ issues still apply


Accessing the platform
----------------------

I want to start using the platform, where can I start?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Great, welcome aboard! 🥳

Start by registering an :doc:`register in the platform </getting-started/register>`.
Depending on your account you will get access to some services and not others, according to the different :doc:`user access levels </reference/user-access-levels>`.

We have a :doc:`quickstart guide </getting-started/quickstart>` with some ideas on how to start using the platform.

Deployment issues
-----------------

🔥 The Dashboard shows my deployment but it immediately disappears
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sometimes it can happen that when you :ref:`create a new deployment <reference/dashboard:Making a deployment>`, it initially appears in the :ref:`deployments table <reference/dashboard:Managing the deployments>` but disappears immediately, or is marked as ``failed/error``.

This usually happens in deployments that where :ref:`launched using Nextcloud <reference/dashboard:Storage configuration>`. It can happen that your Nextcloud credentials become invalid thus leading to failure when trying to launched your deployment with Nextcloud connected.

To fix this issue, please :ref:`re-link your Nextcloud account <reference/dashboard:Profile>` and try deploying again.

If you are still experiencing this error after relinking, please :doc:`contact support </help/index>`.
If you are experiencing this issue in a deployment that was not linked with Nextcloud, please :doc:`contact support </help/index>`.

We are debugging why the Nextcloud expiration happens in the first place.


🔥 I suddenly lost the contents of my deployment, can I recover them?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Nodes sometimes crash unexpectedly. It's not common but it can happen.
Since your deployment is running as a Docker container, after a node restart, your deployment contents are gone and not recoverable.

To protect yourself against unexpected data losses we recommend locating any important files (like the code you are developing) inside the ``/storage`` to have instant file syncing with the :doc:`AI4OS Storage </reference/storage>`.

Learn how to create a :ref:`Development Environment linked with storage <howtos/develop/dashboard:2. Prepare your development environment>`.

Hardware issues
---------------

🔥 The Dashboard shows there are free GPUs but my deployment is still queued
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This can happen sometimes when a GPU gets stuck in the system and is not correctly
freed.

Please :doc:`contact support </help/index>` if this happens to you!


🔥 I ran out of disk in my deployment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You are trying to download some data but the following error is raised:

.. code-block:: console

    RESOURCE_EXHAUSTED: Out of memory while trying to allocate ******** bytes

This means that you have consumed more disk than what you initially requested.
You can see your current disk consumption using:

.. code-block:: console

    $ df -h | grep overlay

This will show you three values, respectively the ``Total | Used | Remaining`` disk.

To solve this first, make sure to delete files in the Trash (``/root/.local/share/Trash/files``).
Files end up there when deleted from the JupyterLab UI, thus not freeing up the space
correctly.

If you still find you have not enough disk, you have two options:

* create a new deployment, requesting more disk in the configuration,
* access your Nextcloud dataset files :doc:`via a virtual filesystem </reference/storage>`,
  in order to avoid overloading the disk.


🔥 My deployment does not correctly list my resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The deployments in the platform are created as Docker containers.
Therefore some resources might not be properly virtualized like in a traditional
Virtual Machine.
This means that standard commands for checking up resources might give you higher
numbers than what is really available (ie. they give you the resources of the
full Virtual Machine where Docker is running, not the resources avaible to your
individual Docker container).

Standard commands:

* **CPU**: ``lscpu | grep -E '^Thread|^Core|^Socket|^CPU\('``
* **RAM memory**: ``free -h``
* **Disk**: ``df -h``

Real available resources can be found with the following commands:

* **CPU**: ``printenv | grep NOMAD_CPU`` will show both reserved cores (``NOMAD_CPU_CORES``) and maximum CPU limit (in MHz) (``NOMAD_CPU_LIMIT``).
* **RAM memory**: ``echo $NOMAD_MEMORY_LIMIT`` or ``cat /sys/fs/cgroup/memory/memory.limit_in_bytes``
* **Disk**: ``df -h | grep overlay`` will show you three values, respectively the ``Total | Used | Remaining`` disk

It is your job to program your application to make use of these real resources
(eg. load smaller models, load less data, etc).
Failing to do so could potentially make your process being killed for surpassing
the available resources.
For example, check how to limit CPU usage in `Tensorflow <https://stackoverflow.com/questions/57925061/how-can-i-reduce-the-number-of-cpus-used-by-tensorlfow-keras>`__
or `Pytorch <https://pytorch.org/docs/stable/generated/torch.set_num_threads.html#torch.set_num_threads>`__.

.. dropdown:: ㅤ 💡 More info

    For example trying to allocate 8GB in a 4GB RAM machine will lead to failure.

    .. code-block:: console

        root@2dc9e20f923e:/srv# stress -m 1 --vm-bytes 8G
        stress: info: [69] dispatching hogs: 0 cpu, 0 io, 1 vm, 0 hdd
        stress: FAIL: [69] (415) <-- worker 70 got signal 9
        stress: WARN: [69] (417) now reaping child worker processes
        stress: FAIL: [69] (451) failed run completed in 6s


🔥 My GPU just disappeared from my deployment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You try to list to GPU and it doesn't appear:

.. code-block:: console

    $ nvidia-smi
    Failed to initialize NVML: Unknown Error"

This is due to `this issue <https://github.com/NVIDIA/nvidia-docker/issues/1730>`__.
We are working on fixing this issue. If this is happening to you, please :doc:`contact support </help/index>`.

In the meantime, your best option is to backup your data, delete your deployment and create a new one.


.. _faq_storage:

Storage issues
--------------

🔥 I cannot access ``/storage``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You try to :doc:`access "/storage" </reference/storage>` and you get the message:

.. code:: console

    root@226c02330e9f:/srv# ls /storage
    ls: reading directory '/storage': Input/output error

This probably means that you have entered the wrong credentials when configuring your
deployment in the :doc:`Dashboard </reference/dashboard>`.

You will need to delete the current deployment and make a new one.
Follow our guidelines on how to :ref:`get an RCLONE user and password <rclone_configuration>`
to fill the deployment configuration form.


🔥 Accessing ``/storage`` runs abnormally slow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This happens from time to time due to connectivity issues. If this behavior persists
for more than a few days, try creating a new deployment.

If latency is still slow in the new deployment, please :doc:`contact support </help/index>`.


🔥 I cannot find my dataset under ``/storage/ai4-storage``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Option 1: Refresh the index**

This can happen if you are accessing the dataset from several deployments at the same
time, and the ``ls`` command hasn't properly refreshed its index.

To fix this you will need to `cd` to the folder and run `cd .` for the `ls` command to
refresh its index (`ref <https://stackoverflow.com/questions/38336329/ls-not-updating-to-reflect-new-files>`__).
Now you should be able to see your dataset.

**Option 2: Download error**

It can also happen that your dataset failed to download for some reasons.
In the file ``ai4os.log`` you will find the reason of the failure (eg. timeout).

You have several options:

* *Option 1*: redeploy and see if the timeout error is no longer happening,
* *Option 2*: try to download the dataset with the CLI using `datahugger <https://github.com/J535D165/datahugger>`__:

  .. code-block:: console

    $ pip install datahugger
    $ datahugger "<doi>" "<data_dir>"

* *Option 3*: download your dataset manually and paste it to Nextcloud

🔥 rclone fails to connect
^^^^^^^^^^^^^^^^^^^^^^^^^^

You tried to manually use RCLONE and you are returned the following error message:

.. code:: console

    2024/11/04 13:04:53 Failed to about: about call failed: No public access to this resource., Username or password was incorrect, No 'Authorization: Bearer' header found. Either the client didn't send one, or the server is mis-configured, Username or password was incorrect: Sabre\DAV\Exception\NotAuthenticated: 401 Unauthorized

This is probably due because you are using an older RCLONE version (earlier than ``1.63.3``).
Update to a newer RCLONE version and :ref:`find more information here <rclone_configuration>`.


Other issues
------------

🔥 The Quick access button is not working
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This happens when you launched a module/tool from the Dashboard and try to immediately
click on ``Quick Access``. The new tab it opens is returning either
*404 page not found* or *Bad Gateway*.

You might need to wait a few seconds, still the endpoint is really ready and shows as
an active endpoint in the ⓘ ``Info`` section.

.. We are not disabling the `Quick Access` view based on the active endpoints,
.. because parsing active endpoints in the main view is very costly (we have to ping
.. at least 1 endpoint, ~0.4s, per deployment)


🔥 Service X is not working
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check the `Status page <https://status.ai4eosc.eu/>`__ to see if there is any
maintenance action going on.
If you don't see anything, wait a couple of hours to make sure it is not a
temporary issue.

If the issue persists, please :doc:`contact support </help/index>`.


.. _new-features-request:

ℹ️ How can I cite the AI4EOSC project?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you need to cite he AI4EOSC project or the AI4OS stack, please consider citing
the following paper:

    Heredia, I., García, Á. L., Moltó, G., Calatrava, A., Kozlov, V., Costantini, A., … Díez, J. (2025). `AI4EOSC: a Federated Cloud Platform for Artificial Intelligence in Scientific Research <http://arxiv.org/abs/2512.16455>`__. *arXiv* [Cs.DC].

.. dropdown:: 📄 ㅤBixTeX citation

    .. code-block:: bib

        @misc{heredia2025ai4eoscfederatedcloudplatform,
            title={AI4EOSC: a Federated Cloud Platform for Artificial Intelligence in Scientific Research},
            author={Ignacio Heredia and Álvaro López García and Germán Moltó and Amanda Calatrava and Valentin Kozlov and Alessandro Costantini and Viet Tran and Mario David and Daniel San Martín and Marcin Płóciennik and Marta Obregón Ruiz and Saúl Fernandez and Judith Sáinz-Pardo Díaz and Miguel Caballer and Caterina Alarcón Marín and Stefan Dlugolinsky and Martin Šeleng and Lisana Berberi and Khadijeh Alibabaei and Borja Esteban Sanchis and Pedro Castro and Giacinto Donvito and Diego Aguirre and Sergio Langarita and Vicente Rodriguez and Leonhard Duda and Andrés Heredia Canales and Susana Rebolledo Ruiz and João Machado and Giang Nguyen and Fernando Aguilar Gómez and Jaime Díez},
            year={2025},
            eprint={2512.16455},
            archivePrefix={arXiv},
            primaryClass={cs.DC},
            url={https://arxiv.org/abs/2512.16455},
        }


ℹ️ I received a cluster downtime notification, what should I do?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If a downtime is expected, you should backup your work in order to avoid losing data.
Sometimes, when the downtime is performed only in some nodes of the cluster, you might recover your original work after the downtime.
But you should backup it anyway, just to be on the safe side.

How to backup modules?
""""""""""""""""""""""

There are two options. To be extra-safe, you can run both of them:

1. :ref:`Create a snapshot from your deployment<dashboard_snapshots>`.
   After the downtime you should be able to redeploy it and restart your work where you left it.
   This is the most comprehensive option, as it saves both your *data* and the *software/configuration* you installed in your deployment.

2. Save your data somewhere.

  * If your deployment is :ref:`connected with the AI4OS Storage <dashboard_storage>`, you can move your work under ``/storage``. It will automatically write the data into Nextcloud.

    Anyway, it's always good practice to develop under the ``/storage`` path because, in that way, your work is automatically synced with Nextcloud, thus preventing data loss in case of an unforeseen data failure.
  * If you are using git, you can commit your work to Github.
  * If you are accessing your deployment via an IDE, you can the available options to directly download your files.

How to backup tools?
""""""""""""""""""""

Snapshot creation is not supported for tools.
Therefore you will need to manually backup the data (different options are available for each tool).

In the case of :doc:`CVAT deployments </howtos/train/cvat>`, you can perform both these actions:

* `manually export the data <https://docs.cvat.ai/docs/manual/advanced/formats/>`__,
* deleting your CVAT deployment will automatically create a snapshot in the platform from which you will be able to restore later on,


🚀 I would like to suggest a new feature
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We are always happy improve our software based on user feedback.

Please open an issue in the Github repo of the component you are interested in:

* `The Dashboard <https://github.com/ai4os/ai4-dashboard/issues>`__
* `FlowFuse/Oscar/Elyra <https://github.com/ai4os/ai4-compose/issues>`__
* `The ML flow server <https://github.com/ai4os/ai4-mlflow/issues>`__
* `Frouros <https://github.com/IFCA-Advanced-Computing/frouros/issues>`__

If you think the documentation itself can be improved, don't hesitate to open
an issue or submit a Pull Request.

* `AI4OS documentation <https://github.com/ai4os/ai4-docs>`__

You can always check that your suggested feature is not on the
:doc:`Upcoming features </getting-started/new-features>` list.
