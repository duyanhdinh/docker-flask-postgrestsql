from app.db.flask_session import db_session
from app.models.users import User
from app.models.roles import Role
from app.core.security import get_password_hash


def get_by_id(user_id):
    return db_session.query(User).filter(User.id == user_id).first()


def get_by_email(email):
    return db_session.query(User).filter(User.email == email).first()


def created(email, password):
    user = User(email=email, password=get_password_hash(password))
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user


def set_role(role: Role, user: User):
    user.roles.append(role)
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user
