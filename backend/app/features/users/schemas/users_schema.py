from marshmallow import Schema, fields, validate, ValidationError

def validate_estudioenpenascal_email(value):
    if not value.lower().endswith('@estudioenpenascal.com'):
        raise ValidationError(
            'Solo se permiten correos con dominio @estudioenpenascal.com'
        )
        
class UserSchema(Schema):
    # Campos que el backend devuelve al frontend (Solo lectura)
    id = fields.Int(dump_only=True)
    
    # Mapeamos 'nombre_usuario' (API) con el atributo de tu servicio/modelo
    nombre_usuario = fields.Str(
        required=True, 
        validate=validate.Length(min=3, max=80),
        attribute="username" # Esto hace la magia de traducir username <-> nombre_usuario
    )
    
    email = fields.Email(
        required=True, 
        validate=[validate.Length(max=120), validate_estudioenpenascal_email]
    )
    
    # La contraseña solo se recibe, NUNCA se envía de vuelta en el JSON
    password = fields.Str(
        required=True, 
        load_only=True, 
        validate=validate.Length(min=6, max=128),
        attribute="password_hash"
    )
    
    role = fields.Str(
        validate=validate.OneOf(['user', 'admin']),
        load_default='user' # Valor por defecto si no se envía
    )

class UserCreateSchema(UserSchema):
    """Esquema específico para la creación de usuarios (usa las reglas base)"""
    pass

class UserUpdateSchema(UserSchema):
    """Esquema específico para actualizar. Los campos se vuelven opcionales."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Al actualizar, el cliente puede mandar solo un campo si quiere
        self.fields['nombre_usuario'].required = False
        self.fields['email'].required = False
        self.fields['password'].required = False