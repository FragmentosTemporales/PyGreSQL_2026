from .db import db, Base, ReBase


class Producto(ReBase):
    __tablename__ = 'producto'
    nombre = db.Column(db.String(50), nullable=False)
    codigo = db.Column(db.String(100), unique=True, nullable=False)
    marca = db.Column(db.String(50), nullable=True)
    valor = db.Column(db.Integer, nullable=True)

    @staticmethod
    def validate_codigo(codigo):
        if db.session.query(Producto).filter_by(codigo=codigo).first():
            raise ValueError("El código ya existe en la base de datos.")
        
    @staticmethod
    def get_producto_by_codigo(codigo):
        return db.session.query(Producto).filter_by(codigo=codigo).first()