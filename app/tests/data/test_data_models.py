import pytest
import shutil
from app import create_app
from app.extensions.database import DB
from app.extensions import database
from app.models.users import Users
from app.models.companies import Companies
from app.models.products import Products
from app.models.transactions import Transactions

from .. import tools


@pytest.fixture()
def app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        }
    )

    with app.app_context():
        DB.create_all()

    yield app

    with app.app_context():
        DB.drop_all()


@pytest.fixture()
def DB_session(app):
    with app.app_context():
        DB.session.begin_nested()
        tools.setup_qa_db(DB.session)
        yield DB.session
        shutil.copyfile("instance/db.sqlite", "app/tests/tools/mocks/qa_db.sqlite")
        DB.session.rollback()


def test_qa_setup(DB_session):
    user = Users.query.first()
    assert user is not None

    company = Companies.query.first()
    assert company is not None
