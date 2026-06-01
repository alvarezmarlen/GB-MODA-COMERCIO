from datetime import datetime, timezone
from .... import db


class TokenBlacklist(db.Model):
    __tablename__ = 'token_blacklist'

    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), unique=True, nullable=False, index=True)
    token_type = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
