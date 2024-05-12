# type: ignore
import time

from flask import make_response, Response

from app.interfaces import CompanyInterface, InviteInterface
from app.utils.email import send_invite
from app.types.exceptions import LoggedError

def add_company(name: str, admin_email:str)-> Response:
    response_headers = {"Content-Type": "application/json"}

    try:
        company = CompanyInterface.add(name)
        invite = InviteInterface.add(
            company_id=company.id,
            expiration=int(time.time()) + 3 * 24 * 60 * 60,
            role="admin",
            email=admin_email,
        )
        send_invite(email=admin_email, invite=invite, company=company)

        response = make_response(
            {
                "message": f"Company created, Admin invite has been sent to {admin_email}",
                "company": company.sanitize(),
            }
        )
        response.status_code = 201

    except LoggedError as e:
        response = e.response


    response.headers = response_headers
    return response
