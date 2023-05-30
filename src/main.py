from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.service import create_new_issue, get_issue


COLLECTION_NAME = 'testing-report-problem'


app = FastAPI()


@app.get('/v1/ping/')
async def root():
    return {'ping': 'pong'}


@app.post('/v1/report-new-issue/')
async def report_new_issue(json: dict):
    issue = await create_new_issue(data=json)
    if isinstance(issue, str):
        return JSONResponse(issue, status_code=200)
    return JSONResponse(issue, status_code=400)


@app.get('/v1/{issue_id}/')
async def get_problem_by_id(issue_id: str):
    return await get_issue(issue_id)
