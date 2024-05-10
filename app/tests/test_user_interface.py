# type: ignore
import pytest

from app import create_app
from app.extensions.database import DB
from app.models.user import User
from app.models.companies import Companies
from app.interfaces.users.user_interface import UserInterface
from app.types.exceptions import LoggedError

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


def test_get_100_users(DB_session):
    list_of_ids = [x for x in range(1, 100)]
    users = UserInterface.get(list_of_ids)
    for i in range(len(users)):
        assert users[i].id == i + 1


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
    with pytest.raises(LoggedError):
        UserInterface.get(1000)


def test_invalid_user_ids(DB_session):
    with pytest.raises(LoggedError):
        UserInterface.get([1004, 2004])


def test_invalid_username(DB_session):
    with pytest.raises(LoggedError):
        UserInterface.get(username="invalid_username")


def test_invalid_email(DB_session):
    with pytest.raises(LoggedError):
        UserInterface.get(email="invalid_email@example.com")


def test_invalid_mobile(DB_session):
    with pytest.raises(LoggedError):
        UserInterface.get(mobile="invalid_mobile")


def test_invalid_arg_types(DB_session):
    with pytest.raises(LoggedError):
        UserInterface.get("invalid_arg")
    with pytest.raises(LoggedError):
        UserInterface.get(username=123)
    with pytest.raises(LoggedError):
        UserInterface.get(email=123)
    with pytest.raises(LoggedError):
        UserInterface.get(mobile=123)
    with pytest.raises(LoggedError):
        UserInterface.get(123, username="user1")
    with pytest.raises(LoggedError):
        UserInterface.get(email="123")


def test_update_single_attribute(DB_session):
    user = User.query.get(1)
    updated_user = UserInterface.update_nonsecure(user=user, role="test")
    assert updated_user.role == "test"


def test_update_multiple_attributes(DB_session):
    user = User.query.get(2)
    updated_user = UserInterface.update_nonsecure(
        user=user, role="admin", first_name="Taylor"
    )
    assert updated_user.role == "admin"
    assert updated_user.first_name == "Taylor"


def test_update_non_existent_user(DB_session):
    with pytest.raises(LoggedError):
        UserInterface.update_nonsecure(user=User(id=1000))


def test_update_no_arguments(DB_session):
    with pytest.raises(LoggedError):
        UserInterface.update_nonsecure()


def test_update_invalid_arguments(DB_session):
    with pytest.raises(LoggedError):
        UserInterface.update_nonsecure(user="invalid_user_object")
    with pytest.raises(LoggedError):
        UserInterface.update_nonsecure(user=User(id=1), invalid_arg="invalid_value")
