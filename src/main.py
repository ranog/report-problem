from fastapi import FastAPI, Response
from google.cloud import firestore


COLLECTION_NAME = 'testing-report-problem'


app = FastAPI()


@app.get('/v1/ping/')
async def root():
    return {'ping': 'pong'}


@app.post('/v1/new-issue/')
async def new_issue(json: dict):
    collection = firestore.AsyncClient().collection(COLLECTION_NAME)
    await collection.document(str(id(json['user_id']))).set(json)
    issues = await collection.where(field_path='user_id', op_string='==', value=json['user_id']).get()
    return Response(headers={'location': issues[0].id}, status_code=200)
