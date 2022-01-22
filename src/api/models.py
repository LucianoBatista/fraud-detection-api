from sqlalchemy.sql import func
from src import db


class Model(db.Model):

    __tablename__ = "model"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    modelname = db.Column(db.String(128), nullable=False)

    def __init__(self, id, modelname):
        self.id = id
        self.modelname = modelname
