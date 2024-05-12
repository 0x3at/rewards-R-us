from flask_mail import Message
from flask import current_app

from app.interfaces import InviteInterface
from app.extensions.mail import MAIL as mail


def send_invite(email, invite, company):
    """
    Sends an invite to the user.

    Args:
        email (str): The email of the user to send the invite to.
        role (str): The role the user will have when using the invite.
        company_id (int): The unique identifier for the company associated to the invite.
        days_before_expiration (int): The number of days before the invite expires.
    """
    email = Message(
        subject="You have been invited to join Rewards-R-Us!",
        recipients=[email],
        body=f"You have been invited to join the company {company.name}. To accept the invite, click on the following link: rewards-r-us.dunderinitjob.me/accept_invite/{invite.code}",
    )

    with current_app.app_context():
        mail.send(email)
