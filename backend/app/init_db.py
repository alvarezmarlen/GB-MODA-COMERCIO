# pyrefly: ignore [missing-import]
# Script to initialize the database schema (run once to create all tables)
from app.app import create_app
from app import db

app = create_app()
with app.app_context():
    db.create_all()
    print("Base de datos creada exitosamente.")
