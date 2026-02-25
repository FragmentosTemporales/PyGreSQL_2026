from marshmallow import fields
from marshmallow_sqlalchemy import auto_field, SQLAlchemyAutoSchema
from ..models import LogError, LogQuery
from ..models import db


class BaseSchema(SQLAlchemyAutoSchema):
    class Meta:
        load_instance = True
        sqla_session = db.session


class LogErrorSchema(BaseSchema):
    class Meta(BaseSchema.Meta):
        model = LogError
        include_fk = True

class LogQuerySchema(BaseSchema):
    class Meta(BaseSchema.Meta):
        model = LogQuery
        include_fk = True

log_error_schema = LogErrorSchema()
logs_error_schema = LogErrorSchema(many=True)

log_query_schema = LogQuerySchema()
logs_query_schema = LogQuerySchema(many=True)