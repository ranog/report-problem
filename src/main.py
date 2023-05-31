from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.service import create_issue, get_issue, get_issue_list


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


@app.get('/v1/{issue_id}/')
async def get_issue_by_id(issue_id: str):
    return await get_issue(issue_id)


@app.get('/v1/issue-list/{category}/{priority}/')
async def get_issues(category: str, priority: str):
    issues = await get_issue_list(category=category, priority=priority)
    return JSONResponse(issues, status_code=200)
