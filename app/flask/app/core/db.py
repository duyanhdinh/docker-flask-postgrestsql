from flask_sqlalchemy import SQLAlchemy
from flask import g, Flask

from app.db.base import Base

db = SQLAlchemy(model_class=Base)


def get_db(app=None):
    """Connect to the application's configured database. The connection
    is unique for each request and will be reused if this is called
    again.
    """
    if 'db' not in g:
        if app is None:
            new_app = Flask(__name__)
            new_app.config.from_object('app.core.config')
            db.init_app(new_app)
        else:
            db.init_app(app)

        g.db = db

    return g.db.session


def close_db(e=None):
    """If this request connected to the database, close the
    connection.
    """
    g_db = g.pop("db", None)

    if g_db is not None:
        g_db.session.remove()


def first_request():
    from app.db.init_db import init_db
    init_db()


def init_app(app):
    """Register database functions with the Flask app. This is called by
    the application factory.
    """
    app.teardown_appcontext(close_db)
    app.before_first_request(first_request)
