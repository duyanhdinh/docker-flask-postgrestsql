from app.core import config

def uri_api(endpoints):
    return f"{config.API_V1_URI}/{endpoints}/"

def uri_api_auth(endpoints):
    return f"{uri_api('auth')}{endpoints}/"