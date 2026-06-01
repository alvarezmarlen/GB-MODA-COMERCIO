import pytest
from unittest.mock import patch
from app.features.users.models.users import User
from create_admin import setup_admin

def test_setup_admin_creates_user(app, capsys):
    """
    Prueba que el script de create_admin inserta correctamente al usuario en la BD.
    """
    # Parcheamos 'create_app' dentro de 'create_admin' para que en lugar de usar 
    # la configuración real, use nuestro 'app' fixture (que usa base de datos en memoria).
    with patch('create_admin.create_app', return_value=app):
        setup_admin()
        
    # Verificamos en el contexto de nuestra aplicación de pruebas que el usuario existe
    with app.app_context():
        admin_user = User.query.filter_by(email="admin@admin.com").first()
        
        assert admin_user is not None, "El usuario admin no fue creado"
        assert admin_user.username == "admin"
        assert admin_user.role == "admin"
        assert admin_user.password_hash != "Admin123!" # Comprobar que está hasheado
        
        # Verificamos que imprimió el mensaje de éxito por terminal
        captured = capsys.readouterr()
        assert "Usuario administrador creado con éxito" in captured.out

def test_setup_admin_handles_existing_user(app, capsys):
    """
    Prueba que si el usuario ya existe, el script lo maneja correctamente sin romper la aplicación.
    """
    with patch('create_admin.create_app', return_value=app):
        # Primera ejecución: crea el admin
        setup_admin()
        
        # Limpiamos la captura de la consola
        capsys.readouterr()
        
        # Segunda ejecución: intenta crear el admin de nuevo, el cual ya existe
        setup_admin()
        
    captured = capsys.readouterr()
    # Debería imprimir el ValueError lanzado por nuestro servicio create_user
    assert "⚠️ El email ya está registrado" in captured.out
