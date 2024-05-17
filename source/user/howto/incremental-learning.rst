Incremental (online) Learning
=============================

Usually, when developing machine or deep learning models we can encounter problems in the assumption of training them with non-stationary stream data. In many research papers this type of learning is referred to as continuous learning. It is important to note that incremental deep learning arises in order to solve the problem of loss of predictive capability of the models in cases of non-stationary streams of data. This is important in cases where the trend of the data can change quickly, as well as their distributions. 

Meanwhile, this is clearly related to data drift detection in machine or deep learning scenarios. Specifically, in an incremental learning scenario, the model to be trained does not have all the data at the beginning, but they arrive sequentially or in different steps, which may cause the distributions to vary over time. The idea is that the model is able to adapt to new data without losing the knowledge previously acquired. From a theoretical point of view, three types of incremental learning data are proposed in [1], task-incremental learning, domain-incremental learning and class-incremental learning.

In particular, if you are applying machine learning models such as those available in scikit-learn, you can use river to migrate your model from batch learning (classic) to incremental (or online) learning. In particular, we recommend reviewing the example given at [2], where online learning is applied to the widely known AirlinePassengers dataset (contains the number of air-passengers per month). This example is reproduced in the code below, so that new data is added to the dataset to make predictions and capture the trend. To do this we make use of the river pipelines, which according to the model to be applied (a linear regression in this case), apply different transformations to the data, such as get the ordinal date, apply one-hot encoding to the month name and linearly detrend the series using a TargetStandardScaler. 

1. Install river and pytest (this dependency is needed):

.. code-block:: console

    $ pip install river
    $ pip install pytest
    
2. Create the pipeline for processing the data, scaling and creating the model

.. code-block:: python

    from river import compose
    from river import linear_model
    from river import preprocessing
    from river import metrics
    from river import utils
    import calendar

    def get_ordinal_date(x):
        return {'ordinal_date': x['month'].toordinal()}
    
    def get_month(x):
        return {
           calendar.month_name[month]: month == x['month'].month
            for month in range(1, 13)
        }
    
    model = compose.Pipeline(
        # Features used as input for the model
        ('features', compose.TransformerUnion(
            ('ordinal_date', compose.FuncTransformer(get_ordinal_date)),
            ('month', compose.FuncTransformer(get_month)),
        )),
        # Scaling the data
        ('scale', preprocessing.StandardScaler()),
        # Applying the model
        ('lin_reg', linear_model.LinearRegression(intercept_lr=0))
    )
    

3. Evaluate the model applied using online learning and return the real values and the predictions 

.. code-block:: python

    def evaluate_model(model): 
        metric = utils.Rolling(metrics.MAE(), 12)

        y_true = []
        y_pred = []
        for x, y in datasets.AirlinePassengers():
            # Obtain the prior prediction and update the model with the next data
            pred = model.predict_one(x)
            model.learn_one(x, y)

            # Update the error metric
            metric.update(y, pred)

            # Save the true value and the prediction
            y_true.append(y)
            y_pred.append(pred)

        return y_true, y_pred
    

Using river, one of the goals is to create models that are robust to concept drift. In particular, for more information about this we recommend to check `Frouros <https://frouros.readthedocs.io>`__, a Python library for data drift and concept drift detection. Examples of use can be found on the same following a similar structure to the previous one so that pipelines (in this case from scikit-learrn) are applied to process the data, select the features and apply the desired model, and detect if concept drift is occurring. In this regard, we recommend to review [3].

The biggest problem with batch learning is that you need to retrain your model frequently (periodically in the presence of new data). Online or incremental learning is especially useful in environments where data arrives continuously or storing and processing large data sets all at once is not feasible. However, it is important to note that in most cases, for example when we are applying a deep learning model using TensorFlow, the batch learning will be sufficient and it is not necessary to apply online learning. Instead, we can retrain the model in mini-batches in case of new data or changes in the trend of the data. In this line, we will applyt incremental training as a learning technique where a model is updated and improved over time by training it on a new data while retaining from previous learned patterns. In this case, the deep learning model will be updated regularly with new data. 

For example, using tensorflow, to solve this problem of new data arriving, it is possible to explore the possibility of applying a specific retraining of the model. The following is an example for the MNIST dataset. 

1. Read and process the data. Let's assume that initially we only have 70% of the data (x_train_ini, y_train_ini). We train the initial model and save it.  

.. code-block:: python

    import tensorflow as tf
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Dense, Flatten
    from tensorflow.keras.datasets import mnist
    import time

    # Read and process:
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    x_train = x_train / 255.0
    x_test = x_test / 255.0
    y_train = tf.keras.utils.to_categorical(y_train, 10)
    y_test = tf.keras.utils.to_categorical(y_test, 10)

    # First training data used:
    x_train_ini = x_train[:int(0.7*len(x_train))]
    y_train_ini = y_train[:int(0.7*len(x_train))]

2. Define and compile the model

.. code-block:: python

    model = Sequential([
        Input(shape=(28,28,1)),
        Conv2D(32, kernel_size=(3, 3), activation="relu"),
        MaxPooling2D(pool_size=(2, 2)),
        Conv2D(64, kernel_size=(3, 3), activation="relu"),
        MaxPooling2D(pool_size=(2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

3. Train the model with the first batch of data available. Save the initial model

.. code-block:: python

    model.fit(x_train, y_train, epochs=10, batch_size=16, validation_split=0.2)
    model.save('initial_model.h5')
    
3. Create a logic to get new data (in this case we use x_train_new and y_train_new as new data), in a real case we should get that new data currently available.

.. code-block:: python

    def get_new_data(x_train, y_train):
        # In a real scenario here the new data that are available should be obtained. 
        # In this case, we take the remaining 30% of the data from the train set
        x_train_new = x_train[int(0.7*len(x_train)):]
        y_train_new = y_train[int(0.7*len(x_train)):]
        return x_train_new, y_train_new

4. Re-train the model periodically with the new data that will be obtained (in this case we do not obtain new data but take the final 30% of the train set, but this should be changed in a real case where new data are periodically available):

.. code-block:: python

    while True:
        x_train_new, y_train_new = get_new_data(x_train, y_train)
    
        if x_train_new is not None and y_train_new is not None:
            model = tf.keras.models.load_model('updated_model.h5')
            model.fit(x_train_new, y_train_new, epochs=5, batch_size=16, validation_split=0.2)
            model.save('updated_model.h5')
            print(f'Accuracy test: {model.evaluate(x_test, y_test)[1]}')
    
        # Repeat the process of acquiring new data and re-training the model periodically (e.g. every one hour).
        # Note: new data must be obtained, in this example the final 30% of the train set would be retaken.
        time.sleep(3600)
        

.. note::
    This approach can be followed by connecting your current deployment with a Nextcloud instance which is receiving new data periodically. 


[1] van de Ven, G.M., Tuytelaars, T. & Tolias, A.S. Three types of incremental learning. Nat Mach Intell 4, 1185–1197 (2022). https://doi.org/10.1038/s42256-022-00568-3.  

[2] River example (AirlinePassengers): https://riverml.xyz/latest/examples/building-a-simple-nowcasting-model.

[3] Frouros example (Elec2): https://frouros.readthedocs.io/en/latest/examples/concept_drift/DDM_simple.html.

