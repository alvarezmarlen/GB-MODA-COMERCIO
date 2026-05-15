from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from app.core.extensions import db
from app.features.story_images.routes import story_images_bp
import os

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(os.path.abspath("instance"), "moda_comercio.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "clave-secreta-temporal"

    db.init_app(app)
    JWTManager(app)

    app.register_blueprint(story_images_bp)

    @app.route("/api/health")
    def health():
        return jsonify({"status": "ok", "message": "Backend funcionando"})

    with app.app_context():
        db.create_all()

    return app