Modules
=======

Every component in the platform is open-source, including the modules!
This means that everything you develop in the platform can be :doc:`deployed anywhere else </user/howto/deploy/cloud>`.

All  modules are found at the :doc:`AI4OS Dashboard <dashboard>`, the source code is
hosted under `Github's ai4os-hub <https://github.com/ai4os-hub>`__ organization and the corresponding Docker images are
hosted under `DockerHub's ai4oshub <https://hub.docker.com/u/ai4oshub/>`__ organization.

Modules follow the following name convention:

* ``ai4os-hub/ai4-<project-name>``: module officially developed by the project
* ``ai4os-hub/<project-name>``: modules developed by external users

Docker images have usually tags depending on whether they are using Github's ``master`` or ``test`` and
whether they use ``cpu`` or ``gpu``. Tags are usually:

* ``latest`` or ``cpu``: master + cpu
* ``gpu``: master + gpu
* ``cpu-test``: test + cpu
* ``gpu-test``: test + gpu


CI /CD pipeline
---------------

In the project we use `Jenkins <https://jenkins.services.ai4os.eu/job/AI4OS-hub>`__
for implementing CI/CD (Continuous Integration / Continuous Development) pipeline. This pipeline automatically performs a
series of actions for you each time you commit a change in your code. This ensures that all the information and builds
across the project are always up-to-date with your code.

This is an example of actions tha are performed by the pipeline:

.. image:: /_static/images/ai4eosc/jenkins.png
