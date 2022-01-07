from .endpoints.authentication import auth

def set_route(app):
    app.register_blueprint(auth)