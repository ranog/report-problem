from datetime import datetime, timezone
from enum import Enum

from pydantic import BaseModel, EmailStr, Field


class Category(str, Enum):
    NOTEBOOK = 'notebook'
    SOFTWARE = 'software'
    PERIPHERAL = 'peripheral'


class Status(str, Enum):
    TO_DO = 'todo'
    IN_PROGRESS = 'in progress'
    DONE = 'done'


class Priority(str, Enum):
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'


class BasePayload(BaseModel):
    username: str
    user_id: str
    user_email: EmailStr
    contact_phone: str
    description: str
    priority: Priority = Priority.HIGH
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    status: Status = Status.TO_DO
    responsible_engineer: EmailStr = None
