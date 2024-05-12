# type: ignore
from flask import make_response, Response

from flask_login import login_user as flask_login_user

from ...interfaces import UserInterface
from ...types.exceptions import LoggedError


def login_user(username: str, plaintext_password: str, remember: bool = False)-> Response:
    response_headers= {"Content-Type": "application/json"}

    try:
        authenticated = UserInterface.check_password(username, plaintext_password)

        if authenticated:
            user = UserInterface.get_user_by_username(username)
            flask_login_user(user, remember)
            response = make_response(
                {"message": "User authenticated", "user": user.sanitize()}
            )
            response.status_code = 200

        else:
            response = make_response({"message": "Invalid username or password"})
            response.status_code = 401

    except LoggedError as e:

        response = e.response

    return response
