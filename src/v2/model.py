from dataclasses import dataclass
from enum import Enum


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


class Issue:
    user: User
    description: str
    priority: str
    created_at: str
    status: Status
    responsible_collaborator: str

    def __init__(self, user, description, priority, created_at, responsible_collaborator, status=Status.TO_DO):
        self.user = user
        self.description = description
        self.priority = priority
        self.created_at = created_at
        self.status = status
        self.responsible_collaborator = responsible_collaborator

    def assign(self, engineer: Engineer):
        self.responsible_collaborator = engineer.email

    def change_status(self, status: Status):
        self.status = status
