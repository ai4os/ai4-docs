Deploy an external model
========================

.. admonition:: Requirements
   :class: info

   🔒 You need a :doc:`platform account </getting-started/register>` with :ref:`full access level <reference/user-access-levels:Full access level>`.

You can deploy models from external marketplaces in :doc:`AI4OS dedicated resources </howtos/deploy/nomad>` to perform inference.
Currently we support the following marketplaces:

AI4Life
-------

We currently support all V5 models from the AI4Life `BioImage Model Zoo <https://bioimage.io/>`__.
Those model are accessible in the :ref:`Dashboard Marketplace panel <dashboard_marketplace>`.

.. image:: /_static/images/dashboard/marketplace-ai4life.png

When clicking on a given model you will be show the model information along with the metadata of that model.

.. image:: /_static/images/dashboard/module-ai4life.png

Click ``Deploy`` and :ref:`configure the resources <reference/dashboard:Hardware configuration>`.
Once it is deployed you can find it on the Tools deployment table (similar to the :ref:`Modules deployments table <dashboard-manage-deployments>`).

.. image:: /_static/images/dashboard/deployments_modules_tools.png

Clicking on the :material-outlined:`terminal;1.5em` ``Quick access`` button you will be redirected to the Gradio UI to make an inference with the model.

.. image:: /_static/images/endpoints/gradio_ai4life.png
