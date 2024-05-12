from flask import jsonify
from flask_restful import Resource
from ...services.users import get_all_users

class GetAllUsers(Resource):
    def get(self):
        users = get_all_users()
        return jsonify(users)
