from .... import db
from .base import BaseMixin, TimestampMixin


class StoryImage(db.Model, BaseMixin, TimestampMixin):
    __tablename__ = 'story_images'

    id = db.Column(db.Integer, primary_key=True)
    story_id = db.Column(db.Integer, db.ForeignKey('stories.id', ondelete='CASCADE'), nullable=False)
    filename = db.Column(db.String(255), nullable=False)
    original_name = db.Column(db.String(255), nullable=False)
    mime_type = db.Column(db.String(50), nullable=False)
    size = db.Column(db.Integer, nullable=False)

    story = db.relationship('Story', back_populates='images')

    def to_dict(self):
        data = super().to_dict()
        data['url'] = f'/uploads/stories/{self.filename}'
        return data
