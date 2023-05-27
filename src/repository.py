import uuid

from google.cloud import firestore


COLLECTION_NAME = 'testing-report-problem'


class IssueRepository:
    def __init__(self):
        self.collection = firestore.AsyncClient().collection(COLLECTION_NAME)

    async def add(self, issue: dict):
        issue['id'] = str(uuid.uuid4())
        await self.collection.document().set(issue)
        return issue['id']

    async def get(self, issue_id: str):
        issues = await self.collection.where(field_path='id', op_string='==', value=issue_id).get()
        if issues:
            return issues[0].to_dict()
        return {}
