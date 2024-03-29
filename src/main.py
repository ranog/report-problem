from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from src.repository import IssueRepository
from src.v1.models.base_payload import Category
from src.v1.models.notebook import Notebook
from src.v1.models.peripheral import Peripheral
from src.v1.models.software import Software


app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, error):
    return JSONResponse(status_code=400, content={'detail': 'Validation error', 'errors': error.errors()})


@app.get('/v1/ping/', include_in_schema=False)
async def root():
    return {'ping': 'pong'}


@app.post('/v1/report-notebook-issue/')
async def report_notebook_issue(notebook: Notebook):
    return await IssueRepository().add(notebook)


@app.post('/v1/report-software-issue/')
async def report_software_issue(software: Software):
    return await IssueRepository().add(software)


@app.post('/v1/report-peripheral-issue/')
async def report_peripheral_issue(peripheral: Peripheral):
    return await IssueRepository().add(peripheral)


@app.get('/v1/issue/{issue_id}/')
async def get_issue_by_id(issue_id: str):
    return await IssueRepository().get(issue_id)


@app.get('/v1/issues/')
async def get_issues(category: str = None, priority: str = None):
    return await IssueRepository().list(category=category, priority=priority)


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
