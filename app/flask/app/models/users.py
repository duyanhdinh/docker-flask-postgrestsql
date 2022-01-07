# Import standard library packages
from uuid import uuid4

# Import installed packages
from sqlalchemy import Column, Integer, DateTime, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

# Import app code
from app.db.base_class import Base, DeletedMixin
from app.models.base_relations import users_roles


class User(DeletedMixin, Base):
    __tablename__ = 'users'
    # Own properties
    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String, unique=True, default=str(uuid4()))
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    is_verified = Column(Boolean(), default=False)
    # Relationships
    roles = relationship("Role", secondary=users_roles, back_populates="users")
    # socials = relationship('Social', backref='users', lazy=True, cascade="all, delete, delete-orphan")
    # profile = relationship('UserProfile', backref='users', lazy=True, uselist=False, cascade="all, delete, delete-orphan")

