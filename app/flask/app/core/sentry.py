# Import standard library packages

# Import installed packages
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

# Import app code


# Init Sentry
from app.core import config


def init():
    sentry_sdk.init(
        dsn=config.SENTRY_DSN,
        integrations=[FlaskIntegration()],

        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=config.SENTRY_RATE
    )

