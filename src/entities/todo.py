import uuid
import enum

from sqlalchemy import Column, Boolean, Enum, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime, timezone


class Priority(enum.Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3    


class Todo():
    __tablename__ = "todos"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    due_date = Column(DateTime, nullable=True)
    description = Column(String, nullable=False)
    is_completed = Column(Boolean, default=False)
    priority = Column(Enum(Priority), nullable=False, default=Priority.LOW)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    def __repr__(self):
        return f"<Todo(id={self.id}, user_id={self.user_id}, due_date={self.due_date}, description={self.description}, is_completed={self.is_completed}, priority={self.priority}, created_at={self.created_at})>"



