from flask_restful import Resource, reqparse
from ...services.auth import register_user


parser = reqparse.RequestParser()
parser.add_argument("username", type=str, required=True, help="Username is required")
parser.add_argument("password", type=str, required=True, help="Password is required")
parser.add_argument("role", type=str, required=True, help="Role is required")
parser.add_argument("email", type=str, required=True, help="Email is required")
parser.add_argument("mobile", type=str, required=True, help="Mobile is required")
parser.add_argument(
    "first_name", type=str, required=True, help="First name is required"
)
parser.add_argument("last_name", type=str, required=True, help="Last name is required")
parser.add_argument(
    "company_id", type=int, required=True, help="Company ID is required"
)


class RegisterUser(Resource):
    def post(self):
        args = parser.parse_args()
        response = register_user(
            args["username"],
            args["password"],
            args["role"],
            args["email"],
            args["mobile"],
            args["first_name"],
            args["last_name"],
            args["company_id"],
        )

        return response
