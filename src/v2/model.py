from datetime import datetime, timezone
from enum import Enum
from dataclasses import dataclass


@dataclass
class User:
    id: str
    name: str
    email: str
    phone_number: str


@dataclass
class Engineer:
    id: str
    name: str
    email: str


class Status(str, Enum):
    TO_DO = 'todo'
    IN_PROGRESS = 'in progress'
    DONE = 'done'


class Priority(str, Enum):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'


class Issue:
    user: User
    description: str
    priority: Priority
    status: Status = Status.TO_DO
    responsible_collaborator: Engineer
    created_at: datetime = datetime.now(timezone.utc)

    def __init__(self, user, description):
        self.user = user
        self.description = description

    def assign(self, engineer: Engineer):
        self.responsible_collaborator = engineer

    def change_status(self, status: Status):
        self.status = status

    def change_priority(self, priority: Priority):
        self.priority = priority
