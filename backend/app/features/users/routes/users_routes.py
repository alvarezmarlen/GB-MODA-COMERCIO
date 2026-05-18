from flask import Blueprint, request, jsonify
from ..services.users_service import (
    create_user as service_create_user,
    update_user as service_update_user,
    delete_user as service_delete_user,
    get_all_users as service_get_all_users,
    get_user_by_id as service_get_user_by_id,
)

# Creamos un Blueprint para las rutas de usuarios
users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['POST'])
def create_user_route():
    data = request.get_json()
    new_user = service_create_user(data)
    return jsonify(new_user), 201

@users_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user_route(user_id):
    data = request.get_json()
    updated_user = service_update_user(user_id, data)
    if not updated_user:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    return jsonify(updated_user), 200

@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user_route(user_id):
    success = service_delete_user(user_id)
    if not success:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    return jsonify({'message': 'Usuario eliminado exitosamente'}), 200

@users_bp.route('/users', methods=['GET'])
def get_all_users_route():
    users = service_get_all_users()
    return jsonify(users), 200

@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id_route(user_id):
    user = service_get_user_by_id(user_id)
    if not user:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    else:
        return jsonify(user), 200