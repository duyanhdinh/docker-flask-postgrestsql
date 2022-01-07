# Import standard library modules

# Import installed packages
from flask_cors import CORS


# Import app code

def init(current_app):
    origins = []

    # Set all CORS enabled origins
    if current_app.config['BACKEND_CORS_ORIGINS']:
        origins_raw = current_app.config['BACKEND_CORS_ORIGINS'].split(",")
        for origin in origins_raw:
            use_origin = origin.strip()
            origins.append(use_origin)

        CORS(current_app, origins=origins, supports_credentials=True)
