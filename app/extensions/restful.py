from flask_restful import Api


def register_extension(app):
    api = Api(app)

    from ..resources.users import GetAllUsers

    api.add_resource(GetAllUsers, "/users")

    return api
