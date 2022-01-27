from tokenize import Name
from flask import Blueprint, jsonify, request
from flask_restx import Api, Resource, Namespace, fields

from src.celery.tasks import async_workflow
from src.database.crud import model_crud

ml_model_namespace = Namespace("Training")

ml_model_schema = ml_model_namespace.model(
    "ML-Model", {"dataset": fields.String(required=True)}
)


class MlModel(Resource):
    """Endpoint related to the training of the model"""

    @ml_model_namespace.expect(ml_model_schema, validate=True)
    def post(self):
        content = request.get_json()
        dataset_url = content["dataset"]
        training_model_id = model_crud.queue_model(
            dataset=dataset_url, status="processing"
        )
        _ = async_workflow.delay(str(dataset_url), str(training_model_id))
        return {"id": training_model_id}, 201


class MlModelStatus(Resource):
    """Endpoint to collect the information about the training of the model"""

    def get(self, model_id: int):
        obj = model_crud.get_status(model_id)
        return {"status": obj.status}, 200


ml_model_namespace.add_resource(MlModel, "/training")
ml_model_namespace.add_resource(MlModelStatus, "/training/<int:model_id>")
