import io
import pytest


def _dummy_png():
    return io.BytesIO(b'\x89PNG\r\n\x1a\n' + b'\x00' * 20)


class TestStoryImagesRoutes:

    STORY_DATA = {
        'user_id': None,
        'title': 'Historia con Imagen',
        'content': 'Contenido de la historia.',
        'origin_country': 'Colombia',
        'profession': 'Diseñador',
        'age': 35,
    }

    def _create_story(self, client, test_user):
        data = {**self.STORY_DATA, 'user_id': test_user}
        resp = client.post('/stories', json=data)
        return resp.get_json()['id']

    def test_upload_image_returns_201(self, client, test_user):
        story_id = self._create_story(client, test_user)
        resp = client.post(
            f'/stories/{story_id}/images',
            data={'image': (_dummy_png(), 'foto.png')},
            content_type='multipart/form-data',
        )
        assert resp.status_code == 201
        body = resp.get_json()
        assert 'id' in body
        assert 'url' in body
        assert body['original_name'] == 'foto.png'
        assert body['mime_type'] == 'image/png'

    def test_upload_image_no_file_returns_400(self, client, test_user):
        story_id = self._create_story(client, test_user)
        resp = client.post(
            f'/stories/{story_id}/images',
            data={},
            content_type='multipart/form-data',
        )
        assert resp.status_code == 400
        assert 'error' in resp.get_json()

    def test_upload_image_empty_filename_returns_400(self, client, test_user):
        story_id = self._create_story(client, test_user)
        resp = client.post(
            f'/stories/{story_id}/images',
            data={'image': (_dummy_png(), '')},
            content_type='multipart/form-data',
        )
        assert resp.status_code == 400
        assert 'error' in resp.get_json()

    def test_upload_image_invalid_extension_returns_400(self, client, test_user):
        story_id = self._create_story(client, test_user)
        resp = client.post(
            f'/stories/{story_id}/images',
            data={'image': (_dummy_png(), 'documento.pdf')},
            content_type='multipart/form-data',
        )
        assert resp.status_code == 400
        assert 'error' in resp.get_json()

    def test_upload_image_nonexistent_story_returns_404(self, client, test_user):
        resp = client.post(
            '/stories/9999/images',
            data={'image': (_dummy_png(), 'foto.png')},
            content_type='multipart/form-data',
        )
        assert resp.status_code == 404
        assert 'error' in resp.get_json()

    def test_get_story_images_returns_list(self, client, test_user):
        story_id = self._create_story(client, test_user)
        client.post(
            f'/stories/{story_id}/images',
            data={'image': (_dummy_png(), 'foto.png')},
            content_type='multipart/form-data',
        )
        resp = client.get(f'/stories/{story_id}/images')
        assert resp.status_code == 200
        images = resp.get_json()
        assert isinstance(images, list)
        assert len(images) == 1

    def test_delete_image_returns_200(self, client, test_user):
        story_id = self._create_story(client, test_user)
        upload_resp = client.post(
            f'/stories/{story_id}/images',
            data={'image': (_dummy_png(), 'foto.png')},
            content_type='multipart/form-data',
        )
        image_id = upload_resp.get_json()['id']
        resp = client.delete(f'/stories/{story_id}/images/{image_id}')
        assert resp.status_code == 200
        assert 'message' in resp.get_json()

    def test_delete_nonexistent_image_returns_404(self, client, test_user):
        story_id = self._create_story(client, test_user)
        resp = client.delete(f'/stories/{story_id}/images/9999')
        assert resp.status_code == 404
        assert 'error' in resp.get_json()

    def test_images_appear_in_story_detail(self, client, test_user):
        story_id = self._create_story(client, test_user)
        client.post(
            f'/stories/{story_id}/images',
            data={'image': (_dummy_png(), 'foto.png')},
            content_type='multipart/form-data',
        )
        resp = client.get(f'/stories/{story_id}')
        assert resp.status_code == 200
        body = resp.get_json()
        assert 'images' in body
        assert len(body['images']) == 1
        assert 'url' in body['images'][0]

    def test_images_appear_in_story_list(self, client, test_user):
        story_id = self._create_story(client, test_user)
        client.post(
            f'/stories/{story_id}/images',
            data={'image': (_dummy_png(), 'foto.png')},
            content_type='multipart/form-data',
        )
        resp = client.get('/stories')
        assert resp.status_code == 200
        stories = resp.get_json()
        story = next(s for s in stories if s['id'] == story_id)
        assert 'images' in story
        assert len(story['images']) == 1
