from httpx import AsyncClient

from src.repository import COLLECTION_NAME


async def test_it_should_ping_successfully(async_http_client: AsyncClient):
    response = await async_http_client.get('/v1/ping/')
    assert response.status_code == 200
    assert response.json() == {'ping': 'pong'}


async def test_it_should_successfully_create_a_new_issue(issue, clean_collection, async_http_client: AsyncClient):
    await clean_collection(COLLECTION_NAME)
    response = await async_http_client.post('/v1/report-new-issue/', json=issue)
    assert response.status_code == 200


async def test_it_should_return_status_code_400_when_the_new_issue_is_empty(
    clean_collection,
    async_http_client: AsyncClient,
):
    await clean_collection(COLLECTION_NAME)
    response = await async_http_client.post('/v1/report-new-issue/', json={})
    assert response.status_code == 400
    assert response.json() == 'New issue cannot be empty'
