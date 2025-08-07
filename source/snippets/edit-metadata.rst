The module's metadata is located in the ``ai4-metadata.yml`` file (`example <https://github.com/ai4os-hub/ai4os-demo-app/blob/main/ai4-metadata.yml>`__).
This is the information that will be displayed in the Marketplace.
The fields you need to edit to comply with our `schemata <https://github.com/ai4os/ai4-metadata/tree/master/src/ai4_metadata/assets/schemata>`__ are:

* ``title`` (*mandatory*): short title,
* ``summary`` (*mandatory*): one liner summary of your module,
* ``description`` (*optional*): extended description of your module, like a README,
* ``links`` (*mostly optional*): links to related info (training dataset, module citation. etc),
* ``tags`` (*mandatory*): relevant user-defined keywords (can be empty),
* ``categories``, ``tasks``, ``libraries``, ``data-type`` (*mandatory*): one or several keywords, to be chosen from a closed list (can be empty).

  .. dropdown:: ㅤ 📋 Supported values

      .. list-table::
        :header-rows: 1
        :widths: 15 40 25 20

        * - Libraries
          - Tasks
          - Categories
          - Data Type
        * - TensorFlow
          - Computer Vision
          - AI4 pre trained
          - Image
        * - PyTorch
          - Natural Language Processing
          - AI4 trainable
          - Text
        * - Keras
          - Time Series
          - AI4 inference
          - Time Series
        * - Scikit-learn
          - Recommender Systems
          - AI4 tools
          - Tabular
        * - XGBoost
          - Anomaly Detection
          -
          - Graph
        * - LightGBM
          - Regression
          -
          - Audio
        * - CatBoost
          - Classification
          -
          - Video
        * - Other
          - Clustering
          -
          - Other
        * -
          - Dimensionality Reduction
          -
          -
        * -
          - Generative Models
          -
          -
        * -
          - Graph Neural Networks
          -
          -
        * -
          - Optimization
          -
          -
        * -
          - Reinforcement Learning
          -
          -
        * -
          - Transfer Learning
          -
          -
        * -
          - Uncertainty Estimation
          -
          -
        * -
          - Other
          -
          -

* ``inference`` (*optional*): this is is the minimum resources your module needs to run an inference correctly (eg. CPU cores, RAM, GPUs, etc). If not specified, the Dashboard will prefill with some defaults, that can later be adapted by the user during the :ref:`configuration step <reference/dashboard:Hardware configuration>`.

* ``provenance`` (*optional*): this will allow your model to have a more rich :ref:`provenance <reference/modules:Provenance>` information, as your model provenance graph will show the resources and the hyper-parameters you used to train. The are two subfields you can specify:

  - ``nomad_job``: the Dashboard deployment UUID you used to train the final model,
  - ``mlflow_run``: the MLflow run UUID you used to train the final model,

Some fields are pre-filled via the AI4OS Modules Template and usually do not need to be modified.
Check you didn't mess up the YAML definition by running our `metadata validator <https://github.com/ai4os/ai4-metadata>`__:

.. code-block:: console

   pip install ai4-metadata
   ai4-metadata validate ai4-metadata.yml
