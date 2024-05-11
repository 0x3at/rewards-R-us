from flask_sqlalchemy import (
    SQLAlchemy,
)  # ? https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/

DB = _db = SQLAlchemy()


def register_extension(app):
    DB.init_app(app)

    from ..models import (
        Companies,
        Users,
        Products,
        Transactions,
    )

    with app.app_context():
        DB.create_all()

    return DB
