from datetime import datetime, timezone
from enum import Enum

from pydantic import BaseModel, EmailStr, Field


class DefectCategory(str, Enum):
    NOTEBOOK = 'Defeito no notebook'
    SOFTWARE = 'Problema com software'
    PERIPHERAL = 'Defeito em um periferico (Mouse, Teclado, Monitor, etc)'


class Status(str, Enum):
    TO_DO = 'to_do'
    IN_PROGRESS = 'in_progress'
    DONE = 'done'


class Priority(Enum):
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'


class NewIssue(BaseModel):
    username: str
    user_id: str
    user_email: EmailStr
    description: str
    category: DefectCategory
    priority: Priority
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    status: Status
    owner_email: EmailStr
