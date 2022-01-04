# Import standard library packages

# Import installed packages
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

# Import app code
from app.main import app
from app.db.flask_session import db_session
from app.db.init_db import init_db
from app.core import config

# Set up CORS
from . import cors  # noqa

from .jwt import jwt  # noqa
from . import errors  # noqa

from app.api import api  # noqa

# Create secret key
app.config["SECRET_KEY"] = config.SECRET_KEY

# Init Sentry
sentry_sdk.init(
    dsn=config.SENTRY_DSN,
    integrations=[FlaskIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=config.SENTRY_RATE
)


@app.teardown_appcontext
def shutdown_db_session(exception=None):
    db_session.remove()


@app.before_first_request
def setup():
    init_db()
