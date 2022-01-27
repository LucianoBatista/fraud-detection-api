from importlib.metadata import requires
from flask import request
from flask_restx import Resource, Namespace, fields
from src.pipelines.pipelines import prediction

from src.pipelines.utils import predict

import pandas as pd

predict_namespace = Namespace("Predict")

predict_schema = predict_namespace.model(
    "Predict",
    {
        "day_of_month": fields.Integer(required=True),
        "type": fields.String(required=True),
        "amount_log": fields.Float(required=True),
        "amount_dest": fields.Float(required=True),
    },
)


class Predict(Resource):
    @predict_namespace.expect(predict_schema, validate=True)
    def post(self):
        content = request.get_json()
        day_of_month = content["day_of_month"]
        transaction_type = content["type"]
        amount_log = content["amount_log"]
        amount_dest = content["amount_dest"]

        # data
        data = {
            "day_of_month": day_of_month,
            "type": transaction_type,
            "amount_log": amount_log,
            "amount_dest": amount_dest,
        }

        data_df = pd.DataFrame(data, index=[0])

        # do the prediction
        predictions = predict(data_df)
        predictions = [int(prediction) for prediction in predictions]

        return {"predictions": predictions}


predict_namespace.add_resource(Predict, "/predict")
