from re import U
from flask.app import Flask
import sys
from flask.cli import FlaskGroup
from src import create_app, db

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command("recreate_db")
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    """Will populate our database just for initial test"""
    ...


if __name__ == "__main__":
    cli()
