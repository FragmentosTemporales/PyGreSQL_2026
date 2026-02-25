from werkzeug.security import generate_password_hash, check_password_hash
from .db import db, Base, ReBase


class Usuario(ReBase):
    __tablename__ = 'usuario'
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    clave = db.Column(db.String(255), nullable=False)

    @staticmethod
    def hash_password(password):
        return generate_password_hash(password)

    @staticmethod
    def verify_password(password, hashed_password):
        return check_password_hash(hashed_password, password)

    @staticmethod
    def get_usuario_by_correo(correo):
        return db.session.query(Usuario).filter_by(correo=correo).first()

    @staticmethod
    def validate_correo(correo):
        if db.session.query(Usuario).filter_by(correo=correo).first():
            raise ValueError("El correo ya existe en la base de datos.")

    @staticmethod
    def validate_correo_structure(correo):
        if "@" not in correo or "." not in correo:
            raise ValueError("El correo no tiene una estructura válida.")

    @staticmethod
    def find_by_correo(correo):
        return db.session.query(Usuario).filter_by(correo=correo).first()