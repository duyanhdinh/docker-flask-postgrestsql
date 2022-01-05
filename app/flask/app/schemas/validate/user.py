# Import standard library packages

# Import installed packages
from marshmallow import fields, validate, validates, ValidationError, validates_schema

# Import app code
from .base import BaseValidateSchema
from ...core.security import verify_password
from ...repository.users import get_by_email


class RegisterUserSchema(BaseValidateSchema):
    # Own properties
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6, max=20))
    confirm_password = fields.Str(required=True, validate=validate.Length(min=6, max=20))


    @validates("email")
    def validate_email(self, value, **kwargs):
        if get_by_email(value):
            raise ValidationError('email_exist')

    @validates_schema
    def validate_confirm_password(self, data, **kwargs):
        if data['password'] != data['confirm_password']:
            raise ValidationError("not_confirmed")


class LoginUserSchema(BaseValidateSchema):
    # Own properties
    email = fields.Email(required=True)
    password = fields.Str(required=True)

    @validates_schema
    def validate_user(self, data, **kwargs):
        user = get_by_email(data['email'])
        if user:
            if not verify_password(data['password'], user.password):
                raise ValidationError('wrong_password')
        else:
            raise ValidationError('wrong_email')