# Import standard library packages
from enum import Enum

# Import installed packages
from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.orm import relationship

# Import app code
from app.db.base_class import Base, DeletedMixin
from app.models.base_relations import users_roles


class Role(DeletedMixin, Base):
    __tablename__ = 'roles'
    # Own properties
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    # Relationships
    users = relationship("User", secondary=users_roles, back_populates="roles")


class RoleName(Enum):
    ADMIN = 1
    USER = 2
    PREMIUM = 3

