import pytest

from app import create_app
from app.extensions.database import DB


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


@pytest.fixture
def client(app):
    return app.test_client()


def test_register_user(client):
    data = {
        "username": "testuser",
        "password": "Testpassword1!",
        "role": "user",
        "email": "test@example.com",
        "mobile": "8178757545",
        "first_name": "John",
        "last_name": "Doe",
        "company_id": "1",
    }
    response = client.post("/auth/register", json=data)

    assert response.status_code == 201
    assert response.json["message"] == "User created"
    assert response.json["user"]["username"] == "testuser"
    assert response.json["user"]["role"] == "user"
    assert response.json["user"]["email"] == "test@example.com"
    assert response.json["user"]["mobile"] == "8178757545"

    with open("logs/endpoint_tests.log", "a") as f:
        f.write(
            f"""Test Register User Response: {response.json}\n==============\n    endpoint: /auth/register\n==============\n   data: {data}\n==============\n"""
        )

def test_register_user_invalid(client):
    data = {
        "username": "tes",
        "password": "testpassword",
        "role": "user",
        "email": "test@example.com",
        "mobile": "8178757545",
        "first_name": "John",
        "last_name": "Doe",
        "company_id": "1",
    }
    response = client.post("/auth/register", json=data)

    with open("logs/endpoint_tests.log", "a") as f:
        f.write(
            f"""Test Register User Invalid Response: {response.json}\n==============\n    endpoint: /auth/register\n==============\n   data: {data}\n==============\n"""
        )
    assert response.status_code == 400
