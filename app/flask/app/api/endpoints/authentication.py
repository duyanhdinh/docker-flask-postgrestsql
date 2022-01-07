# Import installed packages
from webargs.flaskparser import use_args, use_kwargs
from flask import jsonify, Blueprint
from flask_jwt_extended import jwt_required, create_access_token

# Import app code
from app.helpers.common import true_uri
from app.repository import users as user_rps
from app.repository import roles as roles_rps
from app.repository.users import get_by_email
from app.schemas.model.user import UserSchema
from app.schemas.validate.user import RegisterUserSchema, LoginUserSchema

auth = Blueprint('auth', __name__, url_prefix='/auth')

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
    
    @apiError   {String}   msg          Description of error
    @apiError   {Json}     [errors]       List error
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
@auth.route(true_uri('register'), methods=["POST"])
@use_args(RegisterUserSchema())
def register(args):
    """Register new account functions."""
    user_rps.set_role(
        roles_rps.get_user(),
        user_rps.created(email=args['email'], password=args['password'])
    )
    return jsonify('success'), 200


"""
    @api {post} /auth/login Sign In an user
    @apiVersion 1.0.0
    @apiName auth_login
    @apiGroup Authentication
    
    @apiHeader {String} Authorization Bearer token
    @apiHeaderExample {json} Header-Example:
        {
            "Authorization": "Bearer <access_token>"
        }

    @apiBody {String}      token                reCAPTCHA token
    @apiBody {String}      email                The account's email.
    @apiBody {String}      password             The account's password.

    @apiSuccess {String}   message=success      Response message

    @apiError   {String}   msg          Description of error
    @apiError   {Json}     [errors]       List error
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
@auth.route(true_uri('login'), methods=["POST"])
@use_args(LoginUserSchema())
def login(args):
    """Login user functions."""
    user = UserSchema(exclude=('uuid','updated_at','deleted_at')).dump(get_by_email(args['email']))
    access_token = {'access_token' : create_access_token(identity=args['email'])}
    return user | access_token, 200
