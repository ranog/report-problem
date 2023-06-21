from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.model import Category, Notebook, Peripheral, Software
from src.repository import IssueRepository
from src.service import select_priority


COLLECTION_NAME = 'testing-report-problem'


app = FastAPI()


@app.get('/v1/ping/', include_in_schema=False)
async def root():
    return {'ping': 'pong'}


@app.post('/v1/report-notebook-issue/')
async def report_notebook_issue(notebook: Notebook):
    try:
        notebook.priority = select_priority(notebook)
    except ValueError as error:
        return JSONResponse(content=str(error), status_code=400)
    return await IssueRepository().add(notebook)


@app.post('/v1/report-software-issue/')
async def report_software_issue(software: Software):
    try:
        software.priority = select_priority(software)
    except ValueError as error:
        return JSONResponse(content=str(error), status_code=400)
    return await IssueRepository().add(software)


@app.post('/v1/report-peripheral-issue/')
async def report_peripheral_issue(peripheral: Peripheral):
    try:
        peripheral.priority = select_priority(peripheral)
    except ValueError as error:
        return JSONResponse(content=str(error), status_code=400)
    return await IssueRepository().add(peripheral)


@app.get('/v1/issue/{issue_id}/')
async def get_issue_by_id(issue_id: str):
    return await IssueRepository().get(issue_id)


@app.get('/v1/issues/')
async def get_issues(category: str = None, priority: str = None):
    return await IssueRepository().list(category=category, priority=priority)


@app.patch('/v1/update-issue/{issue_id}/')
async def update_issue(issue_id: str, items: dict):
    repository = IssueRepository()
    issue_doc = await repository.get(issue_id)
    if not issue_doc:
        return JSONResponse(content=f'{issue_id} not found.', status_code=404)
    for item in items.keys():
        if item not in issue_doc:
            return JSONResponse(content=f'{item} field not exist.', status_code=400)
    return await repository.update(issue_id=issue_id, items=items)


@app.get('/v1/payloads/{category}/')
async def payload(category: str):
    match category:
        case Category.NOTEBOOK.value:
            notebook = Notebook.schema()
            return {key: notebook['properties'][key]['type'] for key in notebook['required']}
        case Category.SOFTWARE.value:
            software = Software.schema()
            return {key: software['properties'][key]['type'] for key in software['required']}
        case Category.PERIPHERAL.value:
            peripheral = Peripheral.schema()
            return {key: peripheral['properties'][key]['type'] for key in peripheral['required']}
    return JSONResponse(
        content=(
            f'{category} not found. Categories with available payload: '
            f'{Category.NOTEBOOK.value}, {Category.SOFTWARE.value} and {Category.PERIPHERAL.value}'
        ),
        status_code=400,
    )
