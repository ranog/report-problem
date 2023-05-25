from datetime import datetime

import pytest
from google.cloud import firestore
from httpx import AsyncClient

from src.main import app


TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%SZ'


@pytest.fixture
async def async_http_client() -> AsyncClient:
    async with AsyncClient(app=app, base_url='http://test') as async_client:
        yield async_client


@pytest.fixture
def clean_collection():
    async def _clean_collection(collection_path, async_client=firestore.AsyncClient()):
        async_collection_reference = async_client.collection(collection_path)
        await async_client.recursive_delete(reference=async_collection_reference)

    return _clean_collection


@pytest.fixture
def issue():
    return {
        'user_id': 1,
        'email': 'test@email.com',
        'description': 'dummy description',
        'category': 'dummy category',
        'priority': 'high',
        'created_at': datetime.utcnow().strftime(TIMESTAMP_FORMAT),
        'status': 1,
    }
