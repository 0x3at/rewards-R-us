# type: ignore
from flask import make_response, Response

from ...interfaces import UserInterface
from ...types.exceptions import LoggedError


def login_user(username: str, plaintext_password: str):
    response_headers: dict[str, str] = {"Content-Type": "application/json"}

    try:
        authenticated = UserInterface.check_password(username, plaintext_password)

        if authenticated:
            user = UserInterface.get_user_by_username(username)
            response = make_response(
                {"message": "User authenticated", "user": user.sanitize()}
            )
            response.headers = response_headers
            response.status_code = 200

        else:
            response = make_response({"message": "Invalid username or password"})
            response.headers = response_headers
            response.status_code = 401

    except LoggedError as e:

        response = make_response(
            {
                "message": "Internal server error",
                "error": {
                    "id": e.id,
                    "func_name": e.func_name,
                    "message": str(e.exception),
                },
            }
        )
        response.headers = response_headers
        response.status_code = 500

    return response
