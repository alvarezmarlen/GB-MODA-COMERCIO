from flask import Flask
from flask_cors import CORS
from . import db

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('backend.app.core.config')
    db.init_app(app)

    @app.route("/api/health")
    def health():
        return {"status":"ok", "message":"Backend funcionando"}

    return app

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5000, debug=True)