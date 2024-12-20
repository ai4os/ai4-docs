Frequently Asked Questions (FAQ)
================================

This page gathers know issues of the platform, along with possible solutions.
If your issue does not appear here, please contact support.

.. TODO: check if the FAQ issues still apply


Hardware issues
---------------

🔥 The Dashboard shows there are free GPUs but my deployment is still queued
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This can happen sometimes when a GPU gets stuck in the system and is not correctly
freed.

Please contact support if this happens to you!


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

.. dropdown:: ㅤㅤ More info

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
We are working on fixing this issue. If this is happening to you, please contact support.

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

If latency is still slow in the new deployment, please contact support.


🔥 I cannot find my dataset under ``/storage/ai4-storage``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This can happen if you are accessing the dataset from several deployments at the same
time, and the ``ls`` command hasn't properly refreshed its index.

To fix this you will need to `cd` to the folder and run `cd .` for the `ls` command to
refresh its index (`ref <https://stackoverflow.com/questions/38336329/ls-not-updating-to-reflect-new-files>`__).
Now you should be able to see your dataset.


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

If the issue persists, please contact support.


.. _new-features-request:

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
