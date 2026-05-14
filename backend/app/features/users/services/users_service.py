from ..models import User
from ...stories.users import db

def create_user(data):
    """Crea un nuevo usuario en la base de datos."""
    new_user = User(
        username=data['username'],
        email=data['email'],
        password_hash=data['password_hash'],  # Asegúrate de hashear la contraseña antes de guardarla
        role=data.get('role', 'customer')  # Por defecto, el rol es 'customer'
    )
    db.session.add(new_user)
    db.session.commit()
    return user.to_dict()