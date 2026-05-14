from flask import Blueprint, request, jsonify
from ..services.users_service import create_user, update_user, delete_user, get_all_users, get_user_by_id    

# Creamos un Blueprint para las rutas de usuarios
users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = create_user(data)
    return jsonify(new_user.to_dict()), 201

