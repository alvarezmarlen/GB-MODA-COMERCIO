import os
from werkzeug.utils import secure_filename
from app.core.extensions import db  
from app.features.story_images.models.story_images import StoryImage

UPLOAD_FOLDER = "uploads/story_images"
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "webp"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def save_image(story_id, file):
    if not allowed_file(file.filename):
        raise ValueError("Formatohola no permitido. Usa JPG, PNG o WebP.")

    

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    image = StoryImage(story_id=story_id, image_url=filepath)
    db.session.add(image)
    db.session.commit()
    return image

def get_images_by_story(story_id):
    return StoryImage.query.filter_by(story_id=story_id).all()

def delete_image(image_id):
    image = StoryImage.query.get_or_404(image_id)
    if os.path.exists(image.image_url):
        os.remove(image.image_url)
    db.session.delete(image)
    db.session.commit()
    return True

# Forzando actualizacion de carpetas