from src.api.models import Model


def get_metrics():
    obj = Model.query.filter_by(enabled=True).first()
    return obj
