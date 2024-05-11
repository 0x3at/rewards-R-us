import time
import secrets
from ..extensions.database import DB

class Invites(DB.Model):
    """
    Represents an invite in the database.

    Attributes:
        id (int): The unique identifier for the invite.
        company_id (int): The unique identifier for the company associated to the invite.
        expiration (int): The timestamp when the invite expires.
        created_at (int): The timestamp when the invite was created.
        code (str): The code for the invite.
        role (str): The role the user will have when using the invite.
        email (str): The email of the user who received the invite.
    """
    
    id = DB.Column(DB.Integer, primary_key=True)
    company_id = DB.Column(DB.Integer, DB.ForeignKey("companies.id"), nullable=False)
    expiration = DB.Column(DB.Integer, nullable=False)
    created_at = DB.Column(DB.Integer, nullable=False, default=time.time())
    code = DB.Column(DB.String(80), nullable=False, default=secrets.token_urlsafe(), unique=True)
    role = DB.Column(DB.String(80), nullable=False)
    email = DB.Column(DB.String(80), nullable=False)

    def sanitize(self):
        return {
            "id": self.id,
            "company_id": self.company_id,
            "expiration": self.expiration,
            "created_at": self.created_at,
            "code": self.code,
            "role": self.role,
            "email": self.email,
        }
