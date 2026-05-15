from flask import Blueprint, request, jsonify
from ..services.stories_service import create_story, update_story, delete_story, get_all_stories, get_story_by_id

stories_bp = Blueprint('stories', __name__)

@stories_bp.route('/stories', methods=['POST'])
def create_story_route():
    data = request.get_json()
    new_story = create_story(data)
    return jsonify(new_story), 201

@stories_bp.route('/stories/<int:story_id>', methods=['PUT'])
def update_story_route(story_id):
    data = request.get_json()
    updated_story = update_story(story_id, data)
    if not updated_story:
        return jsonify({'error': 'Historia no encontrada'}), 404
    else:
        return jsonify(updated_story), 200

@stories_bp.route('/stories/<int:story_id>', methods=['DELETE'])
def delete_story_route(story_id):
    success = delete_story(story_id)
    if not success:
        return jsonify({'error': 'Historia no encontrada'}), 404
    else:
        return jsonify({'message': 'Historia eliminada exitosamente'}), 200

@stories_bp.route('/stories', methods=['GET'])
def get_all_stories_route():
    stories = get_all_stories()
    return jsonify(stories), 200

@stories_bp.route('/stories/<int:story_id>', methods=['GET'])
def get_story_by_id_route(story_id):
    story = get_story_by_id(story_id)
    if not story:
        return jsonify({'error': 'Historia no encontrada'}), 404
    else:
        return jsonify(story), 200
