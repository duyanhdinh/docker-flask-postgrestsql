# Import standard library packages

# Import installed packages
from marshmallow import fields, validate, validates, ValidationError, validates_schema

# Import app code
from .base import BaseSchema


class UserSchema(BaseSchema):
    # Own properties
    uuid = fields.UUID(dump_only=True)
    email = fields.Email(required=True)
    username = fields.Str(missing=email)
    password = fields.Str(required=True, validate=validate.Length(min=6, max=20), load_only=True)
    is_verified = fields.Bool(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)
    # roles = fields.Nested(RoleSchema, only=("id", "name"), many=True)
