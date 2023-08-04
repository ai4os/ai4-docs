Develop Dashboard
=================

Right now we have two Dev Dashboards:

* https://dashboard.dev.ai4eosc.eu/
* https://dashboard.dev.imagine-ai.eu/

Dev Dashboards are querying

	https://api.dev.ai4eosc.eu/

instead of

	https://api.cloud.ai4eosc.eu/

**Right now** both Dashboards (prod and dev) are the same:
they use main branch from dashboard, main branch from API and
are pointing to Nomad production cluster.

**In the future**, dev dashboard will be used to test experimental features that might
break production workflow. This means dashboard from dev branch, api from dev branch
and potentially also pointing to Nomad dev cluster.
