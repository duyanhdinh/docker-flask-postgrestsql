# Import standard library packages

# Import installed packages
from marshmallow import fields, validate, validates, ValidationError, validates_schema

# Import app code
from .base import BaseSchema, BaseValidateSchema
from ..repository.users import get_by_email


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



class UserSchema(BaseSchema):
    # Own properties
    uuid = fields.UUID(dump_only=True)
    email = fields.Email(required=True)
    username = fields.Str(missing=email)
    password = fields.Str(required=True, validate=validate.Length(min=6, max=20))
    is_active = fields.Bool(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)
    # roles = fields.Nested(RoleSchema, only=("id", "name"), many=True)
