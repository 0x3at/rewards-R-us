# type: ignore
from flask import make_response
from werkzeug.security import generate_password_hash
from validate_email_address import validate_email
import phonenumbers
from ...interfaces import UserInterface
from ...types.exceptions import LoggedError
from ...utils.validation import is_password_valid


def register_user(
    username: str,
    plaintext_password: str,
    role: str,
    email: str,
    mobile: str,
    first_name: str,
    last_name: str,
    company_id: str,
):
    response_headers = {"Content-Type": "application/json"}

    validity_check = {
        "username": len(username) > 3,
        "password": is_password_valid(plaintext_password),
        "email": validate_email(email),
        "mobile": phonenumbers.is_valid_number(phonenumbers.parse(mobile, "US")),
    }

    if validity_check == {k: True for k in validity_check}:
        password_hash = generate_password_hash(plaintext_password)

        try:
            user = UserInterface.add(
                username=username,
                password_hash=password_hash,
                balance=0,
                role=role,
                email=email,
                mobile=mobile,
                first_name=first_name,
                last_name=last_name,
                company_id=company_id,
            )

            response = make_response(
                {"message": "User created", "user": user.sanitize()}
            )
            response.headers = response_headers
            response.status_code = 201

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

    else:
        invalid_args = [key for key in validity_check if not validity_check[key]]
        response = make_response(
            {"message": "Invalid input", "invalid_args": invalid_args}
        )
        response.headers = response_headers
        response.status_code = 400

    return response
