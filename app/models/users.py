import time
from flask_login import UserMixin
from ..extensions.database import DB


class Users(DB.Model,UserMixin):
    """
    Represents a user in the database.

    Attributes:
        id (int): The unique identifier for the user.
        username (str): The username of the user (unique).
        password_hash (str): The hashed password of the user.
        balance (float): The balance of the user's account.
        role (str): The role of the user (e.g., admin, user).
        created_at (int): The timestamp when the user account was created.
        email (str): The email address of the user (unique).
        mobile (str): The mobile number of the user (unique).
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        company_id (int): The foreign key reference to the company the user belongs to.

    Relationships:
        company (Companies): The company the user belongs to.
    """

    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(64), nullable=False, unique=True)
    password_hash = DB.Column(DB.String(256), nullable=False)
    balance = DB.Column(DB.Float, nullable=False, default=0.0)
    role = DB.Column(DB.String(64), nullable=False, default="user")
    created_at = DB.Column(DB.Integer, nullable=False, default=time.time())
    email = DB.Column(DB.String(64), nullable=False, unique=True)
    mobile = DB.Column(DB.String(64), nullable=False, unique=True)
    first_name = DB.Column(DB.String(64), nullable=False)
    last_name = DB.Column(DB.String(64), nullable=False)
    company_id = DB.Column(DB.Integer, DB.ForeignKey("companies.id"))
    transactions = DB.relationship("Transactions", backref="user", lazy=True)

    def sanitize(self):
        return {
            "id": self.id,
            "username": self.username,
            "balance": self.balance,
            "role": self.role,
            "email": self.email,
            "mobile": self.mobile,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "company_id": self.company_id,
            "created_at": self.created_at,
        }
