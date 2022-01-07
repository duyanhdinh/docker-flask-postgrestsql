from flask import Blueprint

from app.api import v1 as endpoints_v1

v1 = Blueprint('v1', __name__, url_prefix='/v1')

endpoints_v1.set_route(v1)
