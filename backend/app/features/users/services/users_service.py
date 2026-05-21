from werkzeug.security import generate_password_hash, check_password_hash
from ..models.users import User
from .... import db


def create_user(data):
    new_user = User(
        username=data['nombre_usuario'],
        email=data['email'],
        password_hash=generate_password_hash(data['password']),
        role=data.get('role', 'customer')
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user.to_dict()


def update_user(user_id, data):
    user = User.query.get(user_id)
    if not user:
        return None
    user.username = data.get('nombre_usuario', user.username)
    user.email = data.get('email', user.email)
    if 'password' in data:
        user.password_hash = generate_password_hash(data['password'])
    user.role = data.get('role', user.role)
    db.session.commit()
    return user.to_dict()


def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return False
    db.session.delete(user)
    db.session.commit()
    return True


def get_all_users():
    users = User.query.all()
    return [user.to_dict() for user in users]


def get_user_by_id(user_id):
    user = User.query.get(user_id)
    return user.to_dict() if user else None


def verify_password(user, password):
    return check_password_hash(user.password_hash, password)
