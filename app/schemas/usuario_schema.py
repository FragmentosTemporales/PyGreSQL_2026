from flask_marshmallow import Marshmallow
from marshmallow import fields
from marshmallow_sqlalchemy import auto_field, SQLAlchemyAutoSchema
from ..models import Usuario
from ..models import db

ma = Marshmallow()


class BaseSchema(SQLAlchemyAutoSchema):
    class Meta:
        load_instance = True
        sqla_session = db.session


class UsuarioSchema(BaseSchema):
    class Meta(BaseSchema.Meta):
        model = Usuario
        include_fk = True

    id = auto_field(dump_only=True)
    nombre = auto_field(required=True)
    apellido = auto_field(required=True)
    correo = auto_field(required=True)
    clave = auto_field(load_only=True, required=True)


class LoginSchema(ma.Schema):
    """ Serializer for logs users in """
    correo = fields.Email(
        required=True,
        error_messages={
            "required": "El campo de correo es requerido.",
            "null": "Este campo de correo no debe estar vacío.",
            "validator_failed": "El correo ingresado no es válido.",
            "invalid": "El valor ingresado no es un correo electrónico válido.",
        }
    )
    clave = fields.String(
        required=True,
        error_messages={
            "required": "El campo de password es requerido.",
            "null": "Este campo de password no debe estar vacío.",
            "validator_failed": "La password ingresada no es válida.",
            "invalid": "El valor ingresado no es una contraseña válida."
        }
    )


login_schema = LoginSchema()

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)
