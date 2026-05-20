import pytest


class TestUsersRoutes:

    def test_create_user_returns_201(self, client):
        data = {
            'nombre_usuario': 'testuser',
            'email': 'test@example.com',
            'password': 'secret123',
        }
        response = client.post('/users', json=data)
        assert response.status_code == 201
        body = response.get_json()
        assert body['username'] == 'testuser'
        assert body['email'] == 'test@example.com'
        assert body['role'] == 'customer'
        assert 'id' in body

    def test_create_user_with_role_returns_201(self, client):
        data = {
            'nombre_usuario': 'adminuser',
            'email': 'admin@example.com',
            'password': 'secret123',
            'role': 'admin',
        }
        response = client.post('/users', json=data)
        assert response.status_code == 201
        body = response.get_json()
        assert body['role'] == 'admin'

    def test_create_user_missing_fields_raises_error(self, client):
        response = client.post('/users', json={})
        assert response.status_code == 500

    def test_create_user_no_body_raises_error(self, client):
        response = client.post('/users')
        assert response.status_code in (415, 500)

    def test_get_all_users_returns_200_and_list(self, client):
        response = client.get('/users')
        assert response.status_code == 200
        assert isinstance(response.get_json(), list)

    def test_get_all_users_returns_created_users(self, client):
        data = {'nombre_usuario': 'user1', 'email': 'user1@example.com', 'password': 'pass1'}
        client.post('/users', json=data)
        data2 = {'nombre_usuario': 'user2', 'email': 'user2@example.com', 'password': 'pass2'}
        client.post('/users', json=data2)
        response = client.get('/users')
        assert len(response.get_json()) == 2

    def test_get_user_by_id_returns_200(self, client):
        data = {'nombre_usuario': 'findme', 'email': 'findme@example.com', 'password': 'pass'}
        post_resp = client.post('/users', json=data)
        user_id = post_resp.get_json()['id']
        response = client.get(f'/users/{user_id}')
        assert response.status_code == 200
        assert response.get_json()['id'] == user_id
        assert response.get_json()['username'] == 'findme'

    def test_get_user_by_id_non_existent_returns_404(self, client):
        response = client.get('/users/999')
        assert response.status_code == 404
        assert 'error' in response.get_json()

    def test_update_user_returns_200_and_updated_user(self, client):
        data = {'nombre_usuario': 'original', 'email': 'original@example.com', 'password': 'pass'}
        post_resp = client.post('/users', json=data)
        user_id = post_resp.get_json()['id']
        response = client.put(f'/users/{user_id}', json={'nombre_usuario': 'modificado'})
        assert response.status_code == 200
        assert response.get_json()['username'] == 'modificado'

    def test_update_user_non_existent_returns_404(self, client):
        response = client.put('/users/999', json={'nombre_usuario': 'nuevo'})
        assert response.status_code == 404
        assert 'error' in response.get_json()

    def test_update_user_preserves_unmodified_fields(self, client):
        data = {'nombre_usuario': 'keep', 'email': 'keep@example.com', 'password': 'pass'}
        post_resp = client.post('/users', json=data)
        user_id = post_resp.get_json()['id']
        response = client.put(f'/users/{user_id}', json={'nombre_usuario': 'changed'})
        body = response.get_json()
        assert body['username'] == 'changed'
        assert body['email'] == 'keep@example.com'

    def test_delete_user_returns_200(self, client):
        data = {'nombre_usuario': 'deleteme', 'email': 'deleteme@example.com', 'password': 'pass'}
        post_resp = client.post('/users', json=data)
        user_id = post_resp.get_json()['id']
        response = client.delete(f'/users/{user_id}')
        assert response.status_code == 200
        assert 'message' in response.get_json()

    def test_delete_user_actually_removes_it(self, client):
        data = {'nombre_usuario': 'gone', 'email': 'gone@example.com', 'password': 'pass'}
        post_resp = client.post('/users', json=data)
        user_id = post_resp.get_json()['id']
        client.delete(f'/users/{user_id}')
        get_resp = client.get(f'/users/{user_id}')
        assert get_resp.status_code == 404

    def test_delete_user_non_existent_returns_404(self, client):
        response = client.delete('/users/999')
        assert response.status_code == 404
        assert 'error' in response.get_json()
