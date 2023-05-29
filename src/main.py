from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.service import create_new_issue


COLLECTION_NAME = 'testing-report-problem'


app = FastAPI()


@app.get('/v1/ping/')
async def root():
    return {'ping': 'pong'}


@app.post('/v1/report-new-issue/')
async def report_new_issue(json: dict):
    if json:
        issue_id = await create_new_issue(data=json)
        return JSONResponse(issue_id, status_code=200)
    return JSONResponse('New issue cannot be empty', status_code=400)
