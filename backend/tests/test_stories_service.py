import pytest
from app.features.stories.services.stories_service import (
    create_story, get_all_stories, get_stories_filtered, get_story_by_id, update_story, delete_story
)



def test_create_story(app, test_user):
    with app.app_context():
        story_data = {
            "user_id": test_user["id"],
            "title": "New Story",
            "content": "Content of new story.",
            "origin_country": "France",
            "profession": "Designer",
            "age_range": "18-24"
        }
        story = create_story(story_data)
        assert story is not None
        assert story["title"] == "New Story"
        assert story["origin_country"] == "France"

def test_get_all_stories(app, test_story):
    with app.app_context():
        stories = get_all_stories()
        assert len(stories) >= 1

def test_get_stories_filtered(app, test_story):
    with app.app_context():
        # Match
        stories = get_stories_filtered(origin_country="Spain")
        assert len(stories) >= 1
        assert stories[0]["origin_country"] == "Spain"
        
        # No match
        stories_empty = get_stories_filtered(origin_country="Brazil")
        assert len(stories_empty) == 0

def test_get_story_by_id(app, test_story):
    with app.app_context():
        story = get_story_by_id(test_story["id"])
        assert story is not None
        assert story["id"] == test_story["id"]

def test_update_story(app, test_story):
    with app.app_context():
        updated = update_story(test_story["id"], {
            "title": "Updated Title"
        })
        assert updated is not None
        assert updated["title"] == "Updated Title"
        assert updated["content"] == test_story["content"] # Other fields remain

def test_delete_story(app, test_story):
    with app.app_context():
        success = delete_story(test_story["id"])
        assert success is True
        assert get_story_by_id(test_story["id"]) is None
