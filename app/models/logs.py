from .db import db, Base, ReBase


class LogError(ReBase):
    __tablename__ = 'log_error'
    function_name = db.Column(db.String(100), nullable=False)
    error_message = db.Column(db.Text, nullable=False)


class LogQuery(ReBase):
    __tablename__="log_query"
    endpoint = db.Column(db.String(255), nullable=False)
    method = db.Column(db.String(10), nullable=False)
    url = db.Column(db.String(255), nullable=True)
