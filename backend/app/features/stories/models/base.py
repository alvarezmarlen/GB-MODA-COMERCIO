from datetime import datetime
from decimal import Decimal
from .... import db

class BaseMixin:
    def to_dict(self):
        result = {c.name: getattr(self, c.name) for c in self.__table__.columns}

        for key, value in result.items():
            if isinstance(value, datetime):
                result[key] = value.isoformat()
            elif isinstance(value, Decimal):
                result[key] = float(value)

        return result

class TimestampMixin:
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
