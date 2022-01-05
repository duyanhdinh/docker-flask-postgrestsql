# Import installed packages
from flask import Flask, jsonify

# Import app code
app = Flask(__name__)
app.config.from_object('app.core.config')

# Setup app
from .core import app_setup  # noqa


@app.route("/")
def hello():
    return "Hello World!!!"


@app.route("/test")
def test():
    return "Hello World!!!" if None else "haha"


@app.route('/route-list', methods=['GET'])
def list_route():
    """Print available functions."""
    func_list = {}
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            func_list[rule.rule] = app.view_functions[rule.endpoint].__doc__
    return jsonify(func_list)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
