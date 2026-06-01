def test_login_route_success(client, test_user):
    response = client.post('/auth/login', json={
        "email": "testuser@estudioenpenascal.com",
        "password": "testpass123"
    })
    assert response.status_code == 200
    data = response.get_json()
    assert "access_token" in data
    assert "refresh_token" in data
    assert data["user"]["email"] == "testuser@estudioenpenascal.com"

def test_login_route_invalid_password(client, test_user):
    response = client.post('/auth/login', json={
        "email": "testuser@estudioenpenascal.com",
        "password": "wrongpassword"
    })
    assert response.status_code == 401
    assert "error" in response.get_json()

def test_login_route_missing_fields(client):
    response = client.post('/auth/login', json={
        "email": "testuser@estudioenpenascal.com"
    })
    assert response.status_code == 422
    assert "error" in response.get_json()

def test_logout_route(client, test_user):
    # First login to get a valid token
    login_response = client.post('/auth/login', json={
        "email": "testuser@estudioenpenascal.com",
        "password": "testpass123"
    })
    access_token = login_response.get_json()["access_token"]
    
    # Test logout
    response = client.post('/auth/logout', headers={
        "Authorization": f"Bearer {access_token}"
    })
    assert response.status_code == 200
    assert response.get_json()["message"] == "Logged out successfully"
    
    # Try logging out again with the same token (should fail or at least be caught if token is revoked, though flask_jwt_extended might block it before reaching the view)
    response_again = client.post('/auth/logout', headers={
        "Authorization": f"Bearer {access_token}"
    })
    # Since we set up token blacklisting, this should return 401
    assert response_again.status_code == 401

def test_refresh_route(client, test_user):
    # First login to get a refresh token
    login_response = client.post('/auth/login', json={
        "email": "testuser@estudioenpenascal.com",
        "password": "testpass123"
    })
    refresh_token = login_response.get_json()["refresh_token"]
    
    # Test refresh
    response = client.post('/auth/refresh', headers={
        "Authorization": f"Bearer {refresh_token}"
    })
    assert response.status_code == 200
    assert "access_token" in response.get_json()
