import sqlalchemy

from .db_session import SqlAlchemyBase


class Version(SqlAlchemyBase):
    __tablename__ = 'versions'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    git_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    number = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    text = sqlalchemy.Column(sqlalchemy.String, nullable=True)
