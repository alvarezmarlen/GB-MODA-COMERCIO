from app.core.extensions import db 
from .base import BaseMixin, TimestampMixin


class Story(db.Model, BaseMixin, TimestampMixin):
    """Story model representing a user's fashion-related story.

    Each story is linked to a user and includes demographic information
    such as origin country, profession, and age range.
    """

    __tablename__ = 'stories'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    origin_country = db.Column(db.String(100), nullable=False)
    profession = db.Column(db.String(100), nullable=False)
    age_range = db.Column(db.String(50), nullable=False)

    user = db.relationship('User', backref='stories')
