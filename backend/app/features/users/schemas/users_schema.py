from marshmallow import Schema, fields, validate, ValidationError

def validate_estudioenpenascal_email(value):
    if not value.lower().endswith('@estudioenpenascal.com'):
        raise ValidationError(
            'Solo se permiten correos con dominio @estudioenpenascal.com'
        )
        
class UserSchema(Schema):
    # Read-only fields returned by the backend
    id = fields.Int(dump_only=True)

    # Maps API field 'nombre_usuario' to model attribute 'username'
    nombre_usuario = fields.Str(
        required=True,
        validate=validate.Length(min=3, max=80),
        attribute="username" # Translates username <-> nombre_usuario
    )

    email = fields.Email(
        required=True,
        validate=[validate.Length(max=120), validate_estudioenpenascal_email]
    )

    # Password is received from client but never included in API responses
    password = fields.Str(
        required=True,
        load_only=True,
        validate=validate.Length(min=6, max=128),
        attribute="password_hash"
    )

    role = fields.Str(
        validate=validate.OneOf(['user', 'admin']),
        load_default='user' # Default role if not provided
    )

class UserCreateSchema(UserSchema):
    """Schema for user creation (inherits base validation rules)."""
    pass

class UserUpdateSchema(UserSchema):
    """Schema for user updates. All fields become optional."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Client may send only the fields they want to update
        self.fields['nombre_usuario'].required = False
        self.fields['email'].required = False
        self.fields['password'].required = False