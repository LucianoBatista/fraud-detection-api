from re import U
from flask.app import Flask
import sys
from flask.cli import FlaskGroup
from src import create_app, db
from src.api.models import Model, Predict, TrainingQueue

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command("recreate_db")
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_model")
def seed_db():
    """Will populate our database just for initial test"""
    db.session.add(
        Model(
            modelname="lrc_baseline.sav",
            precision=0.964,
            recall=0.082,
            accuracy=0.997,
            auc=0.541,
            f1=0.153,
            time=26.77,
            enabled=True,
        )
    )
    db.session.commit()


@cli.command("seed_predict")
def seed_predict():
    db.session.add(Predict(transaction={"amount": 125}, prediction=1, model_id=1))
    db.session.commit()


@cli.command("seed_training")
def seed_trainning():
    db.session.add(TrainingQueue(dataset="htttp://data.csv"))
    db.session.commit()


if __name__ == "__main__":
    cli()
