from flask import jsonify
from flask_restful import Resource, reqparse
from ...services.admin import get_all_users

parser = reqparse.RequestParser()

class GetAllUsers(Resource):
    def get(self):
        response = get_all_users()
        return response
