import time
from ..extensions.database import DB


class Transactions(DB.Model):
    """
    Represents a transaction in the database.

    Attributes:
        id (int): The unique identifier for the transaction.
        user_id (int): The foreign key reference to the user that made the transaction.
        product_id (int): The foreign key reference to the product that was transacted.
        quantity (int): The quantity of the product that was transacted.
        total (float): The total cost of the transaction.
        created_at (int): The timestamp when the transaction was created.
    """

    id = DB.Column(DB.Integer, primary_key=True)
    user_id = DB.Column(DB.Integer, DB.ForeignKey("users.id"))
    product_id = DB.Column(DB.Integer, DB.ForeignKey("products.id"))
    quantity = DB.Column(DB.Integer, nullable=False)
    total = DB.Column(DB.Float, nullable=False)
    credits_spent = DB.Column(DB.Float, nullable=False)
    currency_spent = DB.Column(DB.Float, nullable=False)
    created_at = DB.Column(DB.Integer, nullable=False, default=time.time())

    def sanitize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "total": self.total,
            "credits_spent": self.credits_spent,
            "currency_spent": self.currency_spent,
            "created_at": self.created_at,
        }
