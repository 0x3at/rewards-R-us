from flask_restful import Resource, reqparse

from ...services.companies import add_company

parser = reqparse.RequestParser()
parser.add_argument("name", type=str, required=True, help="Name is required")
parser.add_argument("admin_email", type=str, required=True, help="Address is required")

class AddCompany(Resource):
    def post(self):
        args = parser.parse_args()
        response = add_company(
            args["name"],
            args["admin_email"]
        )

        return response