import pytest
from unittest.mock import patch
from create_admin import setup_admin

def test_setup_admin_success(app, capsys):
    # setup_admin calls create_app(), which might recreate the app context.
    # To avoid this, we can mock create_app to return our test app.
    with patch('create_admin.create_app', return_value=app):
        setup_admin()
        
        captured = capsys.readouterr()
        assert "Usuario administrador creado con éxito" in captured.out

def test_setup_admin_already_exists(app, capsys):
    with patch('create_admin.create_app', return_value=app):
        # Run once to create
        setup_admin()
        
        # Run again to trigger duplicate
        setup_admin()
        
        captured = capsys.readouterr()
        assert "El email ya está registrado" in captured.out
