import sqlalchemy

from .db_session import SqlAlchemyBase


class Git(SqlAlchemyBase):
    __tablename__ = 'gites'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
