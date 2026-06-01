# JWT lifetime and token location settings
from datetime import timedelta

class JWTConfig:
    JWT_TOKEN_LOCATION = ['headers']
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)