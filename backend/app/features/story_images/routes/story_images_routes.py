from flask import Blueprint, request, jsonify
from app.features.story_images.services.story_images_service import (save_image, get_images_by_story, delete_image)

story_images_bp = Blueprint("story_images", __name__)

@story_images_bp.route("/story_images/<int:story_id>", methods=["POST"])
def upload_image(story_id):
    if "file" not in request.files:
        return jsonify({"error": "No se envió ningún archivo"}), 400
    file = request.files["file"]
    try:
        image = save_image(story_id, file)
        return jsonify({"id": image.id, "image_url": image.image_url}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 422


@story_images_bp.route("/story_images/<int:story_id>", methods=["GET"])
def get_images(story_id):
    images = get_images_by_story(story_id)
    return jsonify([{"id": img.id, "image_url": img.image_url} for img in images])


@story_images_bp.route("/story_images/<int:image_id>", methods=["DELETE"])
def delete_image_route(image_id):
    delete_image(image_id)
    return jsonify({"message": "Imagen eliminada"}), 200