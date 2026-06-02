import os
from flask import Flask 
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from app import db
from flask import send_from_directory
from app.features.users.routes.users_routes import users_bp
from app.features.stories.routes.stories_routes import stories_bp
from app.features.auth.routes.auth_routes import auth_bp
from app.features.auth.models.token_blacklist import TokenBlacklist
from app.core.jwt_handlers import setup_jwt_handlers



def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('app.core.config.Config')

    db.init_app(app)

    jwt = JWTManager(app)
    setup_jwt_handlers(jwt)

    app.register_blueprint(users_bp)
    app.register_blueprint(stories_bp)
    app.register_blueprint(auth_bp)


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
