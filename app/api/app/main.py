# Import installed packages
from flask import Flask
import os
from app.core import config

# Import app code
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Setup app
from .core import app_setup  # noqa

"""
    @api {post} /user Adds a new User
    @apiVersion 1.0.0
    @apiName add_user
    @apiGroup User
    @apiParam {String}      username        The user's username.
    @apiParam {String}      first_name      The first name of the User.
    @apiParam {String}      last_name       the last name of the User.
    @apiParam {Object}      profile         The profile data
    @apiParam {Number}      profile.age     The user's age.
    @apiParam {String}      profile.image   The user's avatar-image.
    @apiSuccess {Number}    id              The new user id.
"""
@app.route("/")
def hello():
    return "Hello World!!!"

"""
    @api {get} /haha/:dada/:haha Gets all the users
    @apiVersion 1.0.0
    @apiName get_users
    @apiGroup User
    @apiExample Example usage:
    curl -i http://localhost/users
    @apiSuccess {Object}    users                 The user data
    @apiSuccess {Number}    users.id              The user's id.
    @apiSuccess {String}    users.username        The user's username.
    @apiSuccess {String}    users.first_name      The first name of the User.
    @apiSuccess {String}    users.last_name       The last name of the User.
    @apiSuccess {Object}    users.profile         The profile data
    @apiSuccess {Number}    users.profile.age     The user's age.
    @apiSuccess {String}    users.profile.image   The user's avatar-image.
"""
@app.route("/test")
def hi():
    return str(config.SQLALCHEMY_DATABASE_URI)

"""
    @api {post} /city Create a new city
    @apiVersion 1.0.0
    @apiName CreateCity
    @apiGroup City
    @apiDescription Create a new city.
    @apiHeader {String} access-key Users unique access-key.
    @apiBody {String} name=Paris Name of the city
    @apiQuery {String=Aerial,Land,Underwater} view=Aerial Type of view.
    @apiQuery {Number} zoom Zoom.
    @apiError UserNotFound The <code>id</code> of the User was not found.
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 404 Not Found
        {
        "error": "UserNotFound"
        }
"""
@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 1
    return str(division_by_zero)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
