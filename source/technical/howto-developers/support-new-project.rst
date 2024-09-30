Support a new project
=====================

These are the steps required to onboard a new project:

* create a new VO in EGI Check-In (eg. ``vo.ai4life.eu``),
* ask EGI to approve new Dashboard domain (eg. ``https://ai4life.cloud.ai4eosc.eu``)
* create new Nomad namespace (eg. ``ai4life``),
* add new Nomad CPU/GPU nodes supporting that namespace,
* deploy a dedicated Dashboard in the approved domain,
* adapt PAPI to support new VO,
* adapt ai4-accounting to start tracking new VO,
* adapt OSCAR to start supporting new VO.