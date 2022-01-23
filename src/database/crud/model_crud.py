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
            precision=model.precision,
            recall=model.recall,
            accuracy=model.accuracy,
            auc=model.auc,
            f1=model.f1,
            time=model.time,
            enabled=model.enabled,
        )
    )
    db.session.commit()
