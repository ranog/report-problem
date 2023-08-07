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


class Issue:
    user: User
    description: str
    priority: str
    created_at: str
    status: str
    responsible_collaborator: str

    def __init__(self, user, description, priority, created_at, status, responsible_collaborator):
        self.user = user
        self.description = description
        self.priority = priority
        self.created_at = created_at
        self.status = status
        self.responsible_collaborator = responsible_collaborator

    def assign(self, engineer: Engineer):
        self.responsible_collaborator = engineer.email
