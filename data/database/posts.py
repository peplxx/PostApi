import datetime

import sqlalchemy as sa
from sqlalchemy import orm

from .db_session import SqlAlchemyBase
from ..datatypes.posts import PostData


class Post(SqlAlchemyBase):
    __tablename__ = 'posts'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String, nullable=False)
    content = sa.Column(sa.String, nullable=False)
    published = sa.Column(sa.Boolean, nullable=False, default=True)
    created_at = sa.Column(sa.TIMESTAMP, nullable=False, default=datetime.datetime.now())

    def __repr__(self):
        return f"<Post {self.title=}, {self.content=}, {self.published=}>"

    @property
    def dict(self):
        items = self.__dict__
        items.pop("_sa_instance_state")
        return items

    def __init__(self,data: PostData):
        self.title= data.title
        self.content = data.content
        self.published = data.published
