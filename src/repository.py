from google.cloud import firestore
from pydantic import BaseModel


COLLECTION_NAME = 'testing-report-problem'


class IssueRepository:
    def __init__(self):
        self.collection = firestore.AsyncClient().collection(COLLECTION_NAME)

    def _convert_datetime(self, issue):
        issue_doc = issue.to_dict()
        issue_doc['created_at'] = str(issue_doc['created_at'])
        return issue_doc

    async def add(self, issue: BaseModel):
        doc_ref = self.collection.document()
        await doc_ref.set(issue.dict())
        return doc_ref.id

    async def get(self, issue_id: str):
        issue = await self.collection.document(issue_id).get()
        if issue.exists:
            return self._convert_datetime(issue)
        return {}

    async def list(self, category: str = None, priority: str = None):
        query = self.collection.order_by('created_at')

        if category:
            query = query.where('category', '==', category)

        if priority:
            query = query.where('priority', '==', priority)

        return [self._convert_datetime(issue) for issue in await query.get()]

    async def update(self, issue_id: str, items: dict):
        issue_ref = self.collection.document(issue_id)
        await issue_ref.update(items)
