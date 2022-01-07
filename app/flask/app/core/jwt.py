# Import standard library modules

# Import installed modules
from flask_jwt_extended import JWTManager


# Import app code

# Setup the Flask-JWT-Extended extension
def init(current_app):
    jwt = JWTManager(current_app)
