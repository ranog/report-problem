import pytest

from src.v2.model import Issue, User


@pytest.fixture
def issue():
    return Issue(
        user=User(
            id='dummy_user_id',
            name='Dummy User',
            email='dummy_user_email',
            phone_number='dummy_user_phone',
        ),
        description='dummy_description',
    )
