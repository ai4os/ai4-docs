Experiment Tracking and Model versioning in MLflow
==================================================

We currently have two instances of MLflow running:

* `MLflow AI4EOSC <https://mlflow.cloud.ai4eosc.eu>`__
* `MLflow iMagine <https://mlflow.cloud.imagine-ai.eu>`__

When following this tutorial, adapt the MLflow links depending on which
:doc:`Project or Virtual Organization you belong to </reference/user-access-levels>`.

In case you already have a MLflow account, you can proceed to step 2.


1. Register for an account in MLflow
-------------------------------------

Go to the Sign Up page for self registration in MLflow:

* AI4EOSC: `Sign Up page <https://mlflow.cloud.ai4eosc.eu/signup>`__
* iMagine: `Sign Up page <https://mlflow.cloud.imagine-ai.eu/signup>`__

.. image:: /_static/images/mlflow/self-registration.png
   :width: 500 px

Then, in the next window:

* insert your password.
* read and accept the Privacy Policy and Terms of Use.

Finally you will be shown your user settings:

* In case you want to change the password you can enter a new password in the text box
  ``Password`` and then click the ``Update`` button.
* You can check your user info (your ``username`` is your email!)
* You have also the option of deleting your account as well as logging out.

Once you are ready, proceed to the new step by clicking in ``Go to mlflow``.


2. Login the MLflow UI
----------------------

In the `MLflow login page <https://mlflow.cloud.ai4eosc.eu/signup>`__ you will be asked
to input your credentials:

* ``Username``: the email associated with your :doc:`authentication
  </getting-started/register>`
  account
* ``Password``: the password you choose in step 1.

Once you login, you will see the default MLflow UI as follows:

.. image:: /_static/images/mlflow/ui.png
   :width: 1000 px


3. Log your Experiments
-----------------------

Now you are ready to start logging in your experiments and saving the (best)
trained model with a version in Model Registry.

For this you have to do the following steps in your deployment.

1. First install mlflow client from the IDE that you are using to build your AI model,
   by executing:

   .. code-block:: console

       $ pip install mlflow[extras]

2. Edit your code to insert MLflow constants (env vars) and statements so that your
   experiments will be logged to the tracking server we deployed.

   .. code-block:: python

      import mlflow
      # IMPORTANT CONSTANTS TO DEFINE
      # MLflow User Credentials
      MLFLOW_TRACKING_USERNAME = input('Enter your username: ')
      MLFLOW_TRACKING_PASSWORD =  getpass.getpass()  # inject password by typing manually
      # for MLFLow-way we have to set the following environment variables
      os.environ['MLFLOW_TRACKING_USERNAME'] = MLFLOW_TRACKING_USERNAME
      os.environ['MLFLOW_TRACKING_PASSWORD'] = MLFLOW_TRACKING_PASSWORD
      # Remote MLflow server
      MLFLOW_REMOTE_SERVER="https://mlflow.cloud.ai4eosc.eu"
      #Set the MLflow server and backend and artifact stores
      mlflow.set_tracking_uri(MLFLOW_REMOTE_SERVER)
      # Name of the experiment (e.g. name of the code repository)
      MLFLOW_EXPERIMENT_NAME="your_experiment_name"
      # Name of the model to train. HAS TO BE UNIQUE, Please, DEFINE ONE!
      MLFLOW_MODEL_NAME="your_model_name"

      #MLflow specific statements to log your experiment
      #Insert the following statements in your code where you are training your model,e.g.
      def train_model():
         # your existing code here

         history = model.fit(X_train, y_train, epochs=100, batch_size=64,
                     validation_data=(X_val, y_val), callbacks=[early_stopping])

         with mlflow.start_run(): # mlflow starting command

            # Log metrics to MLflow for each epoch
             batch_size = 10  # Log metrics every 10 epochs (adjust as needed)
             for epoch, (loss, val_loss) in enumerate(zip(history.history["loss"],
                                                      history.history["val_loss"])):
               if epoch % batch_size == 0:
                 mlflow.log_metric("train_loss", loss, step=epoch)
                 mlflow.log_metric("val_loss", val_loss, step=epoch)

            # Log params
            mlflow.log_params({
              "hidden_units": 100,
              "activation": "relu",
              "epochs": 100,
              "batch_size": 64,
              "validation_split": 0.2
            })

            # Log model using: mlflow.<flavor>.log_model()
            # Log the TensorFlow using mlflow.tensorflow.log_model
            mlflow.tensorflow.log_model(model, artifact_path='artifacts')

            # Log additional artifacts
            # Log the CSV file as an artifact in MLflow
            mlflow.log_artifact(data_csv, artifact_path='artifacts/dataset')


We provide some `examples of mlflow implementations <https://codebase.helmholtz.cloud/m-team/ai/mlflow-tutorial/>`__
to serve as reference, as well a `specific integration of mlflow <https://codebase.helmholtz.cloud/m-team/ai/yolov8_api/-/tree/mlflow?ref_type=heads>`__ once you have created your api in the Marketplace.

For more information, see the `Getting Started <https://mlflow.org/docs/latest/getting-started/index.html>`__
guide in the official MLflow docs.

Finally, to save the models in the registry, you have to add the following code in your
deployment:

.. code-block:: python

   # REGISTER MODEL to MODEL REGISTRY #
   result = mlflow.register_model(
      f"runs:/{run_id}/artifacts/", MLFLOW_MODEL_NAME
   )


4. MLflow AutoLogging and CustomLogging
---------------------------------------

There exists two Logging options as illustrated in the following Figures.

.. image:: /_static/images/mlflow/autolog-quickview.png
   :width: 1000 px

.. image:: /_static/images/mlflow/custom-log-quickview.png
   :width: 1000 px

**Important commands to know**

* Log Experiment-Run

.. code-block:: python

   # Log Param (Log a parameter under the current run):
   mlflow.log_param("batch_size", 64)
   # Log Params (Log multiple parameter under the current run):
   mlflow.log_params({"hidden_units": 100,
                     "activation": "relu",
                     "batch_size”:64,
                     "validation_split": 0.2})
   # Log Metric  (Log a metric under the current run):
   mlflow.log_metric("mse", 90.00)
   # Log Metric  (Log multiple metrics under the current run):
   mlflow.log_metrics({"mse": 90.00,
                     "rmse": 75.00})

* Log Artifact(s)

.. code-block:: python

   # Log Figure (Log a figure as an artifact)
   import matplotlib.pyplot as plt
   fig, ax  = plt.subplots()
   ax.plot ([1,2],[4,5])
   mlflow.log_figure(fig, "fig_plot.png")
   # Log a dataset (CSV format) as an artifact in MLflow
   mlflow.log_artifact(data_csv, artifact_path="artifacts")
