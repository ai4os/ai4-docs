The module's metadata is located in the ``ai4-metadata.yml`` file.
This is the information that will be displayed in the Marketplace.
The fields you need to edit to comply with our `schemata <https://github.com/ai4os/ai4-metadata/blob/master/src/ai4_metadata/schemata/ai4-apps-v2.0.0.json>`__ are:

* ``title`` (`mandatory`): short title,
* ``summary`` (`mandatory`): one liner summary of your module,
* ``description`` (`optional`): extended description of your module, like a README,
* ``links`` (`mostly optional`): links to related info (training dataset, module citation. etc),
* ``tags`` (`mandatory`): relevant user-defined keywords (can be empty),
* ``categories``, ``tasks``, ``libraries``, ``data-type`` (`mandatory`): one or several keywords, to be chosen from a closed list (can be empty).

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


Some fields are pre-filled via the AI4OS Modules Template and usually do not need to be modified.
Check you didn't mess up the YAML definition by running our `metadata validator <https://github.com/ai4os/ai4-metadata>`__:

.. code-block:: console

    $ pip install ai4-metadata
    $ ai4-metadata validate ai4-metadata.yml
