from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from ..services.auth_service import login_user, logout_user, refresh_access_token

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/auth/login', methods=['POST'])
def login():                              # Public: authenticate user, returns tokens
    data = request.get_json(silent=True)
    if not data:
        return jsonify({'error': 'No input data provided'}), 422

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 422

    result = login_user(email, password)
    if result is None:
        return jsonify({'error': 'Invalid email or password'}), 401

    return jsonify(result), 200


@auth_bp.route('/auth/logout', methods=['POST'])
@jwt_required()
def logout():                             # Protected: revoke current token
    jti = get_jwt()['jti']
    token_type = get_jwt()['type']
    logout_user(jti, token_type)
    return jsonify({'message': 'Logged out successfully'}), 200


@auth_bp.route('/auth/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():                            # Protected (refresh token): get new access token
    identity = get_jwt_identity()
    result = refresh_access_token(identity)
    return jsonify(result), 200
