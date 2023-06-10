from datetime import datetime, timezone

import pytest
from google.cloud import firestore
from httpx import AsyncClient

from src.factory import build_issue
from src.main import app
from src.model import Defect, Priority, Status


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
def payload():
    return {
        'username': 'dummy name',
        'user_id': '111111111',
        'user_email': 'user@email.com',
        'contact_phone': 'AA 9NNNN-NNNN',
        'description': 'dummy description',
        'category': Defect.NOTEBOOK.value,
        'priority': Priority.HIGH.value,
        'created_at': str(datetime.now(timezone.utc)),
        'status': Status.TO_DO.value,
        'responsible_engineer': 'specific@engineer.com',
    }


@pytest.fixture
def new_issue(payload):
    return build_issue(payload)
