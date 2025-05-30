Train a model
^^^^^^^^^^^^^

This section will guide you through the process of training a model with the Dashboard,
and some other aspects that influence the training process, like labeling your images
with CVAT, or using rclone to sync your dataset. Also, you will learn how to make a
federated learning training.

.. grid:: 1
    :gutter: 3

    .. grid-item-card:: :fas:`brain;fa-lg sd-mr-2`  Train a model in standard mode
        :link: standard
        :link-type: doc

        Learn how to train a model in standard mode.

    .. grid-item-card:: :fas:`brain;fa-lg sd-mr-2`  Train a model in batch mode
        :link: batch
        :link-type: doc

        Learn how to train a model in batch mode.

    .. grid-item-card:: :material-outlined:`hub;1.5em`  Run a federated learning training
        :link: federated
        :link-type: doc

        Learn how to make a federated learning training, both with the Flower and NVFLARE frameworks

    .. grid-item-card:: :material-outlined:`sell;1.5em`  Label your images with CVAT
        :link: cvat
        :link-type: doc

        Learn how to label your images with CVAT.

    .. grid-item-card:: :material-outlined:`sync;1.5em`  Use rclone to sync your dataset (advanced)
        :link: rclone
        :link-type: doc

        Learn how to use rclone to sync your dataset.

.. toctree::
   :caption: Train a model
   :maxdepth: 1
   :titlesonly:
   :hidden:

   Overview <overview>
   Train a model (standard mode) <standard>
   Train a model (batch mode) <batch>
   Run a federated learning training <federated>
   Label your images with CVAT <cvat>
   Use rclone to sync your dataset (advanced) <rclone>
