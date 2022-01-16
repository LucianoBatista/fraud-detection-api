from tokenize import Name
from flask import Blueprint, jsonify, request
from flask_restx import Api, Resource, Namespace

from src.celery.tasks import async_workflow

ml_model_namespace = Namespace("training")


class MlModel(Resource):
    """Endpoint related to the training of the model"""

    def post(self):
        content = request.get_json()
        url = content["url"]
        task = async_workflow.delay(str(url))
        print(task)
        return {"task_id": task.id}, 202


class MlModelStatus(Resource):
    """Endpoint to collect the information about the training of the model"""

    def get(self, model_id: int):
        print(model_id)
        return {"accuracy": 0.987, "auc": 0.877, "recall": 0.766}


ml_model_namespace.add_resource(MlModel, "/training")
ml_model_namespace.add_resource(MlModelStatus, "/training/<int:model_id>")
# api.add_resource(Predict, "/predict")
# api.add_resource(CheckHealthy, "/metrics")
