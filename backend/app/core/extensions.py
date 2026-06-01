# Shared SQLAlchemy instance, initialized once and used across all models
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()