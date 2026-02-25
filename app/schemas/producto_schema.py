from marshmallow import fields
from marshmallow_sqlalchemy import auto_field, SQLAlchemyAutoSchema
from ..models import Producto
from ..models import db


class BaseSchema(SQLAlchemyAutoSchema):
    class Meta:
        load_instance = True
        sqla_session = db.session


class ProductoSchema(BaseSchema):
    class Meta(BaseSchema.Meta):
        model = Producto
        include_fk = True

    id = auto_field(dump_only=True)
    nombre = auto_field(required=True)
    codigo = auto_field(required=True, validate=Producto.validate_codigo, error_messages={"validator_failed": "El código ya existe en la base de datos."})
    marca = auto_field(required=False)
    valor = auto_field(required=False)

    #VALIDACION CODIGO UNICO



producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)
