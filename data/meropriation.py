import sqlalchemy

from .db_session import SqlAlchemyBase


class Meropriation(SqlAlchemyBase):
    __tablename__ = 'meropriations'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=True)
