import os
from datetime import datetime, timezone

import pytest
from google.api_core.exceptions import NotFound

from src.factory import build_issue
from src.model import Defect, Priority, Status
from src.repository import COLLECTION_NAME, IssueRepository


async def test_it_should_persist_in_the_repository(clean_collection, new_issue):
    await clean_collection(COLLECTION_NAME)
    issue_repository = IssueRepository()
    issue_id = await issue_repository.add(new_issue)
    response = await issue_repository.get(issue_id)
    new_issue_doc = new_issue.dict()
    new_issue_doc['category'] = new_issue_doc['category'].value
    new_issue_doc['priority'] = new_issue_doc['priority'].value
    new_issue_doc['status'] = new_issue_doc['status'].value
    new_issue_doc['created_at'] = str(new_issue_doc['created_at'])
    assert response == new_issue_doc


async def test_it_should_add_two_new_issues_but_ids_should_be_different(clean_collection, new_issue):
    await clean_collection(COLLECTION_NAME)
    issue_repository = IssueRepository()
    await issue_repository.add(new_issue)
    await issue_repository.add(new_issue)
    issues = await issue_repository.collection.where(
        field_path='user_id',
        op_string='==',
        value=new_issue.user_id,
    ).get()
    assert len(issues) == 2
    assert issues[0].id != issues[1].id


async def test_it_should_return_an_empty_dict_when_the_issue_id_does_not_exist_in_the_repository(clean_collection):
    await clean_collection(COLLECTION_NAME)
    issue = await IssueRepository().get('dummy_issue_id')
    assert issue == {}


async def test_it_should_return_list_of_issues_when_given_correct_parameters(payload, clean_collection):
    await clean_collection(COLLECTION_NAME)
    payload_2 = {
        'username': 'dummy name',
        'user_id': '99999999999999',
        'user_email': 'user_2@email.com',
        'contact_phone': 'AA 9NNNN-NNNN',
        'description': 'dummy description',
        'category': Defect.SOFTWARE.value,
        'priority': Priority.MEDIUM.value,
        'created_at': str(datetime(2022, 1, 31, 10, 0, 0, tzinfo=timezone.utc)),
        'status': Status.TO_DO.value,
        'responsible_engineer': 'other_specific@engineer.com',
    }
    payload_3 = {
        'username': 'dummy name',
        'user_id': '111111111',
        'user_email': 'user@email.com',
        'contact_phone': 'AA 9NNNN-NNNN',
        'description': 'dummy description',
        'category': Defect.SOFTWARE.value,
        'priority': Priority.MEDIUM.value,
        'created_at': str(datetime.now(timezone.utc)),
        'status': Status.TO_DO.value,
        'responsible_engineer': 'specific@engineer.com',
    }
    repository = IssueRepository()
    await repository.add(build_issue(payload))
    await repository.add(build_issue(payload_2))
    await repository.add(build_issue(payload_3))

    issues = await repository.list(category=Defect.SOFTWARE.value, priority=Priority.MEDIUM.value)

    assert len(issues) == 2
    assert issues == [payload_2, payload_3]


@pytest.mark.parametrize(
    'category_value, priority_value',
    [
        ('', Priority.MEDIUM.value),
        ('dummy value for category', Priority.MEDIUM.value),
        (Defect.NOTEBOOK.value, ''),
        (Defect.NOTEBOOK.value, 'dummy value for priority'),
    ],
)
async def test_it_should_return_an_empty_list_when_not_given_the_correct_parameters(
    category_value,
    priority_value,
    clean_collection,
):
    await clean_collection(COLLECTION_NAME)
    repository = IssueRepository()
    issues = await repository.list(category=category_value, priority=priority_value)

    assert issues == []


async def test_it_should_return_items_from_the_given_category(payload, clean_collection):
    await clean_collection(COLLECTION_NAME)
    payload_2 = {
        'username': 'dummy name',
        'user_id': '99999999999999',
        'user_email': 'user_2@email.com',
        'contact_phone': 'AA 9NNNN-NNNN',
        'description': 'dummy description',
        'category': Defect.SOFTWARE.value,
        'priority': Priority.MEDIUM.value,
        'created_at': str(datetime(2022, 1, 31, 10, 0, 0, tzinfo=timezone.utc)),
        'status': Status.TO_DO.value,
        'responsible_engineer': 'other_specific@engineer.com',
    }
    payload_3 = {
        'username': 'dummy name',
        'user_id': '111111111',
        'user_email': 'user@email.com',
        'contact_phone': 'AA 9NNNN-NNNN',
        'description': 'dummy description',
        'category': Defect.SOFTWARE.value,
        'priority': Priority.HIGH.value,
        'created_at': str(datetime.now(timezone.utc)),
        'status': Status.DONE.value,
        'responsible_engineer': 'specific@engineer.com',
    }
    repository = IssueRepository()
    await repository.add(build_issue(payload))
    await repository.add(build_issue(payload_2))
    await repository.add(build_issue(payload_3))

    issues = await repository.list(category=Defect.SOFTWARE.value)

    assert len(issues) == 2
    assert issues == [payload_2, payload_3]


async def test_it_should_return_items_of_given_priority(payload, clean_collection):
    await clean_collection(COLLECTION_NAME)
    payload_2 = {
        'username': 'dummy name',
        'user_id': '99999999999999',
        'user_email': 'user_2@email.com',
        'contact_phone': 'AA 9NNNN-NNNN',
        'description': 'dummy description',
        'category': Defect.SOFTWARE.value,
        'priority': Priority.MEDIUM.value,
        'created_at': str(datetime(2022, 1, 31, 10, 0, 0, tzinfo=timezone.utc)),
        'status': Status.TO_DO.value,
        'responsible_engineer': 'other_specific@engineer.com',
    }
    payload_3 = {
        'username': 'dummy name',
        'user_id': '111111111',
        'user_email': 'user@email.com',
        'contact_phone': 'AA 9NNNN-NNNN',
        'description': 'dummy description',
        'category': Defect.SOFTWARE.value,
        'priority': Priority.HIGH.value,
        'created_at': str(datetime.now(timezone.utc)),
        'status': Status.DONE.value,
        'responsible_engineer': 'specific@engineer.com',
    }
    repository = IssueRepository()
    await repository.add(build_issue(payload))
    await repository.add(build_issue(payload_2))
    await repository.add(build_issue(payload_3))

    issues = await repository.list(priority=Priority.HIGH.value)

    assert len(issues) == 2
    assert issues == [payload, payload_3]


async def test_it_should_update_all_fields_provided(payload, clean_collection):
    await clean_collection(COLLECTION_NAME)
    repository = IssueRepository()
    issue_id = await repository.add(build_issue(payload))
    item_to_update = {
        'responsible_engineer': 'email@updated.com',
        'status': Status.IN_PROGRESS.value,
        'priority': Priority.LOW.value,
    }

    await repository.update(issue_id=issue_id, items=item_to_update)

    issue = await repository.get(issue_id)

    assert issue['responsible_engineer'] == item_to_update['responsible_engineer']
    assert issue['status'] == item_to_update['status']
    assert issue['priority'] == item_to_update['priority']


async def test_should_raise_an_exception_when_passing_an_issue_id_that_does_not_exist(clean_collection):
    await clean_collection(COLLECTION_NAME)

    expected_msg = (
        '404 No document to update: '
        f"projects/{os.environ['GCLOUD_PROJECT']}/databases/(default)/documents/{COLLECTION_NAME}/dummy_issue_id"
    )

    with pytest.raises(NotFound) as error:
        await IssueRepository().update(issue_id='dummy_issue_id', items={'responsible_engineer': 'email@updated.com'})
    assert str(error.value) == expected_msg
