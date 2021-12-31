from app.repository import users as user_rps

def is_active(user):
    return user.is_active

def is_superuser(user):
    return user.is_superuser

def is_username_active(username):
    user = user_rps.get_by_username(username)
    return is_active(user)

def get_user_roles(user):
    return user.roles