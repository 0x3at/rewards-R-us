from flask_restful import Api


def register_extension(app):
    api = Api(app)

    from ..resources.companies import AddCompany
    from ..resources.auth import RegisterUser, LoginUser, Logout

    api.add_resource(AddCompany, "/companies/post/add")
    
    api.add_resource(RegisterUser, "/auth/register")
    api.add_resource(LoginUser, "/auth/login")
    api.add_resource(Logout, "/auth/logout")

    app.logger.info("Endpoints registered...")

    return api
