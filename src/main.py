from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.services import create_issue, get_issue, get_issue_list


COLLECTION_NAME = 'testing-report-problem'


app = FastAPI()


@app.get('/v1/ping/')
async def root():
    return {'ping': 'pong'}


@app.post('/v1/report-issue/')
async def report_issue(json: dict):
    issue = await create_issue(json)
    if isinstance(issue, str):
        return JSONResponse(issue, status_code=200)
    return JSONResponse(issue, status_code=400)


@app.get('/v1/issue/{issue_id}/')
async def get_issue_by_id(issue_id: str):
    return await get_issue(issue_id)


@app.get('/v1/issues/')
async def get_issues(category: str, priority: str | None = None):
    issues = await get_issue_list(category=category, priority=priority)
    return JSONResponse(issues, status_code=200)


@app.patch('/v1/update-issue/{issue_id}/')
async def update_issues(issue_id: str, items: dict):
    return JSONResponse(content='update performed successfully', status_code=200)
