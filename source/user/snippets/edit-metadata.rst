The module's metadata is located in the ``ai4-metadata.yml`` file.
This is the information that will be displayed in the Marketplace.
Among the fields you might need to edit are:

* ``title`` (`mandatory`): short title,
* ``summary`` (`mandatory`): one liner summary of your module,
* ``description`` (`optional`): extended description of your module, like a README,
* ``links`` (`mostly optional`): links to related info (training dataset, module citation. etc),
* ``tags`` (`mandatory`): relevant user-defined keywords (can be empty),
* ``categories``, ``tasks``, ``libraries`` (`mandatory`): relevant keywords to be chosen from a closed list (can be empty),

Some fields are pre-filled via the AI4OS Modules Template and usually do not need to be modified.
Check you didn't mess up the YAML definition by running our metadata validator:

.. code-block:: console

    $ pip install git+https://github.com/ai4os/ai4-metadata-validator
    $ ai4-metadata-validator ai4-metadata.yml
