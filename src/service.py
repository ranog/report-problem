from pydantic import ValidationError

from src.factory import build_issue
from src.repository import IssueRepository


async def create_issue(data: dict, repository: IssueRepository = None):
    try:
        new_issue = build_issue(data)
    except ValidationError as error:
        messages = {}
        for error_doc in error.errors():
            for field in error_doc['loc']:
                messages[field] = f"'{data.get(field, '')}': {error_doc['msg']}"
        return messages
    if repository is None:
        repository = IssueRepository()
    return await repository.add(new_issue)


async def get_issue(issue_id: str, repository: IssueRepository = None):
    if repository is None:
        repository = IssueRepository()
    return await repository.get(issue_id)


async def get_issue_list(category: str, priority: str, repository: IssueRepository = None):
    if repository is None:
        repository = IssueRepository()
    return await repository.filter(category=category, priority=priority)
