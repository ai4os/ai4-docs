Support a new project
=====================

These are the steps required to onboard a new project:

* support the new project authentication:
    - Option 1: create a new group in AI4EOSC Keycloak (eg. ``vo.ai4life.eu``),
    - Option 2: federate their authentication in Keycloak,
* create the proper Keycloak mappings
* support the new Dashboard domain:
    - create the domain in the `AI4EOSC DNS <https://nsupdate.fedcloud.eu/>`__ (eg. ``https://ai4life.cloud.ai4eosc.eu``),
    - add the domain in the IFCA proxy, that will automatically generate LetsEncrypt certs,
    - add the domain in the Keycloak Dashboard client,
* adapt Nomad:
    - create new Nomad namespace (eg. ``ai4life``),
    - add new Nomad CPU/GPU nodes supporting that namespace,
* adapt PAPI to support new VO,
* deploy a dedicated Dashboard in the target domain,
* add the new dashboard to the docs,

**Optional**:
* adapt OSCAR to start supporting new VO.
