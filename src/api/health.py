from flask_restx import Model, Resource, Namespace


model_healthy_namespace = Namespace("Model-Healthy")


class ModelHealthy(Resource):
    def get(self):
        return {"accuracy": 0.987, "auc": 0.877, "recall": 0.766}


model_healthy_namespace.add_resource(ModelHealthy, "/healthy")
