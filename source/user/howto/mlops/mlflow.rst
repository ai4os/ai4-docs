MLflow Experiment Tracking
==========================

Experiment Tracking and Model versioning in MLflow
--------------------------------------------------

* ``Step-1: Register for an account in mlflow``:

Navigate to: `SIGN UP <https://mlflow.dev.ai4eosc.eu/signup>`_ for self registration. You will see the UI:

.. image:: /_static/images/mlflow_self_registration.png
   :width: 500 px

.. note::
    Only members of vo.ai4eosc.eu are allowed to register!

For more check the following documentation:
:doc:`Authentication for the AI4OS stack </user/overview/auth>`_

Then the next window below will be shown, read and accept `Privacy Policy <https://website.with.policy/privacy-policy/>`__ and `Terms of Use <https://website.with.policy/acceptable-use-policy/>`__

In case you want to change the password you can enter a new password in the textbox "Password" and then click Update button.
Except for the username, if registered or not, password you have also the option to view what are your experiments and registered models with respective permissions
and other relevant attributes.

There are two other options at the bottom of the page: `Delete account` and `Log out`
Once you are logged in, you can start logging your experiment.

Authenticate in the MLFlow UI (frontend interface) with your credentials (via email ): e.g. as follows:
At the bottom of the page there is the option to go to MLflow UI, click the button: **Go to mlflow** then you will be redirected to MLflow login page
where you have to authenticate based on the previous credentials you used during registration.

.. image:: /_static/images/mlflow_login.png
   :width: 500 px

Once you login you will see the default MLflow UI as follows,

.. image:: /_static/images/mlflow_ui.png
   :width: 500 px


* ``Step-2: Log your Experiment(s)``:

Once your are logged in you can start logging your experiments and saving (best) trained model with a version in Model Registry:

1. First install mlflow client from the IDE that you are using to build your AI model, by executing:

  .. code-block:: console

      pip install mlflow[extras]

2. Edit your code to insert MLflow constants (env vars) and statements so that your experiments will be logged to the tracking server we deployed

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
      MLFLOW_REMOTE_SERVER="https://mlflow.dev.ai4eosc.eu" 
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

      

   
3. We provide `some examples of mlflow implementations <https://codebase.helmholtz.cloud/m-team/ai/mlflow-tutorial/>`__
   to serve as reference or a concrete integration of mlflow once you have created your api in the Marketplace: `yolov8 mlflow <https://codebase.helmholtz.cloud/m-team/ai/yolov8_api/-/tree/mlflow?ref_type=heads>`

.. note::
    For more information, see the *Getting Started* step by step guide available in the `mlflow  <https://mlflow.org/docs/latest/getting-started/index.html>`__.

* ``Step-3: Save your models into Model Registry``:
   .. code-block:: python

      # REGISTER MODEL to MODEL REGISTRY #
      result = mlflow.register_model(
      f"runs:/{run_id}/artifacts/", MLFLOW_MODEL_NAME
      )