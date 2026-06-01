import pytest
from app.app import create_app
from app import db
from app.features.users.models.users import User
# pyrefly: ignore [missing-import]
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "WTF_CSRF_ENABLED": False,
        "JWT_SECRET_KEY": "super-secret-key-that-is-at-least-32-bytes-long",
    })

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def test_user(app):
    with app.app_context():
        user = User(
            username="testuser",
            email="testuser@estudioenpenascal.com",
            role="customer",
            password_hash=generate_password_hash("testpass123")
        )
        db.session.add(user)
        db.session.commit()
        # Return a dictionary or re-query to avoid detaching issues
        return {
            "id": user.id,
            "email": user.email,
            "username": user.username,
            "role": user.role
        }

@pytest.fixture
def test_admin(app):
    with app.app_context():
        admin = User(
            username="adminuser",
            email="adminuser@estudioenpenascal.com",
            role="admin",
            password_hash=generate_password_hash("adminpass123")
        )
        db.session.add(admin)
        db.session.commit()
        return {
            "id": admin.id,
            "email": admin.email,
            "username": admin.username,
            "role": admin.role
        }

@pytest.fixture
def user_token(app, test_user):
    with app.app_context():
        return create_access_token(identity=str(test_user["id"]))

@pytest.fixture
def admin_token(app, test_admin):
    with app.app_context():
        return create_access_token(identity=str(test_admin["id"]))

from app.features.stories.services.stories_service import create_story

@pytest.fixture
def test_story(app, test_user):
    with app.app_context():
        story_data = {
            "user_id": test_user["id"],
            "title": "Test Story",
            "content": "This is a test story.",
            "origin_country": "Spain",
            "profession": "Developer",
            "age_range": "25-34"
        }
        return create_story(story_data)
