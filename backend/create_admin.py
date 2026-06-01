"""
Script para crear un usuario administrador en la base de datos.
Sigue el modelo y servicio de usuarios del proyecto.
"""

from app.app import create_app
from app.features.users.services.users_service import create_user

def setup_admin():
    app = create_app()
    with app.app_context():
        # Datos del usuario administrador a crear
        admin_data = {
            "username": "admin",
            "email": "admin@admin.com",
            "password_hash": "Admin123!", # El password será encriptado por el servicio create_user
            "role": "admin"
        }
        
        try:
            print("Intentando crear el usuario administrador...")
            new_admin = create_user(admin_data)
            print(f"✅ Usuario administrador creado con éxito: {new_admin['email']}")
        except ValueError as e:
            # Si el usuario ya existe (por email), atrapar la excepción del servicio
            print(f"⚠️ {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    setup_admin()
