from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid

from ..database.core import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String, nullable=False, unique=True)
    last_name = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)

    def __repr__(self):
        return f"<User(first_name={self.first_name}, last_name={self.last_name}, email={self.email})>"