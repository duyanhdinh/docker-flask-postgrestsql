from app.core import config

from app.repository import users as user_rps
from app.repository import roles as role_rps

def init_db():
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables uncommenting the next line
    # Base.metadata.create_all(bind=engine)

    role = role_rps.get_by_name(config.SUPERUSER_ROLE)
    if not role:
        role = role_rps.created(config.SUPERUSER_ROLE)

    user = user_rps.get_by_email(config.FIRST_SUPERUSER_EMAIL)
    if not user:
        user = user_rps.created(
            config.FIRST_SUPERUSER_EMAIL,
            config.FIRST_SUPERUSER_PASSWORD
        )
        user_rps.set_role(role, user)
