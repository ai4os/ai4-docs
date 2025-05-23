Distributed Learning
====================

Essentially, carrying out the training of AI/ML/DL models in a distributed way can be done due to two fundamental reasons: the first one is that there are privacy issues that prevent to centralize the data in a single site, the second one is that due to the need of computational resources the training must be distributed in different workers (e.g. the model or the data do not fit in memory). Thus, we can consider two main paradigms to carry out distributed machine learning (DML):

* **Data parallelism:** this is the most common case, and is used when the data avilable for training the model does not fit in memory in a single node or worker. Thus, the data is distributed among the different available workers or machines. Then, the model is trained on each data subset and the resulting model is aggregated using the parameters obtained in each case.

* **Model parallelism:** the model, usually a neural network, is split and distributed among different available computation nodes. An important aspect here is to ensure a correct synchronization and coordination between the different workers when performing gradient descent and backward propagation. This method is used in case of very large models that do not fit in memory.

From the point of view of the development and training of a model in a distributed way using the AI4OS platform, the following solutions are proposed depending on the user's needs:

* **The data is distributed in different sites naturally or artificially outside the AI4OS platform**. There are different computing nodes allocating the different datasets. For this approach, we propose to perform the distributed training using the :doc:`federated server </howtos/train/federated-flower>` deployed on the platform, since the federated learning (FL) architecture can be seen as an specific case of DML where data parallelism (data distributed on different nodes) is performed. Thus, in each computing node or worker, a client of the federated architecture will be created, and a deployment will be created in AI4OS using the federated server tool to be in charge of orchestrating the distributed architecture.

* **The data is distributed naturally or artificially and can be uploaded to the AI4OS platform.** In this case, as in the previous one, the user can distribute each dataset to a deployment created on the platform, each of these constituting a worker in a DML architecture. As in the previous case, to carry out the distributed training in this case, the :doc:`federated server </howtos/train/federated-flower>` can be used, deploying this tool in another deployment and creating a client in each of the deployments provided with distributed data previously created.

* **The user wants to train a model on a large dataset. The model is complex enough to require the use of multiple GPUs.** You would create a multi-GPU deployment in AI4OS, upload the data to it and train the model in a distributed way using `horovod <https://horovod.ai/>`__. Below is an example that can be followed, specifically applied to the `CIFAR100 <https://www.cs.toronto.edu/~kriz/cifar.html>`__ dataset using `Tensorflow <https://www.tensorflow.org/>`__ (it would be enough to replace the configuration related to this use case to extrapolate it to the user case).

.. admonition:: Note
   :class: info

   Due to the restricted number of GPUs, for optimal usage, we currently do not support creating multi-GPU deployments.

  .. code-block:: python

    import tensorflow as tf
    import horovod.tensorflow as hvd
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Conv2D
    from tensorflow.keras.layers import MaxPooling2D
    from tensorflow.keras.layers import BatchNormalization
    from tensorflow.keras.layers import Dropout
    from tensorflow.keras.layers import Flatten
    from tensorflow.keras.layers import Dense
    from tensorflow.keras.utils import to_categorical

    # Initialize Horovod
    hvd.init()

    # Pin GPU to be used to process local rank (one GPU per process)
    gpus = tf.config.experimental.list_physical_devices('GPU')
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)
    if gpus:
        tf.config.experimental.set_visible_devices(gpus[hvd.local_rank()], 'GPU')

    # Read the process the data
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar100.load_data()
    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0
    y_train = to_categorical(y_train, 100)
    y_test = to_categorical(y_test, 100)

    dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))
    dataset = dataset.repeat().shuffle(10000).batch(128)

    # Create the model to be trained:
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        Flatten(),
        Dense(64, activation='relu'),
        Dense(100, activation='softmax')
    ])

    loss = tf.losses.CategoricalCrossentropy()
    opt = tf.optimizers.Adam(0.001 * hvd.size())
    metrics = ['accuracy']
    model.compile(optimizer=opt, loss=loss, metrics=metrics)

    checkpoint_dir = './checkpoints'
    checkpoint = tf.train.Checkpoint(model=model, optimizer=opt)

    @tf.function
    def training_step(x_train, y_train, first_batch):
        with tf.GradientTape() as tape:
            probs = model(x_train, training=True)
            loss_value = loss(y_train, probs)

        # Add Horovod Distributed GradientTape.
        tape = hvd.DistributedGradientTape(tape)
        grads = tape.gradient(loss_value, model.trainable_variables)
        opt.apply_gradients(zip(grads, model.trainable_variables))

        # Broadcast initial variable states from rank 0 to all other processes.
        # This is necessary to ensure consistent initialization of all workers when
        # training is started with random weights or restored from a checkpoint.
        # Note: broadcast should be done after the first gradient step to ensure optimizer
        # initialization.
        if first_batch:
            hvd.broadcast_variables(model.variables, root_rank=0)
            hvd.broadcast_variables(opt.variables(), root_rank=0)

        return loss_value

    # Horovod: adjust number of steps based on number of GPUs.
    for batch, (x_train, y_train) in enumerate(dataset.take(10000 // hvd.size())):
        loss_value = training_step(x_train, y_train, batch == 0)

        if batch % 10 == 0 and hvd.local_rank() == 0:
            print('Step #%d\tLoss: %.6f' % (batch, loss_value))

    # Save checkpoints only on one worker (e.g. worker 0):
    if hvd.rank() == 0:
        checkpoint.save(checkpoint_dir)
