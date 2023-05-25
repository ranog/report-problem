from datetime import datetime

from httpx import AsyncClient

from src.main import COLLECTION_NAME


TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%SZ'


async def test_it_should_ping_successfully(async_http_client: AsyncClient):
    response = await async_http_client.get('/v1/ping/')
    assert response.status_code == 200
    assert response.json() == {'ping': 'pong'}


async def test_it_should_shorten_successfully(clean_collection, async_http_client: AsyncClient):
    await clean_collection(COLLECTION_NAME)
    payload = {
        'user_id': 1,
        'email': 'test@email.com',
        'description': 'dummy description',
        'category': 'dummy category',
        'priority': 'high',
        'date': datetime.utcnow().strftime(TIMESTAMP_FORMAT),
    }
    expected_issue_id = str(id(payload['user_id']))
    response = await async_http_client.post('/v1/new-issue/', json=payload)
    assert response.status_code == 200
    assert response.headers['location'] == expected_issue_id
