from flask import Flask
from .extensions import database


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "secret"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    app.config["DEBUG"] = True

    database.register_extension(app)

    return app
