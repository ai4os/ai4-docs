Once your repo is set, it's time to integrate it in the :ref:`Marketplace <user/overview/dashboard:Selecting the modules>`!

For this the steps are:

1. `Open an issue <https://github.com/ai4os-hub/modules-catalog/issues/new>`__ in the the AI4OS Catalog repo.
2. An admin will create the Github repo for your module inside the `ai4os-hub organization <https://github.com/ai4os-hub>`__.
   You will be granted ``write`` permissions in that repo.
3. Upload your code to that repo.
4. An admin will review your code and add it to the Catalog.

When your module gets approved, you may need to commit and push a change to ``metadata.json``
in your ``https://github.com/<github-user>/DEEP-OC-<project-name>`` so that
`the Pipeline <https://github.com/deephdc/DEEP-OC-demo_app/blob/726e068d54a05839abe8aef741b3ace8a078ae6f/Jenkinsfile#L104>`__
is run for the first time, and your module gets rendered in the marketplace.