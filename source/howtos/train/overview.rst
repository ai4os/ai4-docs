Training in AI4OS
=================

This page serves a guide on the different options to train a model in the AI4OS platform.

Training options
----------------

There are currently three main options to train a model in the AI4OS platform:

* :doc:`standard mode </howtos/train/standard>`:
  you are given access to a persistent deployment that you can interact with via an IDE (ie. VScode).

* :doc:`batch mode </howtos/train/batch>`:
  you deploy a temporary job that runs your training and then is killed when the training is completed

* :doc:`federated mode </howtos/train/federated>`:
  you deploy a federated learning server that orchestrates the training. Then you can have several clients joining forces to distribute the training load among all of them.


All these options have the respective pros and cons.

.. list-table:: Training options from the AI4OS Dashboard
    :header-rows: 1

    * - Option
      - ✅ Pros
      - ❌ Cons
    * - :doc:`Standard mode </howtos/train/standard>` (persistent deployment)
      - - It's very convenient to edit and run directly from an IDE,
      - - The GPU is dedicated to you full time, even when you are not actually training. Thus resources are not used optimally.
    * - :doc:`Batch mode </howtos/train/batch>` (temporary jobs)
      - - You are only using resources for as long as your training needs to run.

          :material-outlined:`stars;1.5em` *To promote the usage of batch mode between users, we have dedicated Tesla V100 GPU nodes exclusively devoted to batch mode.*
      - - Less convenient because you cannot debug from IDE.
    * - :doc:`Federated mode </howtos/train/federated>`
      - - You can scale your training across many deployments, mixing both GPU and CPU deployments, both inside and outside the AI4OS platform.
        - Your training data remain local, so it's a perfect match for privacy respecting usecases (eg. healthcare).
      - - Not all modules can be used for default in federated mode, you need to adapt their code first.
        - It might require a bit more work to setup.

Given the above specifications, we recommend the following typical workflows:

* :doc:`Use standard mode </howtos/train/standard>` for you preliminary trainings, when you still might need to have direct access to the code/data to debug things.
* :doc:`Use batch mode </howtos/train/batch>` when your training script is stable, and you are basically tweaking hyperparameters.
* :doc:`Use federated mode </howtos/train/federated>` if you have sensitive data and/or need to distribute you training across many machines.


Additional training-related tasks
---------------------------------

We have a tutorials on additional training-related tasks:

* :doc:`Label your sdata with CVAT </howtos/train/cvat>`
* :doc:`Use MLflow to track your training runs </howtos/train/federated>`

If you are new to Machine Learning, you might want to check some :doc:`useful Machine Learning resources </others/useful-ml-resources>` we compiled to help you getting started.
