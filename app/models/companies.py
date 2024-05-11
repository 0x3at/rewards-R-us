import time
from ..extensions.database import DB


class Companies(DB.Model):
    """
    Represents a company in the database.

    Attributes:
        id (int): The unique identifier for the company.
        name (str): The name of the company (unique).
        created_at (int): The timestamp when the company was created.

    Relationships:
        users (List[User]): The list of users belonging to the company.
    """

    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(80), nullable=False, unique=True)
    created_at = DB.Column(DB.Integer, nullable=False, default=time.time())
    users = DB.relationship("Users", backref="company", lazy=True)

    def sanitize(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at
        }
    