# type: ignore
import pytest

from app import create_app
from app.extensions.database import DB
from app.models.user import User
from app.models.companies import Companies
from app.interfaces.userinterface import UserInterface

from . import tools


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
        tools.setup_qa_db(DB.session, User, Companies)
        yield DB.session
        DB.session.rollback()


def test_get_single_user(DB_session):
    user = UserInterface.get(1)
    assert user is not None
    assert user.id == 1


def test_get_multiple_users(DB_session):
    users = UserInterface.get([1, 2])
    assert len(users) == 2
    assert users[0].id == 1
    assert users[1].id == 2


def test_get_user_by_username(DB_session):
    user = UserInterface.get(username="user1")
    assert user is not None
    assert user.username == "user1"


def test_get_user_by_email(DB_session):
    user = UserInterface.get(email="user2@example.com")
    assert user is not None
    assert user.email == "user2@example.com"


def test_get_user_by_mobile(DB_session):
    user = UserInterface.get(mobile="157.214.183.171")
    assert user is not None
    assert user.mobile == "157.214.183.171"


def test_invalid_user_id(DB_session):
    with pytest.raises(KeyError):
        UserInterface.get(1000)


def test_invalid_user_ids(DB_session):
    with pytest.raises(KeyError):
        UserInterface.get([1004, 2004])


def test_invalid_username(DB_session):
    with pytest.raises(KeyError):
        UserInterface.get(username="invalid_username")


def test_invalid_email(DB_session):
    with pytest.raises(KeyError):
        UserInterface.get(email="invalid_email@example.com")


def test_invalid_mobile(DB_session):
    with pytest.raises(KeyError):
        UserInterface.get(mobile="invalid_mobile")


def test_invalid_arg_types(DB_session):
    with pytest.raises(TypeError):
        UserInterface.get("invalid_arg")
    with pytest.raises(TypeError):
        UserInterface.get(username=123)
    with pytest.raises(TypeError):
        UserInterface.get(email=123)
    with pytest.raises(TypeError):
        UserInterface.get(mobile=123)
    with pytest.raises(KeyError):
        UserInterface.get(123, username="user1")
    with pytest.raises(KeyError):
        UserInterface.get(email="123")
