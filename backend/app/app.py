from flask import Flask
from flask_cors import CORS
from app import db
from app.core.extensions import db

# Importaciones de los Blueprints (Rutas)
from app.features.users.routes.users_routes import users_bp
from app.features.stories.routes.stories_routes import stories_bp
from app.features.story_images.routes import story_images_bp


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('app.core.config.Config')
    db.init_app(app)


    # 2. CREAR LAS TABLAS AUTOMÁTICAMENTE SI NO EXISTEN
    with app.app_context():
        db.create_all()
        
    app.register_blueprint(users_bp)
    app.register_blueprint(stories_bp)
    app.register_blueprint(story_images_bp)

    @app.route('/')
    def home():
        return 'Bienvenidos'

    @app.route('/api/health')
    def health():
        return {'status': 'ok', 'message': 'Backend funcionando'}

    return app
