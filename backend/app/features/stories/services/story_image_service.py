from ..models.story_image import StoryImage
from ..models.stories import Story
from ....core.file_upload import save_file, delete_file
from .... import db


def upload_story_image(story_id, file_storage):
    story = db.session.get(Story, story_id)
    if not story:
        return None

    unique_name, original_name, ext, size = save_file(file_storage)

    mime_type_map = {
        'png': 'image/png',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'gif': 'image/gif',
        'webp': 'image/webp',
    }

    image = StoryImage(
        story_id=story_id,
        filename=unique_name,
        original_name=original_name,
        mime_type=mime_type_map.get(ext, 'application/octet-stream'),
        size=size,
    )
    db.session.add(image)
    db.session.commit()
    return image.to_dict()


def delete_story_image(story_id, image_id):
    image = StoryImage.query.filter_by(id=image_id, story_id=story_id).first()
    if not image:
        return False

    delete_file(image.filename)
    db.session.delete(image)
    db.session.commit()
    return True


def get_story_images(story_id):
    images = StoryImage.query.filter_by(story_id=story_id).all()
    return [img.to_dict() for img in images]
