import uuid
import pytest
from app.features.users.services.users_service import create_user
from app.features.auth.services.auth_service import login_user, logout_user, is_token_revoked, refresh_access_token


USER_DATA = {
    'nombre_usuario': 'authuser',
    'email': 'auth@example.com',
    'password': 'securepassword123',
}


class TestAuthService:

    def test_login_user_returns_tokens_and_user(self, app):
        create_user(USER_DATA)
        result = login_user(USER_DATA['email'], USER_DATA['password'])
        assert result is not None
        assert 'access_token' in result
        assert 'refresh_token' in result
        assert 'user' in result
        assert result['user']['email'] == USER_DATA['email']

    def test_login_user_invalid_email_returns_none(self, app):
        result = login_user('nonexistent@example.com', 'anything')
        assert result is None

    def test_login_user_invalid_password_returns_none(self, app):
        create_user(USER_DATA)
        result = login_user(USER_DATA['email'], 'wrongpassword')
        assert result is None

    def test_logout_and_is_token_revoked(self, app):
        jti = str(uuid.uuid4())
        logout_user(jti, 'access')
        assert is_token_revoked(jti) is True

    def test_logout_twice_returns_false(self, app):
        jti = str(uuid.uuid4())
        logout_user(jti, 'access')
        result = logout_user(jti, 'access')
        assert result is False

    def test_refresh_access_token(self, app):
        token = refresh_access_token('1')
        assert 'access_token' in token
        assert token['access_token'] is not None

    def test_is_token_revoked_returns_false_for_unknown(self, app):
        assert is_token_revoked('nonexistent-jti') is False
