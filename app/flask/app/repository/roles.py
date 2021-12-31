from app.db.flask_session import db_session
from app.models.roles import Role

def get_by_name(name):
    role = db_session.query(Role).filter(Role.name == name).first()
    return role

def get_by_id(role_id):
    role = db_session.query(Role).filter(Role.id == role_id).first()
    return role

def created(name):
    role = Role(name=name)
    db_session.add(role)
    db_session.commit()
    return role

def get_all():
    return db_session.query(Role).all()