from ..models.stories import Story
from .... import db

def create_story(data):
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
    stories = Story.query.all()
    return [story.to_dict() for story in stories]

def get_story_by_id(story_id):
    story = Story.query.get(story_id)
    return story.to_dict() if story else None

def update_story(story_id, data):
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
    story = Story.query.get(story_id)
    if not story:
        return False

    db.session.delete(story)
    db.session.commit()
    return True
