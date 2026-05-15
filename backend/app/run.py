from flask import Flask
from flask_cors import CORS
from . import db
from .features.users.routes.users_routes import users_bp
from .features.stories.routes.stories_routes import stories_bp

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('app.core.config.Config')
    db.init_app(app)

    app.register_blueprint(users_bp)
    app.register_blueprint(stories_bp)

    @app.route("/api/health")
    def health():
        return {"status":"ok", "message":"Backend funcionando"}

    return app

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5000, debug=True)