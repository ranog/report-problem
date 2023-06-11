from datetime import datetime, timezone
from enum import Enum

from pydantic import BaseModel, EmailStr, Field


class Defect(str, Enum):
    NOTEBOOK = 'notebook'
    SOFTWARE = 'software'
    PERIPHERAL = 'periferico'


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
    contact_phone: str
    description: str
    category: Defect
    priority: Priority
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    status: Status
    responsible_engineer: EmailStr = ''


class NotebookCheck(BaseModel):
    # high
    it_is_not_turning_on: bool = False
    power_button_is_not_working: bool = False
    screen_is_not_working: bool = False

    # medium
    keyboard_is_not_working: bool = False
    touchpad_is_not_working: bool = False
    not_connecting_to_the_internet: bool = False

    # low
    displays_error_message: bool = False
    does_not_recognize_peripherals: bool = False
    operating_system_does_not_start_correctly: bool = False
