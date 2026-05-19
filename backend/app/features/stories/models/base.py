from datetime import datetime
from decimal import Decimal
from app.core.extensions import db 


class BaseMixin:
    """Mixin that provides a to_dict() serialization method for SQLAlchemy models."""

    def to_dict(self):
        """Serialize the model instance into a dictionary.

        Converts datetime objects to ISO format strings and Decimal objects to floats.
        """
        result = {c.name: getattr(self, c.name) for c in self.__table__.columns}

        for key, value in result.items():
            if isinstance(value, datetime):
                result[key] = value.isoformat()
            elif isinstance(value, Decimal):
                result[key] = float(value)

        return result


class TimestampMixin:
    """Mixin that adds created_at and updated_at timestamp columns to a model."""

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
