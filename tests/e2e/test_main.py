from datetime import datetime, timezone

import pytest
from httpx import AsyncClient

from src.model import Defect, Priority, Status
from src.repository import COLLECTION_NAME


async def test_it_should_ping_successfully(async_http_client: AsyncClient):
    response = await async_http_client.get('/v1/ping/')

    assert response.status_code == 200
    assert response.json() == {'ping': 'pong'}


async def test_it_should_successfully_create_a_new_issue(payload, clean_collection, async_http_client: AsyncClient):
    await clean_collection(COLLECTION_NAME)

    response = await async_http_client.post('/v1/report-issue/', json=payload)

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
    expected_msg = (
        '1 validation error for NewIssue\n'
        'category\n'
        '  value is not a valid enumeration member; '
        f"permitted: '{Defect.NOTEBOOK.value}', '{Defect.SOFTWARE.value}', '{Defect.PERIPHERAL.value}' "
        '(type=type_error.enum; '
        "enum_values=[<Defect.NOTEBOOK: 'notebook'>, <Defect.SOFTWARE: 'software'>, <Defect.PERIPHERAL: 'periferico'>])"
    )

    response = await async_http_client.post('/v1/report-issue/', json=payload)

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
    expected_msg = (
        '1 validation error for NewIssue\n'
        'priority\n'
        '  value is not a valid enumeration member; '
        f"permitted: '{Priority.HIGH.value}', '{Priority.MEDIUM.value}', '{Priority.LOW.value}' "
        '(type=type_error.enum; '
        "enum_values=[<Priority.HIGH: 'high'>, <Priority.MEDIUM: 'medium'>, <Priority.LOW: 'low'>])"
    )

    response = await async_http_client.post('/v1/report-issue/', json=payload)

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
    expected_msg = (
        '1 validation error for NewIssue\n'
        'status\n'
        '  value is not a valid enumeration member; '
        f"permitted: '{Status.TO_DO.value}', '{Status.IN_PROGRESS.value}', '{Status.DONE.value}' "
        '(type=type_error.enum; '
        "enum_values=[<Status.TO_DO: 'to_do'>, <Status.IN_PROGRESS: 'in_progress'>, <Status.DONE: 'done'>])"
    )

    response = await async_http_client.post('/v1/report-issue/', json=payload)

    assert response.status_code == 400
    assert response.json() == expected_msg


async def test_it_should_return_status_code_400_when_the_new_issue_is_empty(
    clean_collection,
    async_http_client: AsyncClient,
):
    await clean_collection(COLLECTION_NAME)
    expected_msg = (
        '8 validation errors for NewIssue\n'
        'username\n'
        '  field required (type=value_error.missing)\n'
        'user_id\n'
        '  field required (type=value_error.missing)\n'
        'user_email\n'
        '  field required (type=value_error.missing)\n'
        'description\n'
        '  field required (type=value_error.missing)\n'
        'category\n'
        '  field required (type=value_error.missing)\n'
        'priority\n'
        '  field required (type=value_error.missing)\n'
        'status\n'
        '  field required (type=value_error.missing)\n'
        'owner_email\n'
        '  field required (type=value_error.missing)'
    )

    response = await async_http_client.post('/v1/report-issue/', json={})

    assert response.status_code == 400
    assert response.json() == expected_msg


async def test_it_should_successfully_get_issue(payload, clean_collection, async_http_client: AsyncClient):
    await clean_collection(COLLECTION_NAME)
    issue_info = await async_http_client.post('/v1/report-issue/', json=payload)

    response = await async_http_client.get(f'/v1/issue/{issue_info.json()}/')

    assert response.status_code == 200
    assert response.json() == payload


async def test_it_should_return_status_404_when_not_providing_an_id(clean_collection, async_http_client: AsyncClient):
    await clean_collection(COLLECTION_NAME)

    response = await async_http_client.get('/v1/issue/')

    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}


async def test_it_should_return_an_empty_dict_when_passing_the_issue_id_which_does_not_exist(
    clean_collection,
    async_http_client: AsyncClient,
):
    await clean_collection(COLLECTION_NAME)

    response = await async_http_client.get('/v1/issue/dummy_id/')

    assert response.status_code == 200
    assert response.json() == {}


async def test_it_should_successfully_issue_list(payload, clean_collection, async_http_client: AsyncClient):
    await clean_collection(COLLECTION_NAME)
    payload_2 = {
        'username': 'dummy name',
        'user_id': '99999999999999',
        'user_email': 'user_2@email.com',
        'description': 'dummy description',
        'category': Defect.SOFTWARE.value,
        'priority': Priority.MEDIUM.value,
        'created_at': str(datetime(2022, 1, 31, 10, 0, 0, tzinfo=timezone.utc)),
        'status': Status.TO_DO.value,
        'owner_email': 'other_specific@engineer.com',
    }
    payload_3 = {
        'username': 'dummy name',
        'user_id': '111111111',
        'user_email': 'user@email.com',
        'description': 'dummy description',
        'category': Defect.SOFTWARE.value,
        'priority': Priority.MEDIUM.value,
        'created_at': str(datetime.now(timezone.utc)),
        'status': Status.TO_DO.value,
        'owner_email': 'specific@engineer.com',
    }
    await async_http_client.post('/v1/report-issue/', json=payload)
    await async_http_client.post('/v1/report-issue/', json=payload_2)
    await async_http_client.post('/v1/report-issue/', json=payload_3)

    response = await async_http_client.get(
        f'/v1/issues/?category={Defect.SOFTWARE.value}&priority={Priority.MEDIUM.value}'
    )

    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json() == [payload_2, payload_3]


@pytest.mark.parametrize(
    'category_value, priority_value',
    [
        (Defect.NOTEBOOK.value, 'dummy_priority'),
        ('dummy_category', Priority.MEDIUM.value),
        ('dummy_category', 'dummy_priority'),
        (Defect.NOTEBOOK.value, ''),
        ('', Priority.MEDIUM.value),
        ('', ''),
    ],
)
async def test_it_should_return_an_empty_list_when_providing_incorrect_parameters(
    category_value,
    priority_value,
    clean_collection,
    async_http_client: AsyncClient,
):
    await clean_collection(COLLECTION_NAME)

    response = await async_http_client.get(f'/v1/issues/?category={category_value}&priority={priority_value}')

    assert response.status_code == 200
    assert response.json() == []


async def test_it_should_successfully_update_issue(clean_collection, async_http_client: AsyncClient):
    await clean_collection(COLLECTION_NAME)
    items = {'owner_email': 'another@engineer.com'}

    response = await async_http_client.patch('/v1/update-issue/dummy_id/', json=items)

    assert response.status_code == 200
    assert response.json() == 'update performed successfully'
