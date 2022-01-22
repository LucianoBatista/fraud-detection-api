from datetime import date, datetime
from email.policy import default
from sqlalchemy.sql import func
from src import db


class Model(db.Model):

    __tablename__ = "model"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    modelname = db.Column(db.String(128), nullable=False, unique=True)
    precision = db.Column(db.Float, nullable=False)
    recall = db.Column(db.Float, nullable=False)
    accuracy = db.Column(db.Float, nullable=False)
    auc = db.Column(db.Float, nullable=False)
    f1 = db.Column(db.Float, nullable=False)
    time = db.Column(db.Float, nullable=False)
    enabled = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    predicts = db.relationship("Predict", backref="model", lazy=True)


class Predict(db.Model):

    __tablename__ = "predict"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    transaction = db.Column(db.JSON, nullable=False)
    prediction = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.now, index=True)
    model_id = db.Column(db.Integer, db.ForeignKey("model.id"), nullable=False)
