import os
import secrets
import datetime

# app
SECRET_KEY = os.getenv("SECRET_KEY", default=secrets.token_urlsafe(32))

# sentry
SENTRY_DSN = os.getenv("SENTRY_DSN")
SENTRY_RATE = os.getenv("SENTRY_RATE")

# database
DB_TYPE = os.getenv("DB_TYPE")
DB_SERVER = os.getenv("DB_SERVER")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT")
SQLALCHEMY_DATABASE_URI = (
    f"{DB_TYPE}://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}"
)

# SQLAlchemy
SQLALCHEMY_TRACK_MODIFICATIONS = False

# admin
SUPERUSER_ROLE = os.getenv("SUPERUSER_ROLE")
FIRST_SUPERUSER_EMAIL = os.getenv("FIRST_SUPERUSER_EMAIL")
FIRST_SUPERUSER_PASSWORD = os.getenv("FIRST_SUPERUSER_PASSWORD")

# cors
BACKEND_CORS_ORIGINS = os.getenv("BACKEND_CORS_ORIGINS")

# api
API_V1_URI = "/v1"

# ReCaptcha
RECAPTCHA_SECRET_KEY = os.getenv("RECAPTCHA_SECRET_KEY")
RECAPTCHA_SITE_VERIFY = os.getenv("RECAPTCHA_SITE_VERIFY")

# flask-jwt-extended
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", default=secrets.token_urlsafe(32))
JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=7)