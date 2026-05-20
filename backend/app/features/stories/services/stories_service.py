"""Service layer for story-related business logic and database operations."""

from ..models.stories import Story
from app.core.extensions import db 


def create_story(data):
    """Create a new story in the database.

    Args:
        data: Dictionary containing user_id, title, content, origin_country,
              profession, and age_range.

    Returns:
        dict: The newly created story serialized via to_dict().
    """
    new_story = Story(
        user_id=data['user_id'],
        title=data['title'],
        content=data['content'],
        origin_country=data['origin_country'],
        profession=data['profession'],
        age_range=data['age_range']
    )
    db.session.add(new_story)
    db.session.commit()
    return new_story.to_dict()


def get_all_stories():
    """Retrieve all stories from the database including their images.

    Returns:
        list[dict]: A list of all stories serialized as dictionaries.
    """
    stories = Story.query.all()
    result = []
    for story in stories:
        data = story.to_dict()
        data['images'] = [
            {"id": img.id, "image_url": img.image_url}
            for img in story.images
        ]
        result.append(data)
    return result


def get_stories_filtered(origin_country=None, profession=None, age_range=None):
    """Retrieve stories filtered by optional demographic criteria.

    All filters are optional and combined with AND logic when multiple are provided.

    Args:
        origin_country: Filter by exact origin country match.
        profession: Filter by exact profession match.
        age_range: Filter by exact age range match.

    Returns:
        list[dict]: A list of matching stories serialized as dictionaries.
    """
    query = Story.query
    if origin_country:
        query = query.filter(Story.origin_country == origin_country)
    if profession:
        query = query.filter(Story.profession == profession)
    if age_range:
        query = query.filter(Story.age_range == age_range)
    stories = query.all()
    return [story.to_dict() for story in stories]


def get_story_by_id(story_id):
    """Retrieve a single story by its ID.

    Args:
        story_id: The ID of the story to retrieve.

    Returns:
        dict | None: The story serialized as a dictionary, or None if not found.
    """
    story = Story.query.get(story_id)
    return story.to_dict() if story else None


def update_story(story_id, data):
    """Update an existing story with the provided fields.

    Only the fields present in data are updated; missing fields keep their current values.

    Args:
        story_id: The ID of the story to update.
        data: Dictionary containing the fields to update.

    Returns:
        dict | None: The updated story serialized as a dictionary, or None if not found.
    """
    story = Story.query.get(story_id)
    if not story:
        return None

    story.user_id = data.get('user_id', story.user_id)
    story.title = data.get('title', story.title)
    story.content = data.get('content', story.content)
    story.origin_country = data.get('origin_country', story.origin_country)
    story.profession = data.get('profession', story.profession)
    story.age_range = data.get('age_range', story.age_range)

    db.session.commit()
    return story.to_dict()


def delete_story(story_id):
    """Delete a story by its ID.

    Args:
        story_id: The ID of the story to delete.

    Returns:
        bool: True if the story was deleted, False if it was not found.
    """
    story = Story.query.get(story_id)
    if not story:
        return False

    db.session.delete(story)
    db.session.commit()
    return True
