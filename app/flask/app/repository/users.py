from app.db.flask_session import db_session
from app.models.users import User
from app.models.roles import Role
from app.core.security import get_password_hash


def get_active_account(with_trash=False,only_trash=False):
    if with_trash:
        return db_session.query(User)
    elif only_trash:
        return db_session.query(User).filter(User.deleted_at is not None)

    return db_session.query(User).filter_by(deleted_at=None)

def get_by_id(user_id,with_trash=False,only_trash=False):
    return get_active_account(with_trash,only_trash).filter(User.id == user_id).first()


def get_by_email(email,with_trash=False,only_trash=False):
    return get_active_account(with_trash,only_trash).filter(User.email == email).first()


def created(email, password, username=None):
    user = User(
        email=email,
        username=email if username==None else username,
        password=get_password_hash(password)
    )
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
