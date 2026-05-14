from flask import Blueprint, request, jsonify
from ..services.users_service import create_user, update_user, delete_user, get_all_users, get_user_by_id    

# Creamos un Blueprint para las rutas de usuarios
users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = create_user(data)
    return jsonify(new_user.to_dict()), 201

@users_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    updated_user = update_user(user_id, data)
    if not updated_user:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    else:
        return jsonify(updated_user.to_dict()), 200
    
@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    success = delete_user(user_id)
    if not success:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    else:
        return jsonify({'message': 'Usuario eliminado exitosamente'}), 200
    
@users_bp.route('/users', methods=['GET'])
def get_all_users():
    users = get_all_users()
    return jsonify(users), 200

@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    else:
        return jsonify(user), 200