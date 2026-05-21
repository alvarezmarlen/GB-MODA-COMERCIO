from .... import db
from .base import BaseMixin, TimestampMixin


class Story(db.Model, BaseMixin, TimestampMixin):
    """Story model representing a user's fashion-related story."""

    __tablename__ = 'stories'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    origin_country = db.Column(db.String(100), nullable=False)
    profession = db.Column(db.String(100), nullable=False)
    age_range = db.Column(db.String(50), nullable=False)

    user = db.relationship('User', backref='stories')
    images = db.relationship('StoryImage', back_populates='story', cascade='all, delete-orphan')

    def to_dict(self):
        data = super().to_dict()
        data['images'] = [img.to_dict() for img in self.images]
        return data
