from black import Mode
from src.api.models import Model, TrainingQueue


def get_metrics():
    obj = Model.query.filter_by(enabled=True).first()
    return obj


def get_status(model_id: int):
    obj = TrainingQueue.query.filter_by(id=model_id).first()
    return obj
