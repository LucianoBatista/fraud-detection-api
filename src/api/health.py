from flask_restx import Model, Resource, Namespace
from src.database.crud import model_crud

model_healthy_namespace = Namespace("Model-Healthy")


class ModelHealthy(Resource):
    def get(self):
        obj = model_crud.get_metrics()
        response = {
            "modelname": obj.modelname,
            "accuracy": obj.accuracy,
            "recall": obj.recall,
            "f1": obj.f1,
            "enabled": obj.enabled,
        }
        return response, 200


model_healthy_namespace.add_resource(ModelHealthy, "/healthy")
