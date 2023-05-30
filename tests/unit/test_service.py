from src.model import NewIssue
from src.repository import IssueRepository
from src.service import create_new_issue


class FakeIssueRepository(IssueRepository):
    def __init__(self):
        self.logs = []

    def _extract_enum_value(self, issue_doc):
        pass

    async def add(self, issue: NewIssue):
        self.logs.append(issue)

    async def get(self, issue_id: str):
        pass


async def test_it_should_persist_the_new_issue(new_issue):
    repository = FakeIssueRepository()
    await create_new_issue(vars(new_issue), repository)
    assert repository.logs[0].user_id == new_issue.user_id
    assert repository.logs[0].user_email == new_issue.user_email
    assert repository.logs[0].description == new_issue.description
    assert repository.logs[0].category == new_issue.category
    assert repository.logs[0].priority == new_issue.priority
    assert repository.logs[0].created_at == new_issue.created_at
    assert repository.logs[0].status == new_issue.status
    assert repository.logs[0].owner_email == new_issue.owner_email
