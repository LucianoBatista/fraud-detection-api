from flask import Blueprint, jsonify, request
from flask_restx import Api, Resource

from src.celery.tasks import async_workflow

ml_model_blueprint = Blueprint("training", __name__)
predict_blueprint = Blueprint("predict", __name__)
metrics_blueprint = Blueprint("metrics", __name__)

api = Api(ml_model_blueprint)


class MlModel(Resource):
    """Endpoint related to the training of the model"""

    def get(self):
        return {"accuracy": 0.987, "auc": 0.877, "recall": 0.766}

    def post(self):
        content = request.get_json()
        url = content["url"]
        task = async_workflow.delay(str(url))
        print(task)
        return {"task_id": task.id}, 202


api.add_resource(MlModel, "/training")
# api.add_resource(Predict, "/predict")
# api.add_resource(CheckHealthy, "/metrics")
