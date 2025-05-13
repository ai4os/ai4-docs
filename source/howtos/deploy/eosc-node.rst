Deploy a model on ESOC EU Node
==============================

.. admonition:: Requirements
   :class: info

   🔒 This tutorial requires :ref:`access to the EOSC EU Node and the usage of available credits in your account <https://open-science-cloud.ec.europa.eu/>`.

This tutorial summarizes how to deploy a pre-trained AI model from the AI4EOSC Marketplace in the EOSC EU Node to be used for inference via the DEEPaaS API. For this, we will use the Tools Hub functionality of the EOSC EU Node, which allows us to deploy customized virtual infrastructures via TOSCA Templates on the available Cloud resources.

Two kind of deployments are supported in the EOSC EU Node: *Virtual Machines* (VMs), which run on OpenStack-based Clouds and *containers* which run on managed OKD-based platforms. Let's analyze both options in the next tables.

.. list-table::
    :header-rows: 1

    * - ✅ VMs Pros
      - ❌ VMs Cons
    * - - You can login via SSH to the VM and, therefore, have full access to the execution environment.
      - - Longer deployment time,
        - Endpoint exposed in an IP, without a DNS name.


.. list-table::
    :header-rows: 1

    * - ✅ Containers Pros
      - ❌ Containers Cons
    * - - Fast deployment times,
        - Endpoint exposed in a DNS name.
      - - Managed platform, no access to the execution environment.

This page describes the procedures to support both approaches. It also includes the instructions to register an AI4EOSC Model as a tool in the EOSC EU Node and the instructions on how to deploy those previously registered tools to be used for AI inference in the resources of the EOSC EU Node. 

1. Procedure to Register the AI4EOSC Model as a Tool in the EOSC EU Node
------------------------------------------------------------------------
TBC