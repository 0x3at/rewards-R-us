from flask_restful import Api


def register_extension(app):
    api = Api(app)

    from ..resources.users import GetAllUsers
    from ..resources.auth import RegisterUser, LoginUser

    api.add_resource(GetAllUsers, "/users")
    api.add_resource(RegisterUser, "/auth/register")
    api.add_resource(LoginUser, "/auth/login")

    app.logger.info("Endpoints registered...")
    
    return api
