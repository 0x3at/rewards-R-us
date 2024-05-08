import time
from ..extensions.database import DB

class User(DB.Model):
	id = DB.Column(DB.Integer, primary_key=True)
	username = DB.Column(DB.String(64), nullable=False)
	password_hash = DB.Column(DB.String(256), nullable=False)
	balance = DB.Column(DB.Float, nullable=False, default=0.0)
	role = DB.Column(DB.String(64), nullable=False)
	created_at = DB.Column(DB.Integer, nullable=False, default=time.time())
	email = DB.Column(DB.String(64), nullable=False)
	mobile = DB.Column(DB.String(64), nullable=False)
	first_name = DB.Column(DB.String(64), nullable=False)
	last_name = DB.Column(DB.String(64), nullable=False)
	business_unit = DB.Column(DB.Integer, DB.ForeignKey('business_unit.id'))