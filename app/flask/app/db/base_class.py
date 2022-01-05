from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Column, DateTime, Integer, ForeignKey
from datetime import datetime
from sqlalchemy.sql import func


class CustomBase(object):
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(self):
        return self.__name__.lower()

    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())


Base = declarative_base(cls=CustomBase)

class DeletedMixin:
    deleted_at = Column(DateTime, nullable=True, server_default=None)

class UserToMixin:
    @declared_attr
    def user_id(self):
        return Column('user_id', ForeignKey('users.id'), nullable=False, index=True)
