Support a new project
=====================

These are the steps required to onboard a new project:

* support the new project authentication:
    - Option 1: create a new VO in EGI Check-In (eg. ``vo.ai4life.eu``),
    - Option 2: federate their authentication in Keycloak,
* support the new Dashboard domain:
    - create the domain in the DNS (eg. ``https://ai4life.cloud.ai4eosc.eu``),
    - add the domain in the Cloud proxy, generate LetsEncrypt certs,
    - add the domain in the Keycloak Dashboard client,
* adapt Nomad:
    - create new Nomad namespace (eg. ``ai4life``),
    - add new Nomad CPU/GPU nodes supporting that namespace,
* adapt PAPI to support new VO,
* deploy a dedicated Dashboard in the target domain,
* add the new dashboard to the docs,

**Optional**:
* adapt OSCAR to start supporting new VO.
