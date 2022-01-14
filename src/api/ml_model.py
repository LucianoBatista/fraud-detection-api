from flask import Blueprint
from flask_restx import Api, Resource

ml_model_blueprint = Blueprint("mlmodel", __name__)
api = Api(ml_model_blueprint)


class MlModel(Resource):
    def get(self):
        return {"accuracy": 0.987, "auc": 0.877, "recall": 0.766}


api.add_resource(MlModel, "/mlmodel")
