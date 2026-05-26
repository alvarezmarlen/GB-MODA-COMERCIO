from werkzeug.security import generate_password_hash, check_password_hash
from ..models.users import User
from .... import db


def create_user(data):
    existing_user = User.query.filter_by(email=data['email']).first()
    if existing_user:
        raise ValueError("El email ya está registrado")

    new_user = User(
        username=data['username'],  
        email=data['email'],
        password_hash=generate_password_hash(data['password_hash']), 
        role=data.get('role', 'customer')  
    )
    db.session.add(new_user)
    db.session.commit()
    
    # En lugar de usar to_dict(), devolvemos un diccionario manual para probar
    return {
        "id": new_user.id,
        "nombre_usuario": new_user.username,
        "email": new_user.email,
        "role": new_user.role
    }
def update_user(user_id, data):
    user = User.query.get(user_id)
    if not user:
        return None
    
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    if 'password_hash' in data:
        user.password_hash = generate_password_hash(data['password_hash'])  # Asegúrate de hashear la contraseña antes de guardarla
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
