# Import installed packages
from flask import Flask, jsonify

# Import app code
# from app.core import sentry
#
# sentry.init()
# Setup app
from app.core import app as define_app

app = define_app.create_app()


