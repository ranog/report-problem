from google.cloud import firestore

from src.model import NewIssue


COLLECTION_NAME = 'testing-report-problem'


class IssueRepository:
    def __init__(self):
        self.collection = firestore.AsyncClient().collection(COLLECTION_NAME)

    def _extract_enum_value(self, issue):
        issue_doc = issue.dict()
        issue_doc['category'] = issue_doc['category'].value
        issue_doc['priority'] = issue_doc['priority'].value
        issue_doc['status'] = issue_doc['status'].value
        return issue_doc

    def _convert_datetime(self, issue):
        issue_doc = issue.to_dict()
        issue_doc['created_at'] = str(issue_doc['created_at'])
        return issue_doc

    async def add(self, issue: NewIssue):
        doc_ref = self.collection.document()
        await doc_ref.set(self._extract_enum_value(issue))
        return doc_ref.id

    async def get(self, issue_id: str):
        issue = await self.collection.document(issue_id).get()
        if issue.exists:
            return self._convert_datetime(issue)
        return {}

    async def filter(self, category: str, priority: str):
        query = self.collection.where('category', '==', category).where('priority', '==', priority).stream()
        docs = [doc async for doc in query]
        sorted_docs = sorted(docs, key=lambda doc: doc.get('created_at'))
        return [self._convert_datetime(doc) for doc in sorted_docs]
