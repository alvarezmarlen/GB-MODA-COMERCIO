import pytest
import tempfile
import shutil
from pathlib import Path
from app import db as _db
from app.app import create_app
from app.features.users.models.users import User


@pytest.fixture
def app():
    app = create_app()
    tmp_upload = tempfile.mkdtemp()
    app.config.update({
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
        'TESTING': True,
        'PROPAGATE_EXCEPTIONS': False,
        'UPLOAD_FOLDER': tmp_upload,
    })
    with app.app_context():
        _db.create_all()
        yield app
        _db.drop_all()
    shutil.rmtree(tmp_upload, ignore_errors=True)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def test_user(app):
    user = User(
        username='testuser',
        email='test@example.com',
        password_hash='hashed123',
        role='customer'
    )
    _db.session.add(user)
    _db.session.commit()
    return user.id
