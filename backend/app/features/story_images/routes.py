from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.features.story_images import services

story_images_bp = Blueprint("story_images", __name__, url_prefix="/api/stories")

@story_images_bp.route("/<int:story_id>/images", methods=["POST"])
@jwt_required()
def upload_image(story_id):
    if "file" not in request.files:
        return jsonify({"error": "No se envió ningún archivo"}), 400

    file = request.files["file"]
    try:
        image = services.save_image(story_id, file)
        return jsonify({"id": image.id, "image_url": image.image_url}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 422

@story_images_bp.route("/<int:story_id>/images", methods=["GET"])
def get_images(story_id):
    images = services.get_images_by_story(story_id)
    return jsonify([{"id": img.id, "image_url": img.image_url} for img in images])

@story_images_bp.route("/images/<int:image_id>", methods=["DELETE"])
@jwt_required()
def delete_image(image_id):
    services.delete_image(image_id)
    return jsonify({"message": "Imagen eliminada"}), 200