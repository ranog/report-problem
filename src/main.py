from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from src.factory import build_issue
from src.repository import IssueRepository


COLLECTION_NAME = 'testing-report-problem'


app = FastAPI()


@app.get('/v1/ping/')
async def root():
    return {'ping': 'pong'}


@app.post('/v1/report-issue/')
async def report_issue(json: dict):
    try:
        new_issue = build_issue(json)
    except ValidationError as error:
        return JSONResponse(content=str(error), status_code=400)
    return await IssueRepository().add(new_issue)


@app.get('/v1/issue/{issue_id}/')
async def get_issue_by_id(issue_id: str):
    return await IssueRepository().get(issue_id)


@app.get('/v1/issues/')
async def get_issues(category: str = None, priority: str = None):
    return await IssueRepository().list(category=category, priority=priority)


@app.patch('/v1/update-issue/{issue_id}/')
async def update_issues(issue_id: str, items: dict):
    return JSONResponse(content='update performed successfully', status_code=200)
