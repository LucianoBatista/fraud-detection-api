from asyncio import create_task
import os

from flask import Flask
import flask_restx
from flask_sqlalchemy import SQLAlchemy
from celery import Celery

from src.celery_worker import make_celery

# instantiate the db
db = SQLAlchemy()


def create_app(script_info=None):
    app = Flask(__name__)

    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)
    app.config["RESTX_ERROR_404_HELP"] = False  # do not change some outputs

    # db init
    db.init_app(app)

    # register api
    from src.api import api

    api.init_app(app)

    # shell context for flask cli
    # allow us to investigate some things with db and the app
    # from command line
    def ctx():
        return {"app": app, "db": db}

    return app


# creating an instance of the app with celery
celery = make_celery(create_app())
