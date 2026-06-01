from flask_jwt_extended import create_access_token, create_refresh_token, get_jti
from ...users.services.users_service import verify_password
from ...users.models.users import User
from ..models.token_blacklist import TokenBlacklist
from .... import db


# Returns access + refresh tokens on valid credentials, None otherwise
def login_user(email, password):
    user = User.query.filter_by(email=email).first()
    if not user or not verify_password(user, password):
        return None

    access_token = create_access_token(identity=str(user.id))
    refresh_token = create_refresh_token(identity=str(user.id))

    return {
        'access_token': access_token,
        'refresh_token': refresh_token,
        'user': user.to_dict()
    }


# Blacklist token JTI on logout to prevent reuse
def logout_user(jti, token_type):
    blacklisted = TokenBlacklist.query.filter_by(jti=jti).first()
    if blacklisted:
        return False
    entry = TokenBlacklist(jti=jti, token_type=token_type)
    db.session.add(entry)
    db.session.commit()
    return True


def is_token_revoked(jti):
    return TokenBlacklist.query.filter_by(jti=jti).first() is not None


def refresh_access_token(identity):
    new_access_token = create_access_token(identity=identity)
    return {'access_token': new_access_token}
