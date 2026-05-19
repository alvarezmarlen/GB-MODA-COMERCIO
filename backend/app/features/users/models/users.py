from app.core.extensions import db 
from .base import BaseMixin

class User(db.Model, BaseMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='customer')  # 'customer' o 'admin'
    
    def to_dict(self):
        # Usamos la base para los campos de la tabla
        data = super().to_dict()
        return data
    