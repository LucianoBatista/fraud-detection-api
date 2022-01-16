from flask_restx import Api
from src.api.ml_model import ml_model_namespace
from src.api.status import ping_namespace

api = Api(version="1.0", title="Fraud Detection API", doc="/doc")

api.add_namespace(ping_namespace, path="/api/v1")
api.add_namespace(ml_model_namespace, path="/api/v1/model")
