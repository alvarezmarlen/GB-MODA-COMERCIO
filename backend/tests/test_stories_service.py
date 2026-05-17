import pytest
from app.features.stories.services.stories_service import (
    create_story, get_all_stories, get_story_by_id,
    update_story, delete_story
)

VALID_DATA = {
    'user_id': None,
    'title': 'Mi Historia de Prueba',
    'content': 'Este es el contenido de la historia para pruebas.',
    'origin_country': 'México',
    'profession': 'Ingeniero de Software',
    'age_range': '25-35',
}


class TestStoriesService:

    def test_create_story_returns_dict_with_all_fields(self, app, test_user):
        data = {**VALID_DATA, 'user_id': test_user}
        result = create_story(data)
        assert result['title'] == VALID_DATA['title']
        assert result['content'] == VALID_DATA['content']
        assert result['origin_country'] == VALID_DATA['origin_country']
        assert result['profession'] == VALID_DATA['profession']
        assert result['age_range'] == VALID_DATA['age_range']
        assert result['user_id'] == test_user
        assert 'id' in result
        assert 'created_at' in result
        assert 'updated_at' in result

    def test_get_all_stories_returns_empty_list(self, app):
        assert get_all_stories() == []

    def test_get_all_stories_returns_all_created_stories(self, app, test_user):
        data = {**VALID_DATA, 'user_id': test_user}
        create_story(data)
        data['title'] = 'Segunda Historia'
        create_story(data)
        stories = get_all_stories()
        assert len(stories) == 2

    def test_get_story_by_id_returns_none_for_non_existent(self, app):
        assert get_story_by_id(999) is None

    def test_get_story_by_id_returns_matching_story(self, app, test_user):
        data = {**VALID_DATA, 'user_id': test_user}
        created = create_story(data)
        result = get_story_by_id(created['id'])
        assert result['id'] == created['id']
        assert result['title'] == VALID_DATA['title']

    def test_update_story_returns_none_for_non_existent(self, app):
        assert update_story(999, {'title': 'Nuevo'}) is None

    def test_update_story_updates_only_provided_fields(self, app, test_user):
        data = {**VALID_DATA, 'user_id': test_user}
        created = create_story(data)
        updated = update_story(created['id'], {'title': 'Título Actualizado'})
        assert updated['title'] == 'Título Actualizado'
        assert updated['content'] == VALID_DATA['content']
        assert updated['origin_country'] == VALID_DATA['origin_country']

    def test_delete_story_returns_false_for_non_existent(self, app):
        assert delete_story(999) is False

    def test_delete_story_removes_story_from_database(self, app, test_user):
        data = {**VALID_DATA, 'user_id': test_user}
        created = create_story(data)
        assert delete_story(created['id']) is True
        assert get_story_by_id(created['id']) is None
