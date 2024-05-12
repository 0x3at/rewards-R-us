import time
from ..extensions.database import DB


class Products(DB.Model):
    """
    Represents a product in the database.

    Attributes:
        id (int): The unique identifier for the product.
        name (str): The name of the product.
        price (float): The price of the product.
        stock (int): The stock of the product.
        created_at (int): The timestamp when the product was created.
    """

    id = DB.Column(DB.Integer, primary_key=True)
    title = DB.Column(DB.String(80), nullable=False)
    category = DB.Column(DB.String(80), nullable=False)
    description = DB.Column(DB.String(80), nullable=False)
    price = DB.Column(DB.Float, nullable=False)
    status = DB.Column(DB.String(80), nullable=False)
    stock = DB.Column(DB.Integer, nullable=False)
    created_at = DB.Column(DB.Integer, nullable=False, default=time.time())
    image_url = DB.Column(DB.String(80), nullable=False)
    stars = DB.Column(DB.Integer, nullable=False)

    def sanitize(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "status": self.status,
            "stock": self.stock,
            "created_at": self.created_at,
        }
