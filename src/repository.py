from google.cloud import firestore


COLLECTION_NAME = 'testing-report-problem'


class IssueRepository:
    def __init__(self):
        self.collection = firestore.AsyncClient().collection(COLLECTION_NAME)

    async def add(self, issue: dict):
        doc_ref = self.collection.document()
        await doc_ref.set(issue)
        return doc_ref.id

    async def get(self, issue_id: str):
        issues = await self.collection.document(issue_id).get()
        if issues.exists:
            return issues.to_dict()
        return {}
