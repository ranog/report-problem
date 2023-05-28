from datetime import datetime
from enum import Enum

from pydantic import BaseModel, EmailStr


class DefectCategory(str, Enum):
    NOTEBOOK = 'Defeito no notebook'
    SOFTWARE = 'Problema com software'
    PERIPHERAL = 'Defeito em um periférico (Mouse, Teclado, Monitor, etc)'


class Status(str, Enum):
    TO_DO = 'to_do'
    IN_PROGRESS = 'in_progress'
    DONE = 'done'


class Priority(Enum):
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'


class CreateNewIssue(BaseModel):
    created_by: str
    email: EmailStr
    description: str
    category: DefectCategory
    priority: Priority
    created_at: datetime
    status: Status
    owner: EmailStr
