# Import installed packages
import requests
from webargs.flaskparser import use_args, use_kwargs
from flask import jsonify

# Import app code
from app.core.config import RECAPTCHA_SECRET_KEY
from app.main import app
from app.helpers.common import uri_api_auth
from app.repository import users as user_rps
from app.repository import roles as roles_rps
from app.schemas.user import RegisterUserSchema

"""
    @api {post} /auth/register Register an user
    @apiVersion 1.0.0
    @apiName auth_register
    @apiGroup Authentication
    
    @apiBody {String}      token                reCAPTCHA token
    @apiBody {String}      email                The account's email.
    @apiBody {String}      password             The account's password.
    @apiBody {String}      confirm_password     The account's confirm password.
    
    @apiSuccess {String}   message=success      Response message
    
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 422 Unprocessable Entity
        {
          "errors": {
            "json": {
              "email": [
                "Missing data for required field."
              ], 
              "password": [
                "Missing data for required field."
              ]
            }
          }, 
          "msg": "The request was well-formed but was unable to be followed due to semantic errors."
        }
"""
@app.route(uri_api_auth('register'), methods=["POST"])
@use_args(RegisterUserSchema())
def register(args):
    user_rps.set_role(
        roles_rps.get_user(),
        user_rps.created(email=args['email'], password=args['password'])
    )
    return jsonify('success'), 200
