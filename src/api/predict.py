from importlib.metadata import requires
from flask import request
from flask_restx import Resource, Namespace, fields
from src.pipelines.pipelines import prediction

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

        # do the prediction
        payload = {
            "step": 2,
            "type": 888,
            "amount": 2000000,
            "oldbalanceDest": 58858,
            "newbalanceDest": 0,
            "isFlaggedFraud": 0,
        }
        pkl_model_path = "src/models/lrc_baseline.sav"
        y_pred = prediction(pkl_model_path, payload)
        y_pred_float = float(y_pred)
        return {"y_pred": y_pred_float}


predict_namespace.add_resource(Predict, "/predict")
