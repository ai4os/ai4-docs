Useful Machine Learning resources
=================================

This is a piece of documentation trying to offer some advice on tools to
use to answer common problems (non ML expert) users might face.


AI4EOSC webinars
----------------
The AI4EOSC project has organized a series of webinars on the use of the platform (based on the AI4OS software stack), AI, machine learning, deep learning, image processing, image segmentation and other relevant topics. These can be accessed on YouTube at the following links:

* `Introduction to the platform <https://www.youtube.com/watch?v=op70toJFBrk>`__
* `Image processing with AI4EOSC <https://www.youtube.com/watch?v=JQOWmsEQANs>`__

.. warning::

   Please, be aware that video demos can become quickly outdated. In case of doubt, always refer to the written documentation.

Tutorials
---------

Here are some basic resources to get you quickly started in the Deep Learning / Machine Learning world.

Books
^^^^^

* *Deep Learning with Python*, F. Chollet
* *The FastAI book*
* *Deep Learning Book*, Ian Goodfellow

Courses
^^^^^^^

* `Google Machine Learning Crash Course <https://developers.google.com/machine-learning/crash-course>`__
* `Machine Learning Mastery <https://machinelearningmastery.com/start-here/>`__
* `DAIR ML YouTube Courses <https://github.com/dair-ai/ML-YouTube-Courses>`__
* `Stanford CS231N (2017): Introduction to Convolutional Neural Networks for Visual Recognition <https://www.youtube.com/playlist?list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv>`__
* `Stanford CS230 (2018): Deep Learning <https://www.youtube.com/playlist?list=PLoROMvodv4rOABXSygHTsbvUz4G_YQhOb>`__


Datasets
--------

Dataset labeling
^^^^^^^^^^^^^^^^

Some tools to help you getting started creating your dataset.

* `CVAT <https://www.cvat.ai/>`__ - Image annotation tool (with integration with the Segment Anything Model)
* `LabelStudio <https://labelstud.io/>`__ - General annotation (text, images, etc)
* `LabelImg <https://github.com/tzutalin/labelImg>`__ - Image annotation
* `refinery <https://github.com/code-kern-ai/refinery>`__ - Labeling for NLP
* `superintendent <https://github.com/janfreyberg/superintendent>`__ - ipywidget-based interactive labelling tool for your data.
* `VGG Image Annotator (VIA) <https://www.robots.ox.ac.uk/~vgg/software/via/>`__ - Image annotation
* `Biigle <https://biigle.de/>`__ - Web based annotation and exploration of images and videos
* `Roboflow <https://roboflow.com/annotate>`__ - only free is your dataset is public
* `Labelbox <https://labelbox.com/>`__ - paid tool (free with educational license)


Find a dataset
^^^^^^^^^^^^^^

If you don't have any data, try find an open dataset that suits you.

* `Google Dataset search <https://datasetsearch.research.google.com/>`__
* `Graviti Open Datassets <https://docs.graviti.com/guide/opendataset>`__
* `DataHub <https://datahub.io/collections>`__
* `Kaggle <https://www.kaggle.com/>`__
* `Paperwithcode Datasets <https://paperswithcode.com/datasets>`__
* `OpenML datasets <https://www.openml.org/search?type=data&status=active>`__
* `Dataworld datasets <https://data.world/datasets/agriculture>`__
* `Eden library <https://edenlibrary.ai/>`__ - agriculture datasets

Explore your dataset
^^^^^^^^^^^^^^^^^^^^

Less make sure the dataset does not contain errors.

* `Google's Know your data <https://knowyourdata.withgoogle.com/>`__ - only valid for common Tensorflow Datasets
* `Sweetviz <https://github.com/fbdesignpro/sweetviz>`__ - explore and compare tabular data
* `cleanlab <https://github.com/cleanlab/cleanlab>`__ - dataset cleaning
* `FastDup <https://github.com/visualdatabase/fastdup>`__ - dataset cleaning. Find anomalies, duplicate and near duplicate images, clusters of similarity, broken images, image statistics, wrong labels.
* `deepchecks <https://github.com/deepchecks/deepchecks>`__ - checks related to various types of issues, such as model performance, data integrity, distribution mismatches, and more.
* `kangas <https://github.com/comet-ml/kangas>`__ -  exploring, analyzing, and visualizing large-scale multimedia data
* `Impyute <https://github.com/eltonlaw/impyute>`__ - missing data

Feature selection
^^^^^^^^^^^^^^^^^

Some times less is more. Learn how to select the appropriate features of your dataset.

* `sklearn - feature selection <https://scikit-learn.org/stable/modules/classes.html#module-sklearn.feature_selection>`__
* `mlxtend <https://rasbt.github.io/mlxtend/>`__

Imbalanced learning
^^^^^^^^^^^^^^^^^^^

Do you have too much data from one class and too few from others. Let's balance things out!

* `Sklearn imbalanced <https://github.com/scikit-learn-contrib/imbalanced-learn>`__

Data augmentation
^^^^^^^^^^^^^^^^^

Do you have few data? Make the most out of it!

* `Augly <https://github.com/facebookresearch/AugLy>`__ - General augmentation (text, images, etc.)
* `imgaug <https://github.com/aleju/imgaug>`__ - Image augmentation

Dataset shift
^^^^^^^^^^^^^

Is your dataset likely to degrade over time (eg. cam gets dirty). Keep on eye on it!

* `Frouros <https://github.com/IFCA/frouros>`__
* `Alibi-detect <https://github.com/SeldonIO/alibi-detect>`__
* `Avalanche <https://github.com/ContinualAI/avalanche>`__ - Continual Learning library based on Pytorch
* `River <https://github.com/online-ml/river>`__ - Online learning
* `Cinnamon <https://github.com/zelros/cinnamon>`__
* `Eurybia <https://github.com/MAIF/eurybia>`__


Model development
-----------------

If you want to develop a model from scratch don't try to be a hero!
`Papers with Code <https://paperswithcode.com/>`__ gathers top performing models
for multiple tasks with their corresponding code. Reuse them for your usecases! Try not to look
for the top model but for the one with the cleanest code.

If you want nevertheless develop your model from scratch here are some recommendations.

Tensorflow related
^^^^^^^^^^^^^^^^^^

-  `Sonnet <https://github.com/deepmind/sonnet>`__
-  `TensorLayer <https://github.com/tensorlayer/TensorLayer>`__

Extensions for JAX:

-  `Flax <https://github.com/google/flax>`__ - NN library for JAX
-  `Haiku <https://github.com/deepmind/dm-haiku>`__ - Sonnet for JAX
-  `Trax <https://github.com/google/trax>`__ - like Keras for advanced
   deep learning
-  `Diffrax <https://github.com/patrick-kidger/diffrax>`__ - Numerical
   differential equation solvers in JAX
-  Others: `Equinox <https://github.com/patrick-kidger/equinox>`__

`Tensorflow
extensions <https://www.tensorflow.org/resources/libraries-extensions>`__:

-  `Tensorflow Quantum <https://www.tensorflow.org/quantum>`__
-  `TensorFlow Probability <https://www.tensorflow.org/probability>`__ -
   probabilistic reasoning and statistical analysis.
-  `Tensorflow Graph Neural
   Networks <https://blog.tensorflow.org/2021/11/introducing-tensorflow-gnn.html>`__
-  `Tensorflow Model Optimization Pruning
   API <https://medium.com/tensorflow/tensorflow-model-optimization-toolkit-pruning-api-42cac9157a6a>`__
   - build sparse models
-  `Tensorflow
   Similarity <https://blog.tensorflow.org/2021/09/introducing-tensorflow-similarity.html>`__
   - Entrenar modelos similares. Sirve también para Self Supervised
   Learning
   (`ref <https://blog.tensorflow.org/2022/02/boost-your-models-accuracy.html>`__).
-  `TF-GAN <https://github.com/tensorflow/gan>`__ - reproducible GANs
-  `Tensorflow Ranking <https://www.tensorflow.org/ranking>`__ -
   recommender systems
-  `TFX <https://www.tensorflow.org/tfx>`__ - production applications

Tensorflow tutorials:

-  https://github.com/vahidk/EffectiveTensorflow

Pytorch related
^^^^^^^^^^^^^^^

-  `Pytorch
   Lightning <https://github.com/Lightning-AI/pytorch-lightning>`__
-  `Pytorch image
   models <https://github.com/huggingface/pytorch-image-models>`__ - the
   largest collection of PyTorch image encoders / backbones. Including
   train, eval, inference, export scripts, and pretrained weights.
   Integrates the ``timm`` library
-  `Composer <https://github.com/mosaicml/composer>`__ - library with
   raining methods and best practices for efficent training
-  `Torchdim <https://github.com/facebookresearch/torchdim>`__
-  `PyTorch Tabular <https://github.com/manujosephv/pytorch_tabular>`__
   - for tabular data
-  `Pyro <https://github.com/pyro-ppl/pyro>`__ - Probabilistic
   programming
-  `VISSL <https://vissl.ai/>`__ - Self Supervised Learning
-  `TorchSSL <https://github.com/torchssl/torchssl>`__ - Semi Supervised
   Learning
-  `Kornia <https://github.com/kornia/kornia>`__ - accelerar image
   processing con GPUs. Lo puedo usar para depth estimation
-  `Torch Geo <https://github.com/microsoft/torchgeo>`__ - Geospatial ML
-  `TorchMetrics <https://torchmetrics.readthedocs.io/en/latest/>`__
-  `torchtyping <https://github.com/patrick-kidger/torchtyping>`__ -
   enforce torck type checks
-  `lovelytensors <https://github.com/xl0/lovely-tensors/>`__ - human
   friendly debigging of torch tensors
-  `skorch <https://github.com/skorch-dev/skorch>`__ - A scikit-learn
   compatible neural network library that wraps PyTorch.
-  `Additional
   optimizers <https://github.com/jettify/pytorch-optimizer>`__

Pytorch tutorials

-  https://pythonrepo.com/repo/ritchieng-the-incredible-pytorch
-  https://github.com/yunjey/pytorch-tutorial


Other
-----

Computing
^^^^^^^^^

Some useful non-AI packages to run computations:

-  `numba <https://github.com/numba/numba>`__ - see ``@jit`` decorator
-  `cython <https://github.com/cython/cython>`__
-  `numpy <https://github.com/numpy/numpy>`__ - *important*: Install
   OPENBLAS with Numpy to accelerate computation
-  `pandas <https://github.com/pandas-dev/pandas>`__
-  `xarray <https://docs.xarray.dev/>`__ - work better with
   multidimensional array by labelling dimensions
-  `numexpr <https://github.com/pydata/numexpr>`__ - accelerate Numpy
   computations
-  `intelex <https://intel.github.io/scikit-learn-intelex/>`__ - Intel
   extension to accelerate sklearn
-  `dask <https://github.com/dask/dask>`__ - parallel computation
-  `fugue <https://github.com/fugue-project/fugue>`__ - execute Python,
   pandas, and SQL code on Spark, Dask and Ray without rewrites
-  `FAISS <https://github.com/facebookresearch/faiss>`__ - efficient
   similarity search and clustering of dense vectors

GPU acceleration
^^^^^^^^^^^^^^^^

Some packages to accelerate non-AI operations with GPUs.

-  `pycuda <https://github.com/inducer/pycuda>`__
-  `triton <https://github.com/openai/triton>`__ - simple high performance GPU programming (openai)

You can use GPU based alternatives of common libraries for faster
performance:

* `cudf <https://github.com/rapidsai/cudf>`__ - alternative to Pandas
* `cuml <https://github.com/rapidsai/cuml>`__ - alternative to sklearn
* `cusignal <https://github.com/rapidsai/cusignal>`__ - alternative to scipy signal
* `cugraph <https://github.com/rapidsai/cugraph>`__ - for graph algorithms
* `cupatial <https://github.com/rapidsai/cuspatial>`__- for geospatial operations
* `cuxfilter <https://github.com/rapidsai/cuxfilter>`__ - accelerate visualization (Bokeh, DataShader, Panel, Falcon, Jupyter)

Training monitoring
^^^^^^^^^^^^^^^^^^^

Let's keep an eye on the training status.

* `Tensorboard <https://github.com/tensorflow/tensorboard>`__ - only works with Tensorflow
* `TensorboardX <https://github.com/lanpa/tensorboardX>`__ - framework agnostic
* `LabML <https://github.com/labmlai/labml>`__

Training debugging
^^^^^^^^^^^^^^^^^^

Is your training failing for some reason?

* `Netron <https://github.com/lutzroeder/netron>`__ - visualize DL models
* `Cockpit <https://github.com/f-dangel/cockpit>`__ - debug training

Model optimization
^^^^^^^^^^^^^^^^^^

Do you need your model to go faster?

* `VoltaML <https://github.com/VoltaML/voltaML>`__ - accelerate ML models with a single line of code
* `sparse-ml <https://github.com/neuralmagic/sparseml>`__
* `deep-sparse <https://github.com/neuralmagic/deepsparse>`__
* `Pytorch quantization <https://pytorch.org/docs/stable/quantization.html>`__
* `AItemplate <https://github.com/facebookincubator/AITemplate>`__ - transforms deep neural networks into CUDA (NVIDIA GPU) / HIP (AMD GPU) C++ code for lightning-fast inference serving
* `Hummingbird <https://github.com/microsoft/hummingbird>`__ - transform traditional Ml models (eg. Random Forest) to neural networks, and benefit from hardware acceleration
