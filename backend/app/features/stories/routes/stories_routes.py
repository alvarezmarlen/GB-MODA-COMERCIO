"""Route definitions for the stories API blueprint."""

from flask import Blueprint, request, jsonify
from ..services.stories_service import create_story, update_story, delete_story, get_all_stories, get_story_by_id, get_stories_filtered

stories_bp = Blueprint('stories', __name__)


@stories_bp.route('/stories', methods=['POST'])
def create_story_route():
    """Create a new story.

    Request body (JSON):
        user_id (int): ID of the author.
        title (str): Story title.
        content (str): Story content.
        origin_country (str): Country of origin.
        profession (str): Profession of the author.
        age_range (str): Age range of the author.

    Returns:
        201: The created story as JSON.
    """
    data = request.get_json()
    new_story = create_story(data)
    return jsonify(new_story), 201


@stories_bp.route('/stories/<int:story_id>', methods=['PUT'])
def update_story_route(story_id):
    """Update an existing story by ID.

    Returns:
        200: The updated story as JSON.
        404: If the story does not exist.
    """
    data = request.get_json()
    updated_story = update_story(story_id, data)
    if not updated_story:
        return jsonify({'error': 'Story not found'}), 404
    else:
        return jsonify(updated_story), 200


@stories_bp.route('/stories/<int:story_id>', methods=['DELETE'])
def delete_story_route(story_id):
    """Delete a story by ID.

    Returns:
        200: Confirmation message.
        404: If the story does not exist.
    """
    success = delete_story(story_id)
    if not success:
        return jsonify({'error': 'Story not found'}), 404
    else:
        return jsonify({'message': 'Story deleted successfully'}), 200


@stories_bp.route('/stories', methods=['GET'])
def get_all_stories_route():
    """Retrieve all stories, optionally filtered by query parameters.

    Query params (all optional):
        origin_country (str): Filter by exact origin country.
        profession (str): Filter by exact profession.
        age_range (str): Filter by exact age range.

    Filters are combined with AND logic when multiple are provided.
    If no filters are given, all stories are returned.

    Returns:
        200: A list of stories as JSON.
    """
    origin_country = request.args.get('origin_country')
    profession = request.args.get('profession')
    age_range = request.args.get('age_range')

    if origin_country or profession or age_range:
        stories = get_stories_filtered(
            origin_country=origin_country,
            profession=profession,
            age_range=age_range
        )
    else:
        stories = get_all_stories()
    return jsonify(stories), 200


@stories_bp.route('/stories/<int:story_id>', methods=['GET'])
def get_story_by_id_route(story_id):
    """Retrieve a single story by its ID.

    Returns:
        200: The story as JSON.
        404: If the story does not exist.
    """
    story = get_story_by_id(story_id)
    if not story:
        return jsonify({'error': 'Story not found'}), 404
    else:
        return jsonify(story), 200
