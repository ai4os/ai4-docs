.. _dashboard_statistics:

Statistics
==========

This panel shows both your individual statistics, as well as the aggregated statistics of your :ref:`community gateway <getting-started/overview:Community gateways>`.


User stats
----------

.. image:: /_static/images/dashboard/stats/user/usage.png

The **My Usage** section displays your individual metrics in the platform:

* The number of jobs you have deployed,
* The number of resources your are currently consuming (CPUs, GPUs, RAM, disk)
* The aggregated resources consumed over time (compared to the total consumed by your gateway).

The metrics units are ``<resource> / day``. Therefore 2000 CPU consumed means that you have consumed the equivalent of 1 CPU for 2000 days (eg. same as 2 CPU for 1000 days).

As the resources in the project are assigned for exclusive usage, the metrics are not measuring *real* usage, but *allocated* usage. So if you create a 1-CPU deployment for 10 days, the aggregate usage will show 10 CPU days, even if you did not actually use   the CPU at all.

.. image:: /_static/images/dashboard/stats/user/footprint.png

The **My footprint** section shows:

* The aggregated power used by all your deployments
* The aggregated energy consumed by all your deployments
* The aggregated carbon emitted by all your deployments
* The aggregated water emitted by all your deployments

These metrics are based on *realtime measurements* done in directly in your deployments, not on estimates. However not all datacenters currently support footprint monitoring, so your real aggregated footprint might be higher since the footprint of some jobs might not have been taken into account in the aggregation depending on the datacenter they landed in.

Platform stats
--------------

This section aggregates the metrics across all user of your community gateway.

.. image:: /_static/images/dashboard/stats/platform/usage.png

The **Usage** section shows:

* the aggregated platform resources (used and total) available for your gateway
* time series of relevant metrics like running/queued deployments, resources usage, etc.

.. image:: /_static/images/dashboard/stats/platform/footprint.png

The **Footprint** section shows:

* the aggregated footprint of all the deployments of your gateway
* the datacenter grid signals of the datacenters serving your gateway. This shows how clean your datacenters are. Based on this information, the platform tries to route jobs to greener datacenters :ref:`using our GreenDirector <considerations/footprint:Smart job scheduling>`.

.. image:: /_static/images/dashboard/stats/platform/datacenters.png

The **Footprint** section shows a maps with:

* relevant per datacenter characteristics like PUE (Power Usage Effectiveness, which measures how efficiently the a datacenter uses energy: the closer to 1 the better) or grid signals (environmental score, zone carbon footprint, zone water footprint)
* the aggregated resources consumed by that particular datacenter
