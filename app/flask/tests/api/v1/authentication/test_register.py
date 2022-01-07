# Import installed packages
import requests

# Import app code
from app.helpers.common import url_api_auth


def test_register_success(create_user_by_email):
    email = "ae@a.com"
    create_user_by_email.append(email)
    payload = {
        "email": email,
        "password": "123456",
        "confirm_password": "123456",
        "token": "token"
    }
    r = requests.post(url_api_auth('register'), json=payload)

    assert r.json() == "success"
    assert r.status_code == 200
