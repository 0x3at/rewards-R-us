from flask_cors import CORS

def register_extension(app):
    CORS(app)
    return app