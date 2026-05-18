import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
from flask_cors import CORS
from backend.app import db
from backend.app.features.users.routes.users_routes import users_bp

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('backend.app.core.config.Config')
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.register_blueprint(users_bp)

    @app.route("/api/health")
    def health():
        return {"status":"ok", "message":"Backend funcionando"}

    return app

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5010, debug=True)