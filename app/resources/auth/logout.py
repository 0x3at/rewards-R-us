from flask import make_response
from flask_restful import Resource
from flask_login import login_required, logout_user


class Logout(Resource):
    
    @login_required
    def post(self):
        logout_user()
        response = make_response({"message": "User logged out"})
        response.headers["Content-Type"] = "application/json"
        response.status_code = 200
        return response