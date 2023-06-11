from datetime import datetime, timezone
from enum import Enum

from pydantic import BaseModel, EmailStr, Field


class Defect(str, Enum):
    NOTEBOOK = 'notebook'
    SOFTWARE = 'software'
    PERIPHERAL = 'peripheral'


class Status(str, Enum):
    TO_DO = 'todo'
    IN_PROGRESS = 'in progress'
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


class SoftwareCheck(BaseModel):
    name: str

    # high
    it_is_not_installed_correctly: bool = False
    run_with_errors: bool = False
    does_not_respond_to_commands_and_interactions: bool = False

    # medium
    not_displaying_data_and_content_correctly: bool = False
    generates_unexpected_results: bool = False
    not_integrating_with_other_systems_or_devices: bool = False

    # low
    not_using_required_system_resources: bool = False
    not_maintaining_security_and_not_protecting_data: bool = False
    it_is_not_updated_with_the_latest_versions: bool = False
    other_users_are_having_the_same_problem: bool = False
