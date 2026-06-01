from app.features.auth.services.auth_service import login_user, logout_user, is_token_revoked, refresh_access_token
# pyrefly: ignore [missing-import]
from flask_jwt_extended import decode_token

def test_login_user_success(app, test_user):
    with app.app_context():
        # Using the fixture, password was set to "testpass123"
        result = login_user("testuser@estudioenpenascal.com", "testpass123")
        assert result is not None
        assert "access_token" in result
        assert "refresh_token" in result
        assert result["user"]["email"] == "testuser@estudioenpenascal.com"

def test_login_user_invalid_password(app, test_user):
    with app.app_context():
        result = login_user("testuser@estudioenpenascal.com", "wrongpassword")
        assert result is None

def test_login_user_not_found(app):
    with app.app_context():
        result = login_user("nonexistent@estudioenpenascal.com", "anypassword")
        assert result is None

def test_logout_user(app, test_user):
    with app.app_context():
        # First login to get a token
        login_result = login_user("testuser@estudioenpenascal.com", "testpass123")
        access_token = login_result["access_token"]
        
        decoded_token = decode_token(access_token)
        jti = decoded_token["jti"]
        
        # Test logout
        result = logout_user(jti, "access")
        assert result is True
        
        # Verify it's revoked
        assert is_token_revoked(jti) is True
        
        # Test logout again (should return False as it's already blacklisted)
        result_again = logout_user(jti, "access")
        assert result_again is False

def test_refresh_access_token(app, test_user):
    with app.app_context():
        new_token_data = refresh_access_token(str(test_user["id"]))
        assert "access_token" in new_token_data
        
        # Decode and check identity
        decoded = decode_token(new_token_data["access_token"])
        assert decoded["sub"] == str(test_user["id"])
