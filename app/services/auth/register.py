# type: ignore
from flask import make_response, Response
from flask_login import login_user as flask_login_user
from werkzeug.security import generate_password_hash
from validate_email_address import validate_email
import phonenumbers
from ...interfaces import UserInterface, InviteInterface
from ...types.exceptions import LoggedError
from ...utils.validation import is_password_valid


def register_user(
    username: str,
    plaintext_password: str,
    invite_code: str,
    email: str,
    mobile: str,
    first_name: str,
    last_name: str,
)-> Response:

    validity_check = {
        "username": len(username) > 3,
        "password": is_password_valid(plaintext_password),
        "email": validate_email(email),
        "mobile": phonenumbers.is_valid_number(phonenumbers.parse(mobile, "US")),
        "invite_code": InviteInterface.is_invite_valid(invite_code),
    }
        
    if validity_check == {k: True for k in validity_check}:
        password_hash = generate_password_hash(plaintext_password)
        
        invite = InviteInterface.get_invite_by_code(invite_code)

        try:
            user = UserInterface.add(
                username=username,
                password_hash=password_hash,
                balance=0,
                role=invite.role,
                email=email,
                mobile=mobile,
                first_name=first_name,
                last_name=last_name,
                company_id=invite.company_id,
            )
            
            flask_login_user(user)
            invite = InviteInterface.consume_invite(invite)
            response = make_response(
                {"message": "User created", "user": user.sanitize()}
            )
            response.status_code = 201

        except LoggedError as e:
            response = e.response

    else:
        invalid_args = [key for key in validity_check if not validity_check[key]]
        response = make_response(
            {"message": "Invalid input", "invalid_args": invalid_args}
        )

        response.status_code = 400
    
    return response
