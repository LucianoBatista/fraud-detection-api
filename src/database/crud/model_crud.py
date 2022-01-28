from black import Mode
from src.api.models import Model, TrainingQueue
from src import db


def get_metrics():
    obj = Model.query.filter_by(enabled=True).first()
    return obj


def get_status(model_id: int):
    obj = TrainingQueue.query.filter_by(id=model_id).first()
    return obj


def update_model(model_id: int):
    obj = Model.query.filter_by(id=model_id).first()
    obj.enabled = 0
    db.session.commit()


def add_model(model: Model):
    db.session.add(
        Model(
            modelname="other_model.sav",
            precision=model.get("precision"),
            recall=model.get("recall"),
            accuracy=model.get("accuracy"),
            auc=model.get("auc"),
            f1=model.get("f1"),
            time=model.get("time"),
            enabled=model.get("enabled"),
        )
    )
    db.session.commit()


def queue_model(dataset: str, status: str):
    queue_model_obj = TrainingQueue(dataset=dataset, status=status)
    db.session.add(queue_model_obj)
    db.session.commit()
    id = queue_model_obj.id
    return id
