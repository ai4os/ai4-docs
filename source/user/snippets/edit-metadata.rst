The module's metadata is located in the ``metadata.json`` file.
This is the information that will be displayed in the Marketplace.
Among the fields you might need to edit are:

* ``title`` (`mandatory`): short title,
* ``summary`` (`mandatory`): one liner summary of your module,
* ``description`` (`optional`): extended description of your module, like a README,
* ``keywords`` (`mandatory`): tags to make your module more findable
* ``training_files_url`` (`optional`): the URL  of your model weights and additional training information,
* ``dataset_url`` (`optional`): the URL dataset URL,
* ``cite_url`` (`optional`): the DOI URL of any related publication,

Most other fields are pre-filled via the AI4OS Modules Template and usually do not need to be modified.
Check you didn't mess up the JSON formatting by running:

.. code-block:: console

    $ pip install git+https://github.com/ai4os/ai4-metadata-validator
    $ ai4-metadata-validator metadata.json

:fa:`warning` Due to some issues with the JSON format parsing **avoid** using ``:``  in the values you are filling.

.. TODO: update to YAML
