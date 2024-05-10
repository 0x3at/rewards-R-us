from flask import jsonify
from flask_restful import Resource
from ...services.users import get_all_users

class GetAllUsers(Resource):
    def get(self):
        users = get_all_users()
        clean_users = []
        for user in users:
            clean_user = user.sanitize()
            clean_users.append(clean_user)
        return jsonify(clean_users)
