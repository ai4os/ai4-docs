Environmental footprint of AI
=============================

As AI models grow in complexity and scale, their energy consumption and carbon emissions
become increasingly significant. Monitoring the environmental footprint of AI workloads
is essential to promote sustainable practices and to make informed decisions about
resource usage during training and inference.

This is why AI4EOSC has teamed with `Wattnet <https://wattnet.eu/>`__ and the `Greendigit <https://greendigit-project.eu/>`__ project to **monitor** the energy footprint of the platform and to **act** upon it. What is this integration currently offering?

Detailed per-job monitoring
---------------------------

AI4EOSC leverages the Greendigit stack (based on `Scaphandre <https://github.com/hubblo-org/scaphandre>`__) to offer realtime measurements (not estimates!) of energy consumption for any particular deployment in the AI4EOSC platform (as long as the deployment landed in a datacenter that supports footprint monitoring). Then Wattnet is used to transform this measurement into a relatable carbon/water footprint, that :ref:`is shown <dashboard/deployments:Managing the deployments>` to the deployment owner in the Dashboard.

.. image:: /_static/images/dashboard/deployments/details/default-energy.png

It shows:

* The power used by the deployment (measured in W)
* The energy consumed by the deployments (measured in kWH)
* The carbon emitted by the deployment (measured in gCO2)
* The water emitted by the deployment (measured in L)

Finally, this information is included in the provenance chain of the AI module, offering future users accurate information of what was the training footprint of that particular module.

By providing this level of transparency, AI4EOSC aims to raise awareness among users about the environmental cost of their AI workloads. Making researchers and developers mindful of the resources they consume encourages more responsible usage patterns, such as optimizing model architectures or reducing unnecessary training runs.

Aggregated footprint visualization
----------------------------------

The :doc:`Dashboard statistics </dashboard/statistics>` aggregates the individual deployment monitoring both at the level of the user and across all users of the gateway.

.. image:: /_static/images/dashboard/stats/platform/footprint-measured.png

Smart job scheduling
--------------------

Finally, AI4EOSC uses Wattnet to retrieve different grid signals for each datacenter (obtained through the GreenDIGIT metrics publication system - EIMPS). Those indicate how green the energy they consume is, based on how the energy was generated (solar, wind, nuclear, etc). Based on the aggregation of those metrics, an individual environmental score is assigned to each datacenter at each specific point in time.

.. image:: /_static/images/dashboard/stats/platform/footprint-grid.png

Additionally, each datacenter has an associated Power Usage Effectiveness (PUE). This is a metric that measures the energy efficiency of a datacenter by comparing the total energy consumed by the facility to the energy delivered to the computing equipment. A PUE of 1.0 would mean all energy goes to computing, while higher values indicate more energy is spent on cooling, lighting, and other overhead.

Based on the combination of the environmental score and the PUE, we have implemented at the WMS level the :material-outlined:`eco;1.5em` **AI4EOSC GreenDirector**. This is a green-aware extension that ranks candidate sites, allowing us to introduce smart energy-aware scheduling, where the platform favors routing new deployments to greener datacenters via Nomad affinities.

Future iterations will go even further, leveraging Wattnet forecasting capabilities to schedule jobs during the particular hours of the day where energy is greener.
