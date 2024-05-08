import time
from ..extensions.database import DB

class BusinessUnit(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    user_id = DB.relationship('User', backref='business_unit', lazy=True)
    created_at = DB.Column(DB.Integer, nullable=False, default=time.time())
