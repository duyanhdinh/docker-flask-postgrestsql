# Import standard library packages

# Import installed packages
import requests
from marshmallow import Schema, fields, validates, ValidationError


# Import app code
from app.core.config import RECAPTCHA_SECRET_KEY, RECAPTCHA_SITE_VERIFY


class BaseSchema(Schema):
    pass
