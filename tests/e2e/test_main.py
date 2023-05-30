import pytest
from httpx import AsyncClient

from src.model import DefectCategory, Priority, Status
from src.repository import COLLECTION_NAME


async def test_it_should_ping_successfully(async_http_client: AsyncClient):
    response = await async_http_client.get('/v1/ping/')
    assert response.status_code == 200
    assert response.json() == {'ping': 'pong'}


async def test_it_should_successfully_create_a_new_issue(payload, clean_collection, async_http_client: AsyncClient):
    await clean_collection(COLLECTION_NAME)
    response = await async_http_client.post('/v1/report-new-issue/', json=payload)
    assert response.status_code == 200


@pytest.mark.parametrize('category_value', ['', 'dummy category'])
async def test_it_should_return_400_when_category_is_not_valid(
    payload,
    category_value,
    clean_collection,
    async_http_client: AsyncClient,
):
    await clean_collection(COLLECTION_NAME)
    payload['category'] = category_value
    response = await async_http_client.post('/v1/report-new-issue/', json=payload)
    expected_msg = {
        'category': (
            'value is not a valid enumeration member; permitted: '
            f"'{DefectCategory.NOTEBOOK.value}', '{DefectCategory.SOFTWARE.value}', '{DefectCategory.PERIPHERAL.value}'"
        )
    }
    assert response.status_code == 400
    assert response.json() == expected_msg


@pytest.mark.parametrize('priority_value', ['', 'dummy priority'])
async def test_it_should_return_400_when_priority_is_not_valid(
    payload,
    priority_value,
    clean_collection,
    async_http_client: AsyncClient,
):
    await clean_collection(COLLECTION_NAME)
    payload['priority'] = priority_value
    response = await async_http_client.post('/v1/report-new-issue/', json=payload)
    expected_msg = {
        'priority': (
            'value is not a valid enumeration member; permitted: '
            f"'{Priority.HIGH.value}', '{Priority.MEDIUM.value}', '{Priority.LOW.value}'"
        )
    }
    assert response.status_code == 400
    assert response.json() == expected_msg


@pytest.mark.parametrize('status_value', ['', 'dummy status'])
async def test_it_should_return_400_when_status_is_not_valid(
    payload,
    status_value,
    clean_collection,
    async_http_client: AsyncClient,
):
    await clean_collection(COLLECTION_NAME)
    payload['status'] = status_value
    response = await async_http_client.post('/v1/report-new-issue/', json=payload)
    expected_msg = {
        'status': (
            'value is not a valid enumeration member; permitted: '
            f"'{Status.TO_DO.value}', '{Status.IN_PROGRESS.value}', '{Status.DONE.value}'"
        )
    }
    assert response.status_code == 400
    assert response.json() == expected_msg


async def test_it_should_return_status_code_400_when_the_new_issue_is_empty(
    clean_collection,
    async_http_client: AsyncClient,
):
    await clean_collection(COLLECTION_NAME)
    response = await async_http_client.post('/v1/report-new-issue/', json={})
    assert response.status_code == 400
    expected_msg = {
        'created_by': 'field required',
        'email': 'field required',
        'description': 'field required',
        'category': 'field required',
        'priority': 'field required',
        'status': 'field required',
        'owner': 'field required',
    }
    assert response.json() == expected_msg
