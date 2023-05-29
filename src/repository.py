from google.cloud import firestore

from src.model import NewIssue


COLLECTION_NAME = 'testing-report-problem'


class IssueRepository:
    def __init__(self):
        self.collection = firestore.AsyncClient().collection(COLLECTION_NAME)

    def _extract_enum_value(self, issue_doc):
        issue_doc['category'] = issue_doc['category'].value
        issue_doc['priority'] = issue_doc['priority'].value
        issue_doc['status'] = issue_doc['status'].value

    async def add(self, issue: NewIssue):
        doc_ref = self.collection.document()
        issue_doc = issue.dict()
        self._extract_enum_value(issue_doc)
        await doc_ref.set(issue_doc)
        return doc_ref.id

    async def get(self, issue_id: str):
        issue = await self.collection.document(issue_id).get()
        if issue.exists:
            return issue.to_dict()
        return {}
