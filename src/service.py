from src.factory import build_new_issue
from src.repository import IssueRepository


async def create_new_issue(data: dict, repository: IssueRepository = IssueRepository()):
    new_issue = build_new_issue(data)
    return await repository.add(new_issue)
