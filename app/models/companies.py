import time
from ..extensions.database import DB

class Companies(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(80), nullable=False, unique=True)
    created_at = DB.Column(DB.Integer, nullable=False, default=time.time())
    users = DB.relationship('User', backref='company', lazy=True)
