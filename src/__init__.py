import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# instantiate the db
db = SQLAlchemy()


def create_app(script_info=None):
    app = Flask(__name__)

    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)
    app.config["RESTX_ERROR_404_HELP"] = False  # do not change some outputs

    db.init_app(app)

    # register flask blueprints
    from src.api.ping import ping_blueprint
    from src.api.ml_model import ml_model_blueprint

    app.register_blueprint(ping_blueprint)
    app.register_blueprint(ml_model_blueprint)

    # shell context for flask cli
    # allow us to investigate some things with db and the app
    # from command line
    def ctx():
        return {"app": app, "db": db}

    return app
