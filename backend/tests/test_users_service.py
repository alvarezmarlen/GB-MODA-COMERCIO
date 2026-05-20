import pytest
from app.features.users.services.users_service import (
    create_user, get_all_users, get_user_by_id,
    update_user, delete_user
)


VALID_DATA = {
    'nombre_usuario': 'testuser',
    'email': 'test@example.com',
    'password': 'hashedpass',
}


class TestUsersService:

    def test_create_user_returns_dict_with_all_fields(self, app):
        result = create_user(VALID_DATA)
        assert result['username'] == 'testuser'
        assert result['email'] == 'test@example.com'
        assert 'id' in result
        assert 'role' in result

    def test_create_user_default_role_is_customer(self, app):
        result = create_user(VALID_DATA)
        assert result['role'] == 'customer'

    def test_create_user_with_custom_role(self, app):
        data = {**VALID_DATA, 'role': 'admin'}
        result = create_user(data)
        assert result['role'] == 'admin'

    def test_get_all_users_returns_empty_list(self, app):
        assert get_all_users() == []

    def test_get_all_users_returns_all_created_users(self, app):
        create_user(VALID_DATA)
        create_user({**VALID_DATA, 'nombre_usuario': 'user2', 'email': 'user2@example.com'})
        users = get_all_users()
        assert len(users) == 2

    def test_get_user_by_id_returns_none_for_non_existent(self, app):
        assert get_user_by_id(999) is None

    def test_get_user_by_id_returns_matching_user(self, app):
        created = create_user(VALID_DATA)
        result = get_user_by_id(created['id'])
        assert result['id'] == created['id']
        assert result['username'] == 'testuser'

    def test_update_user_returns_none_for_non_existent(self, app):
        assert update_user(999, {'nombre_usuario': 'new'}) is None

    def test_update_user_updates_only_provided_fields(self, app):
        created = create_user(VALID_DATA)
        updated = update_user(created['id'], {'nombre_usuario': 'updated'})
        assert updated['username'] == 'updated'
        assert updated['email'] == 'test@example.com'

    def test_update_user_updates_all_provided_fields(self, app):
        created = create_user(VALID_DATA)
        updated = update_user(created['id'], {
            'nombre_usuario': 'newname',
            'email': 'new@example.com',
            'role': 'admin',
        })
        assert updated['username'] == 'newname'
        assert updated['email'] == 'new@example.com'
        assert updated['role'] == 'admin'

    def test_delete_user_returns_false_for_non_existent(self, app):
        assert delete_user(999) is False

    def test_delete_user_removes_user_from_database(self, app):
        created = create_user(VALID_DATA)
        assert delete_user(created['id']) is True
        assert get_user_by_id(created['id']) is None
