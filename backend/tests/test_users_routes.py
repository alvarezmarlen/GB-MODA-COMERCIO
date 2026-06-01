def test_create_user_route(client):
    response = client.post('/users', json={
        "nombre_usuario": "routeuser",
        "email": "routeuser@estudioenpenascal.com",
        "password": "password123",
        "role": "user"
    })
    assert response.status_code == 201
    assert response.get_json()["nombre_usuario"] == "routeuser"

def test_get_all_users_route(client, test_user):
    response = client.get('/users')
    assert response.status_code == 200
    assert len(response.get_json()) >= 1

def test_get_user_by_id_route(client, test_user):
    response = client.get(f'/users/{test_user["id"]}')
    assert response.status_code == 200
    assert response.get_json()["email"] == test_user["email"]

def test_get_user_not_found(client):
    response = client.get('/users/9999')
    assert response.status_code == 404

def test_update_user_route(client, test_user):
    response = client.put(f'/users/{test_user["id"]}', json={
        "nombre_usuario": "updatedviaapi"
    })
    assert response.status_code == 200
    assert response.get_json()["username"] == "updatedviaapi"

def test_delete_user_route(client, test_user):
    response = client.delete(f'/users/{test_user["id"]}')
    assert response.status_code == 200
    
    # Verify it was deleted
    response2 = client.get(f'/users/{test_user["id"]}')
    assert response2.status_code == 404
