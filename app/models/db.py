from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import datetime as dt
from sqlalchemy import desc, func

# Inicialización de db y migrate
db = SQLAlchemy()
migrate = Migrate()


class Base(db.Model):
    """Model that contains base database models."""
    __abstract__ = True

    def save_to_db(self):
        """Save instance to the database."""
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    def update(self, **kwargs):
        """Update instance in the database."""
        for key, value in kwargs.items():
            setattr(self, key, value)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    def delete_from_db(self):
        """Delete instance from the database."""
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        """ Get all from db """
        return cls.query.all()


class ReBase(Base):
    """Model that contains base database models with read-only access."""
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha_registro = db.Column(db.DateTime, nullable=False, default=lambda: dt.datetime.now(dt.UTC)-dt.timedelta(hours=3))


    @classmethod
    def find_by_id(cls, id):
        """Encuentra registro por ID"""
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all_order_by_fecha_desc(cls):
        """Encuentra todos los registros ordenados por fecha de registro (descendente)"""
        return cls.query.order_by(desc(cls.fecha_registro)).all()

    @classmethod
    def get_paginated(cls, page, per_page):
    # Asegurarse de que la query esté bien formada antes de paginar
        return cls.query.order_by(desc(cls.fecha_registro)).paginate(page=page, per_page=per_page, error_out=False)
