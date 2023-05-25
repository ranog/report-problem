from httpx import AsyncClient

from src.issue_repository import COLLECTION_NAME


async def test_it_should_ping_successfully(async_http_client: AsyncClient):
    response = await async_http_client.get('/v1/ping/')
    assert response.status_code == 200
    assert response.json() == {'ping': 'pong'}


async def test_it_should_successfully_create_a_new_issue(issue, clean_collection, async_http_client: AsyncClient):
    await clean_collection(COLLECTION_NAME)
    response = await async_http_client.post('/v1/report-new-issue/', json=issue)
    assert response.status_code == 200
