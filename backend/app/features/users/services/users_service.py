from ..models import User
from ..services import db

def create_user(data):
    """Crea un nuevo usuario en la base de datos."""
    new_user = User(
        username=data['nombre_usuario'],
        email=data['email'],
        password_hash=data['password'],  # Asegúrate de hashear la contraseña antes de guardarla
        role=data.get('role', 'customer')  # Por defecto, el rol es 'customer'
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user.to_dict()

def update_user(user_id, data):
    """Actualiza un usuario existente."""
    user = User.query.get(user_id)
    if not user:
        return None
    
    user.username = data.get('nombre_usuario', user.username)
    user.email = data.get('email', user.email)
    if 'password' in data:
        user.password_hash = data['password']  # Asegúrate de hashear la contraseña antes de guardarla
    user.role = data.get('role', user.role)
    
    db.session.commit()
    return user.to_dict()

def delete_user(user_id):
    """Elimina un usuario de la base de datos."""
    user = User.query.get(user_id)
    if not user:
        return False
    
    db.session.delete(user)
    db.session.commit()
    return True

def get_all_users():
    """Obtiene todos los usuarios de la base de datos."""
    users = User.query.all()
    return [user.to_dict() for user in users]

def get_user_by_id(user_id):
    """Obtiene un usuario por su ID."""
    user = User.query.get(user_id)
    return user.to_dict() if user else None
