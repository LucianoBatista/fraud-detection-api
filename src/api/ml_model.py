from tokenize import Name
from flask import Blueprint, jsonify, request
from flask_restx import Api, Resource, Namespace, fields

from src.celery.tasks import async_workflow
from src.database.crud import model_crud

ml_model_namespace = Namespace("Training")

ml_model_schema = ml_model_namespace.model(
    "ML-Model", {"url": fields.String(required=True)}
)


class MlModel(Resource):
    """Endpoint related to the training of the model"""

    @ml_model_namespace.expect(ml_model_schema, validate=True)
    def post(self):
        content = request.get_json()
        url = content["url"]
        task = async_workflow.delay(str(url))
        print(task)
        return {"task_id": task.id}, 202


class MlModelStatus(Resource):
    """Endpoint to collect the information about the training of the model"""

    def get(self, model_id: int):
        obj = model_crud.get_status(model_id)
        return {"status": obj.status}, 200


ml_model_namespace.add_resource(MlModel, "/training")
ml_model_namespace.add_resource(MlModelStatus, "/training/<int:model_id>")
