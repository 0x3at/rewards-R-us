from flask import make_response, Response

from flask_login import current_user

from app.interfaces import UserInterface
from app.types.exceptions import LoggedError

def get_all_users():
    try:
        company = current_user.company_id
        companies_users = UserInterface.call_table.query.filter_by(company_id=company).all()
        response = make_response(
            {"message": "Users retrieved", "users": [user.sanitize() for user in companies_users]}
        )
    except LoggedError as e:
        response = e.response

    return response
    
