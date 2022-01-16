from importlib.metadata import requires
from flask import request
from flask_restx import Resource, Namespace, fields

predict_namespace = Namespace("Predict")

predict_schema = predict_namespace.model(
    "Predict",
    {
        "step": fields.Integer(required=True),
        "type": fields.String(required=True),
        "amount": fields.Float(required=True),
    },
)


class Predict(Resource):
    @predict_namespace.expect(predict_schema, validate=True)
    def post(self):
        content = request.get_json()
        step = content["step"]
        transaction_type = content["type"]
        amount = content["amount"]

        # do the prediction

        return {"step": step, "type": transaction_type, "amount": amount}


predict_namespace.add_resource(Predict, "/predict")
