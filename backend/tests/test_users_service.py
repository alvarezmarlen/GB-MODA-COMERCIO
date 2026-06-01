import pytest
from app.features.users.services.users_service import create_user, update_user, delete_user, get_all_users, get_user_by_id

def test_create_user_success(app):
    with app.app_context():
        new_user = create_user({
            "username": "newuser",
            "email": "newuser@estudioenpenascal.com",
            "password_hash": "password123",
            "role": "customer"
        })
        assert new_user is not None
        assert new_user["nombre_usuario"] == "newuser"
        assert new_user["email"] == "newuser@estudioenpenascal.com"

def test_create_user_duplicate_email(app, test_user):
    with app.app_context():
        with pytest.raises(ValueError, match="El email ya está registrado"):
            create_user({
                "username": "anotheruser",
                "email": "testuser@estudioenpenascal.com", # Same as test_user fixture
                "password_hash": "password123"
            })

def test_create_user_invalid_domain(app):
    with app.app_context():
        with pytest.raises(ValueError, match="Solo se permiten correos con dominio @estudioenpenascal.com"):
            create_user({
                "username": "baduser",
                "email": "baduser@gmail.com",
                "password_hash": "password123"
            })

def test_get_all_users(app, test_user, test_admin):
    with app.app_context():
        users = get_all_users()
        assert len(users) >= 2 # At least test_user and test_admin

def test_get_user_by_id(app, test_user):
    with app.app_context():
        user = get_user_by_id(test_user["id"])
        assert user is not None
        assert user["email"] == test_user["email"]

def test_update_user(app, test_user):
    with app.app_context():
        updated = update_user(test_user["id"], {
            "username": "updatedusername"
        })
        assert updated is not None
        assert updated["username"] == "updatedusername"

def test_delete_user(app, test_user):
    with app.app_context():
        success = delete_user(test_user["id"])
        assert success is True
        
        # Verify deletion
        assert get_user_by_id(test_user["id"]) is None
