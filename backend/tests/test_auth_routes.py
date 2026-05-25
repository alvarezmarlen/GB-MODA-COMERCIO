import pytest
from app.features.users.services.users_service import create_user
from app.features.auth.services.auth_service import login_user


USER_DATA = {
    'nombre_usuario': 'routeuser',
    'email': 'route@example.com',
    'password': 'mypassword123',
}


class TestAuthRoutes:

    def test_login_returns_200_and_tokens(self, client, app):
        with app.app_context():
            create_user(USER_DATA)
        response = client.post('/auth/login', json={
            'email': USER_DATA['email'],
            'password': USER_DATA['password'],
        })
        assert response.status_code == 200
        body = response.get_json()
        assert 'access_token' in body
        assert 'refresh_token' in body
        assert 'user' in body

    def test_login_invalid_credentials_returns_401(self, client, app):
        with app.app_context():
            create_user(USER_DATA)
        response = client.post('/auth/login', json={
            'email': USER_DATA['email'],
            'password': 'wrongpassword',
        })
        assert response.status_code == 401
        assert 'error' in response.get_json()

    def test_login_missing_fields_returns_422(self, client):
        response = client.post('/auth/login', json={})
        assert response.status_code == 422

    def test_login_no_body_returns_422(self, client):
        response = client.post('/auth/login')
        assert response.status_code == 422

    def test_logout_returns_200(self, client, app):
        with app.app_context():
            create_user(USER_DATA)
            login_result = login_user(USER_DATA['email'], USER_DATA['password'])
            access_token = login_result['access_token']
        response = client.post(
            '/auth/logout',
            headers={'Authorization': f'Bearer {access_token}'}
        )
        assert response.status_code == 200
        assert 'message' in response.get_json()

    def test_logout_without_token_returns_401(self, client):
        response = client.post('/auth/logout')
        assert response.status_code == 401

    def test_refresh_returns_200(self, client, app):
        with app.app_context():
            create_user(USER_DATA)
            login_result = login_user(USER_DATA['email'], USER_DATA['password'])
            refresh_token = login_result['refresh_token']
        response = client.post(
            '/auth/refresh',
            headers={'Authorization': f'Bearer {refresh_token}'}
        )
        assert response.status_code == 200
        body = response.get_json()
        assert 'access_token' in body

    def test_refresh_with_access_token_returns_401(self, client, app):
        with app.app_context():
            create_user(USER_DATA)
            login_result = login_user(USER_DATA['email'], USER_DATA['password'])
            access_token = login_result['access_token']
        response = client.post(
            '/auth/refresh',
            headers={'Authorization': f'Bearer {access_token}'}
        )
        assert response.status_code == 401

    def test_access_protected_route_with_revoked_token(self, client, app):
        with app.app_context():
            create_user(USER_DATA)
            login_result = login_user(USER_DATA['email'], USER_DATA['password'])
            access_token = login_result['access_token']
            from app.features.auth.services.auth_service import logout_user
            from flask_jwt_extended import decode_token
            decoded = decode_token(access_token)
            logout_user(decoded['jti'], 'access')
        response = client.post(
            '/auth/logout',
            headers={'Authorization': f'Bearer {access_token}'}
        )
        assert response.status_code == 401

    def test_full_auth_flow(self, client, app):
        with app.app_context():
            create_user(USER_DATA)
            login_result = login_user(USER_DATA['email'], USER_DATA['password'])
            access_token = login_result['access_token']
            refresh_token = login_result['refresh_token']

        resp1 = client.post(
            '/auth/logout',
            headers={'Authorization': f'Bearer {access_token}'}
        )
        assert resp1.status_code == 200

        resp2 = client.post(
            '/auth/refresh',
            headers={'Authorization': f'Bearer {refresh_token}'}
        )
        assert resp2.status_code == 200
        new_access_token = resp2.get_json()['access_token']

        resp3 = client.post(
            '/auth/logout',
            headers={'Authorization': f'Bearer {new_access_token}'}
        )
        assert resp3.status_code == 200
        from app.features.auth.services.auth_service import is_token_revoked
        from flask_jwt_extended import decode_token
        with app.app_context():
            decoded = decode_token(new_access_token)
            assert is_token_revoked(decoded['jti'])

        resp4 = client.post(
            '/auth/logout',
            headers={'Authorization': f'Bearer {new_access_token}'}
        )
        assert resp4.status_code == 401
