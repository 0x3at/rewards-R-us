from flask import Flask
from .extensions import (
    database,
    logger,
    restful,
    mail,
    auth
    )


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "secret"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    app.config["DEBUG"] = True

    database.register_extension(app)
    logger.register_extension(app)
    auth.register_extension(app)
    restful.register_extension(app)
    mail.register_extension(app)
    
    app.logger.info("Server build process completed...")
    return app
