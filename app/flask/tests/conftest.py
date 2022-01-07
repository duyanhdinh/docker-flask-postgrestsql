# Import installed packages
import pytest

# Import app code
from app.core.app import create_app
from app.core.db import get_db
from app.db.init_db import init_db
from app.repository.users import destroyed_by_email, get_by_email


@pytest.fixture(scope="session")
def app():
    app = create_app()
    app.testing = True

    app.app_context().push()
    return app

@pytest.fixture
def client(app):
    with app.test_client() as client:
        with app.app_context():
            init_db()
        yield client


@pytest.fixture
def create_user_by_email(app):
    list_email=[]
    yield list_email
    for email in list_email:
        destroyed_by_email(email)
