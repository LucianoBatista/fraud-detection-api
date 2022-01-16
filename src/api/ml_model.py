from flask import Blueprint, jsonify, request
from flask_restx import Api, Resource

from src.celery.tasks import create_task

ml_model_blueprint = Blueprint("training", __name__)
api = Api(ml_model_blueprint)


class MlModel(Resource):
    def get(self):
        return {"accuracy": 0.987, "auc": 0.877, "recall": 0.766}

    def post(self):
        content = request.get_json()
        task_type = content["type"]
        task = create_task.delay(int(task_type))
        print(task)
        return {"task_id": task.id}, 202


api.add_resource(MlModel, "/training")
