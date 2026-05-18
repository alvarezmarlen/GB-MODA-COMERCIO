import pytest

VALID_DATA = {
    'user_id': None,
    'title': 'Historia de Prueba',
    'content': 'Contenido de prueba para la historia.',
    'origin_country': 'Colombia',
    'profession': 'Diseñador',
    'age_range': '30-40',
}


class TestStoriesRoutes:

    def test_create_story_returns_201_and_story_json(self, client, test_user):
        data = {**VALID_DATA, 'user_id': test_user}
        response = client.post('/stories', json=data)
        assert response.status_code == 201
        body = response.get_json()
        assert body['title'] == VALID_DATA['title']
        assert body['user_id'] == test_user
        assert 'id' in body

    def test_create_story_missing_fields_returns_500(self, client):
        response = client.post('/stories', json={})
        assert response.status_code == 500

    def test_get_all_stories_returns_200_and_list(self, client):
        response = client.get('/stories')
        assert response.status_code == 200
        assert isinstance(response.get_json(), list)

    def test_get_all_stories_returns_created_stories(self, client, test_user):
        data = {**VALID_DATA, 'user_id': test_user}
        client.post('/stories', json=data)
        data['title'] = 'Otra Historia'
        client.post('/stories', json=data)
        response = client.get('/stories')
        assert len(response.get_json()) == 2

    def test_get_story_by_id_returns_200_and_story(self, client, test_user):
        data = {**VALID_DATA, 'user_id': test_user}
        post_resp = client.post('/stories', json=data)
        story_id = post_resp.get_json()['id']
        response = client.get(f'/stories/{story_id}')
        assert response.status_code == 200
        assert response.get_json()['id'] == story_id

    def test_get_story_by_id_non_existent_returns_404(self, client):
        response = client.get('/stories/999')
        assert response.status_code == 404
        assert 'error' in response.get_json()

    def test_update_story_returns_200_and_updated_story(self, client, test_user):
        data = {**VALID_DATA, 'user_id': test_user}
        post_resp = client.post('/stories', json=data)
        story_id = post_resp.get_json()['id']
        response = client.put(f'/stories/{story_id}', json={'title': 'Título Modificado'})
        assert response.status_code == 200
        assert response.get_json()['title'] == 'Título Modificado'

    def test_update_story_non_existent_returns_404(self, client):
        response = client.put('/stories/999', json={'title': 'Nuevo'})
        assert response.status_code == 404
        assert 'error' in response.get_json()

    def test_delete_story_returns_200_and_message(self, client, test_user):
        data = {**VALID_DATA, 'user_id': test_user}
        post_resp = client.post('/stories', json=data)
        story_id = post_resp.get_json()['id']
        response = client.delete(f'/stories/{story_id}')
        assert response.status_code == 200
        assert 'message' in response.get_json()

    def test_delete_story_actually_removes_it(self, client, test_user):
        data = {**VALID_DATA, 'user_id': test_user}
        post_resp = client.post('/stories', json=data)
        story_id = post_resp.get_json()['id']
        client.delete(f'/stories/{story_id}')
        get_resp = client.get(f'/stories/{story_id}')
        assert get_resp.status_code == 404

    def test_delete_story_non_existent_returns_404(self, client):
        response = client.delete('/stories/999')
        assert response.status_code == 404
        assert 'error' in response.get_json()

    def test_get_stories_filter_by_origin_country(self, client, test_user):
        data = {**VALID_DATA, 'user_id': test_user}
        client.post('/stories', json=data)
        data2 = {**VALID_DATA, 'user_id': test_user, 'origin_country': 'Mexico'}
        client.post('/stories', json=data2)
        response = client.get('/stories?origin_country=Colombia')
        assert response.status_code == 200
        stories = response.get_json()
        assert all(s['origin_country'] == 'Colombia' for s in stories)
        assert len(stories) == 1

    def test_get_stories_filter_by_profession(self, client, test_user):
        data = {**VALID_DATA, 'user_id': test_user}
        client.post('/stories', json=data)
        data2 = {**VALID_DATA, 'user_id': test_user, 'profession': 'Ingeniero'}
        client.post('/stories', json=data2)
        response = client.get('/stories?profession=Diseñador')
        assert response.status_code == 200
        stories = response.get_json()
        assert all(s['profession'] == 'Diseñador' for s in stories)
        assert len(stories) == 1

    def test_get_stories_filter_by_age_range(self, client, test_user):
        data = {**VALID_DATA, 'user_id': test_user}
        client.post('/stories', json=data)
        data2 = {**VALID_DATA, 'user_id': test_user, 'age_range': '50-60'}
        client.post('/stories', json=data2)
        response = client.get('/stories?age_range=30-40')
        assert response.status_code == 200
        stories = response.get_json()
        assert all(s['age_range'] == '30-40' for s in stories)
        assert len(stories) == 1

    def test_get_stories_filter_by_multiple_params(self, client, test_user):
        data = {**VALID_DATA, 'user_id': test_user}
        client.post('/stories', json=data)
        data2 = {**VALID_DATA, 'user_id': test_user, 'origin_country': 'Mexico', 'profession': 'Ingeniero'}
        client.post('/stories', json=data2)
        response = client.get('/stories?origin_country=Colombia&profession=Diseñador')
        assert response.status_code == 200
        stories = response.get_json()
        assert all(s['origin_country'] == 'Colombia' and s['profession'] == 'Diseñador' for s in stories)
        assert len(stories) == 1

    def test_get_stories_filter_no_matches_returns_empty_list(self, client):
        response = client.get('/stories?origin_country=NonExistent')
        assert response.status_code == 200
        assert response.get_json() == []

    def test_get_stories_no_filters_returns_all(self, client, test_user):
        data = {**VALID_DATA, 'user_id': test_user}
        client.post('/stories', json=data)
        client.post('/stories', json={**data, 'title': 'Otra'})
        response = client.get('/stories')
        assert response.status_code == 200
        assert len(response.get_json()) == 2
