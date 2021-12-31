# Import all the models, so that Base has them before being
# imported by Alembic or used by Flask
from app.db.base_class import Base  # noqa
from app.models.users import User  # noqa
from app.models.roles import Role  # noqa
from app.models.socials import Social  # noqa
from app.models.user_profiles import UserProfile  # noqa
