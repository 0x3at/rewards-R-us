from flask import jsonify
from flask_restful import Resource
from ...services.users import get_all_users

class GetAllUsers(Resource):
    def get(self):
        users = get_all_users()
        user_dicts = []
        for user in users:
            user = user.__dict__
            user_dicts.append(user)
        return jsonify(user_dicts)