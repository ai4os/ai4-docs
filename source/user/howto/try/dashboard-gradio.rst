Try a model from the Dashboard (Gradio)
=======================================

Try-me deployments are available to anyone with an :ref:`EGI Check-In account <user/overview/auth:Basic authentication>`.

To create a deployment, :ref:`select a module in the Marketplace <user/overview/dashboard:Navigating the Marketplace>` and click on ``Try ▼ Nomad (Gradio)``.

.. image:: /_static/images/dashboard/module.png

This will open a new tab where the new try-me environment will be deployed (this can take a few seconds).

Once this is deployed, you will see a `Gradio <https://www.gradio.app/>`__ interface where you can make your prediction.
In the left hand-side, you will be shown the prediction inputs and in the right hand side you
will be shown the prediction outputs.

.. image:: /_static/images/endpoints/gradio.png

Take into account that this try-me endpoints are offered to the general public, thus run
on limited resources. This means that we limit the maximum duration of a try-me environment
to 10 minutes. In addition, resource-hungry operations (eg. video processing) might not work
as expected.

.. admonition:: Advice for model developers
    :class: info

    In some modules, prediction outputs might be shown as a raw JSON instead that with fancy
    Gradio fields. This is due to the developer failing the :ref:`user/overview/api:Integrate your model with the API`
    define an ``schema`` to validate their outputs.
    If you are the developer of the module, please consider defining a schema to
    improve the display of your module.
