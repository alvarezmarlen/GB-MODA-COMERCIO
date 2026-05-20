from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from ..schemas import UserCreateSchema, UserUpdateSchema
from ..services.users_service import (
    create_user as service_create_user,
    update_user as service_update_user,
    delete_user as service_delete_user,
    get_all_users as service_get_all_users,
    get_user_by_id as service_get_user_by_id
)

users_bp = Blueprint('users', __name__)

# Instanciamos los schemas
user_create_schema = UserCreateSchema()
user_update_schema = UserUpdateSchema()

@users_bp.route('/users', methods=['POST'])
def create_user_route():
    json_data = request.get_json()
    if not json_data:
        return jsonify({'error': 'No se proporcionaron datos'}), 400
    
    # 1. Validar y deserializar los datos
    try:
        data = user_create_schema.load(json_data)
    except ValidationError as err:
        # Devuelve un error 400 con los campos exactos que fallaron
        return jsonify({'errors': err.messages}), 400
        
    # 2. Pasar los datos limpios al servicio
    new_user = service_create_user(data)
    return jsonify(new_user), 201

@users_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user_route(user_id):
    json_data = request.get_json()
    if not json_data:
        return jsonify({'error': 'No se proporcionaron datos'}), 400
        
    # 1. Validar datos de actualización
    try:
        data = user_update_schema.load(json_data)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    
    # 2. Pasar al servicio
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
    return jsonify(user), 200


