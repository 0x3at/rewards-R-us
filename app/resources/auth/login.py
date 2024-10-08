from flask_restful import Resource, reqparse
from ...services.auth import login_user

parser = reqparse.RequestParser()
parser.add_argument("username", type=str, required=True, help="Username is required")
parser.add_argument("password", type=str, required=True, help="Password is required")
parser.add_argument("remember", type=bool, required=False, default=False)


class LoginUser(Resource):
    def post(self):
        args = parser.parse_args()
        response = login_user(args["username"], args["password"], remember=args["remember"])
        
        return response
