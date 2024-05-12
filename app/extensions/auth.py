from flask import abort
from flask_login import LoginManager
from http import HTTPStatus


LOGIN = login = LoginManager()

def register_extension(app):
    
    LOGIN.init_app(app)
    
    return app


@LOGIN.user_loader
def load_user(user_id):
    from app.models import Users
    return Users.query.get(int(user_id))


@LOGIN.unauthorized_handler
def unauthorized():
    abort(HTTPStatus.UNAUTHORIZED)