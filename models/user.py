from sqlalchemy import Boolean, Column, Enum, Integer, String
from backend.config.db import Base


class User(Base):
    
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String, index=True)
    phone = Column(String, index=True)
    role = Column(Enum("admin", "teacher", "parent", name="user_role"), index=True, nullable=False)
    timestamp = Column(String, index=True)
    updated_at = Column(String, index=True)
    is_active = Column(Boolean, index=True)