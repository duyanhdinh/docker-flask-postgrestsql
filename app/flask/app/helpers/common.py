from app.core import config


def host_url():
    return f"{config.HOST_URL}"


def true_uri(endpoints):
    return f"{endpoints}/"


def uri_api_ver(version=None):
    return f"{version if version else config.LATEST_VERSION_API}/"

def url_api_auth(endpoints,version=None):
    return f"{host_url()}{uri_api_ver(version)}auth/{endpoints}/"
