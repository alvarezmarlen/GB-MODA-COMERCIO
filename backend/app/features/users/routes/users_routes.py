from flask import Blueprint, request, jsonify
from ..services.users_service import create_user as svc_create_user, update_user as svc_update_user, delete_user as svc_delete_user, get_all_users as svc_get_all_users, get_user_by_id as svc_get_user_by_id
from ..schemas.users_schema import UserCreateSchema, UserUpdateSchema
from marshmallow import ValidationError

users_bp = Blueprint('users', __name__)

# Instanciamos los schemas
user_create_schema = UserCreateSchema()
user_update_schema = UserUpdateSchema()

@users_bp.route('/users', methods=['POST'])
def create_user_route():
    data = request.get_json()
    try:
        data = user_create_schema.load(data)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400

    try:
        new_user = svc_create_user(data)
        return jsonify(new_user), 201
    except ValueError as e:
        return jsonify({'errors': str(e)}), 400

@users_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user_route(user_id):
    data = request.get_json()
    try:
        data = user_update_schema.load(data)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400

    updated_user = svc_update_user(user_id, data)
    if not updated_user:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    else:
        return jsonify(updated_user), 200

@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user_route(user_id):
    success = svc_delete_user(user_id)
    if not success:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    return jsonify({'message': 'Usuario eliminado exitosamente'}), 200

@users_bp.route('/users', methods=['GET'])
def get_all_users_route():
    users = svc_get_all_users()
    return jsonify(users), 200

@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id_route(user_id):
    user = svc_get_user_by_id(user_id)
    if not user:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    return jsonify(user), 200


