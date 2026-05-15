from app.core.extensions import db  # la conexión a la BD que configuró otro compañero

class StoryImage(db.Model):
    __tablename__ = "story_images"

    id        = db.Column(db.Integer, primary_key=True)
    story_id  = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(500), nullable=False)

 #   story = db.relationship("Story", back_populates="images")

    def __repr__(self):
        return f"<StoryImage id={self.id} story_id={self.story_id}>"