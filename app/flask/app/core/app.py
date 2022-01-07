# Import standard library packages

# Import installed packages
from flask import Flask, jsonify


# Import app code  # noqa


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.core.config')

    from . import db
    db.init_app(app)

    with app.app_context():
        db.get_db(app)

    from . import cors, jwt, errors
    cors.init(app)
    jwt.init(app)
    errors.handle(app)

    @app.route("/")
    def hello():
        """home"""
        return "Hello World"

    @app.route('/route-list', methods=['GET'])
    def list_route():
        """Print available functions."""
        func_list = {}
        for rule in app.url_map.iter_rules():
            if rule.endpoint != 'static':
                func_list[rule.rule] = app.view_functions[rule.endpoint].__doc__
        return jsonify(func_list)

    # api
    from .api import v1
    app.register_blueprint(v1)

    if __name__ == "__main__":
        app.run(debug=True, host="0.0.0.0", port=80)

    return app
