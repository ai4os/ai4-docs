Environmental footprint of AI
=============================

As AI models grow in complexity and scale, their energy consumption and carbon emissions
become increasingly significant. Monitoring the environmental footprint of AI workloads
is essential to promote sustainable practices and to make informed decisions about
resource usage during training and inference.

This is why AI4EOSC has teamed with `Wattnet <https://wattnet.eu/>`__ and the `Greendigit <https://greendigit-project.eu/>`__ project to **monitor** the energy footprint of the platform and to **act** upon it. What is this integration currently offering?

Real-time footprint visualization
---------------------------------

The Dashboard integrates a map with all the datacenters that are part of the AI4EOSC federation.
Wattnet is able to offer real-time time estimations of the carbon impact of each datacenter (based on the mean values of the country where the datacenter is located).
This is summarized in an *Energy Quality* metric, which measures (in CO2/kWH) how carbon intensive is the grid that datacenter is plugged to. Lower metrics will mean mean that the datacenters energy is cleaner.

.. image:: /_static/images/dashboard/stats-datacenters.png


Smart job scheduling
--------------------

Power Usage Effectiveness (PUE) is a metric that measures the energy efficiency of a datacenter by comparing the total energy consumed by the facility to the energy delivered to the computing equipment. A PUE of 1.0 would mean all energy goes to computing, while higher values indicate more energy is spent on cooling, lighting, and other overhead.

Based on the datacenter mean energy quality (averaged over the previous days) and the datacenter PUE, AI4EOSC routes new deployments to greener datacenters. Future iterations will go even further, leveraging Wattnet forecasting capabilities to schedule jobs during the particular hours of the day where energy is greener.


Detailed per-job monitoring
---------------------------

.. admonition:: Beta
    :class: warning

    This feature is still in development and may be subject to changes.

Finally, AI4EOSC leverages the Greendigit stack (based on `Scaphandre <https://github.com/hubblo-org/scaphandre>`__) to offer realtime energy consumption metrics of any particular deployment in the AI4EOSC platform. Then Wattnet is used to transform this measurement into a relatable carbon footprint, that is shown to the AI4EOSC deployment owner in the Dashboard.

.. todo: add image

Finally, this information is included in the provenance chain of the AI module, offering future users accurate information of the training footprint of that user.

By providing this level of transparency, AI4EOSC aims to raise awareness among users about the environmental cost of their AI workloads. Making researchers and developers mindful of the resources they consume encourages more responsible usage patterns, such as optimizing model architectures or reducing unnecessary training runs.
