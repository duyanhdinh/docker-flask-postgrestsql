# Import standard library packages

# Import installed packages
import requests
from marshmallow import Schema, fields, validates, ValidationError


# Import app code
from app.core.config import RECAPTCHA_SECRET_KEY, RECAPTCHA_SITE_VERIFY


class BaseValidateSchema(Schema):
    token = fields.Str(required=True)

    # @validates("token")
    # def validate_captcha(self, value, **kwargs):
    #     r = requests.post(RECAPTCHA_SITE_VERIFY, data={'secret': RECAPTCHA_SECRET_KEY, 'response': value})
    #     if not r.json()['success']:
    #         raise ValidationError('captcha')


error_messages = {'required': 'required'}

error_email_messages = error_messages | {'invalid': 'email_invalid'}
