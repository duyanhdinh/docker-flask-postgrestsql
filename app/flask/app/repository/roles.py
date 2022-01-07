from app.core.db import get_db
from app.models.roles import Role

def get_by_name(name):
    db_session = get_db()
    role = db_session.query(Role).filter(Role.name == name).first()
    return role


def get_admin():
    return get_by_name('admin')


def get_user():
    return get_by_name('user')


def get_premium():
    return get_by_name('premium')


def get_by_id(role_id):
    db_session = get_db()
    role = db_session.query(Role).filter(Role.id == role_id).first()
    return role


def created(name):
    db_session = get_db()
    role = Role(name=name)
    db_session.add(role)
    db_session.commit()
    return role


def get_all():
    db_session = get_db()
    return db_session.query(Role).all()
