from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from src.service import create_new_issue


COLLECTION_NAME = 'testing-report-problem'


app = FastAPI()


@app.get('/v1/ping/')
async def root():
    return {'ping': 'pong'}


@app.post('/v1/report-new-issue/')
async def report_new_issue(json: dict):
    try:
        issue_id = await create_new_issue(data=json)
    except ValidationError as error:
        messages = {}
        for error_doc in error.errors():
            for field in error_doc['loc']:
                messages[field] = error_doc['msg']
        return JSONResponse(messages, status_code=400)
    return JSONResponse(issue_id, status_code=200)
