# Documentation repository

[![Documentation Status](https://readthedocs.org/projects/ai4-docs/badge/?version=latest)](https://docs.ai4eosc.eu/en/latest/?badge=latest)


This repository contains software documentations, guides, tutorials, logbooks
and similar documents produced to interact with the AI4EOSC platform.

This documentation is deployed at:  http://docs.ai4eosc.eu/

If you want to build the documentation locally for development, run:
```bash
make html
```

This will create a `build/html` folder with the built documentation.

We recommend to periodically:

* test link health to make sure all the URL referenced in the documentation are indeed up and running.

  `python check_links.py`

* test the documentation spelling:

  `cspell-cli "**/*.rst"`