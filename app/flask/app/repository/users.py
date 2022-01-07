from app.core.db import get_db
from app.models.users import User
from app.models.roles import Role
from app.core.security import get_password_hash


def query_active_account(with_trash=False, only_trash=False):
    db_session = get_db()
    if with_trash:
        return db_session.query(User)
    elif only_trash:
        return db_session.query(User).filter(User.deleted_at is not None)

    return db_session.query(User).filter_by(deleted_at=None)


def query_by_email(email, with_trash=False, only_trash=False):
    return query_active_account(with_trash, only_trash).filter(User.email == email)


def get_by_id(user_id, with_trash=False, only_trash=False):
    return query_active_account(with_trash, only_trash).filter(User.id == user_id).first()


def get_by_email(email, with_trash=False, only_trash=False):
    return query_by_email(email, with_trash, only_trash).first()


def created(email, password, username=None):
    db_session = get_db()
    user = User(
        email=email,
        username=email if username == None else username,
        password=get_password_hash(password)
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user


def set_role(role: Role, user: User):
    db_session = get_db()
    user.roles.append(role)
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user


def destroyed_by_email(email):
    db_session = get_db()
    user = get_by_email(email, with_trash=True)
    if user is not None:
        user.roles[:] = []
        query_by_email(email, with_trash=True).delete()
        db_session.commit()
