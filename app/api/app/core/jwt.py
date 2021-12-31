# Import standard library modules

# Import installed modules
from flask_jwt_extended import JWTManager

# Import app code
from ..main import app
from app.repository import users as user_rps

# Setup the Flask-JWT-Extended extension
jwt = JWTManager(app)


# @jwt.user_loader_callback_loader
# def get_current_user(identity):
#     return user_rps.get_by_id(identity)
