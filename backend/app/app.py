import os
from flask import Flask
from flask_cors import CORS
from app.core.extensions import db


# Importaciones de los Blueprints (Rutas)
from app.features.users.routes.users_routes import users_bp
from app.features.stories.routes.stories_routes import stories_bp
from app.features.story_images.routes import story_images_bp


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('app.core.config.Config')
    

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'moda_comercio.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # 2. CREAR LAS TABLAS AUTOMÁTICAMENTE SI NO EXISTEN
    with app.app_context():
        from app.features.users.models.users import User
        from app.features.stories.models.stories import Story
        
        db.create_all()
        print("Tablas creadas o ya existían.")
        
    app.register_blueprint(users_bp)
    app.register_blueprint(stories_bp)
    app.register_blueprint(story_images_bp)

    @app.route('/')
    def home():
        return 'Bienvenidos'

    @app.route('/api/health')
    def health():
        return {'status': 'ok', 'message': 'Backend funcionando'}

    @app.route('/uploads/stories/<filename>')
    def uploaded_story_image(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

    return app
