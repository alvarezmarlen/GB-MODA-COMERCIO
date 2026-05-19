from flask import Flask, send_from_directory
from flask_cors import CORS
from app import db
from app.features.users.routes.users_routes import users_bp
from app.features.stories.routes.stories_routes import stories_bp


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('app.core.config.Config')
    db.init_app(app)

    app.register_blueprint(users_bp)
    app.register_blueprint(stories_bp)

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
