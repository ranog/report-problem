import os

import pytest
from google.api_core.exceptions import NotFound

from src.repository import COLLECTION_NAME, IssueRepository
from src.v1.models.base_payload import Category, Priority, Status
from src.v1.models.notebook import Notebook
from src.v1.models.peripheral import Peripheral
from src.v1.models.software import Software


async def test_it_should_persist_in_the_repository(clean_collection, notebook_payload):
    await clean_collection(COLLECTION_NAME)
    notebook_payload['it_is_not_turning_on'] = True
    new_issue = Notebook(**notebook_payload)
    issue_repository = IssueRepository()
    issue_id = await issue_repository.add(new_issue)
    response = await issue_repository.get(issue_id)
    new_issue_doc = new_issue.dict()
    new_issue_doc['created_at'] = str(new_issue_doc['created_at'])
    assert response == new_issue_doc


async def test_it_should_add_two_new_issues_but_ids_should_be_different(clean_collection, notebook_payload):
    await clean_collection(COLLECTION_NAME)
    notebook_payload['it_is_not_turning_on'] = True
    new_issue = Notebook(**notebook_payload)
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


async def test_it_should_return_list_of_issues_when_given_correct_parameters(clean_collection):
    await clean_collection(COLLECTION_NAME)
    payload_1 = {
        'username': 'dummy name',
        'user_id': '99999999999999',
        'user_email': 'user@email.com',
        'contact_phone': 'AA 9NNNN-NNNN',
        'description': 'dummy description',
        'software_name': 'Dummy Software',
        'it_is_not_installed_correctly': True,
        'run_with_errors': False,
        'does_not_respond_to_commands_and_interactions': False,
        'not_displaying_data_and_content_correctly': False,
        'generates_unexpected_results': False,
        'not_integrating_with_other_systems_or_devices': False,
        'not_using_required_system_resources': False,
        'not_maintaining_security_and_not_protecting_data': False,
        'it_is_not_updated_with_the_latest_versions': False,
        'other_users_are_having_the_same_problem': False,
    }
    payload_2 = {
        'username': 'dummy name',
        'user_id': '111111111',
        'user_email': 'user@email.com',
        'contact_phone': 'AA 9NNNN-NNNN',
        'description': 'dummy description',
        'software_name': 'Dummy Software',
        'it_is_not_installed_correctly': False,
        'run_with_errors': False,
        'does_not_respond_to_commands_and_interactions': False,
        'not_displaying_data_and_content_correctly': True,
        'generates_unexpected_results': False,
        'not_integrating_with_other_systems_or_devices': False,
        'not_using_required_system_resources': False,
        'not_maintaining_security_and_not_protecting_data': False,
        'it_is_not_updated_with_the_latest_versions': False,
        'other_users_are_having_the_same_problem': False,
    }
    payload_3 = {
        'username': 'dummy name',
        'user_id': '55',
        'user_email': 'user@email.com',
        'contact_phone': 'AA 9NNNN-NNNN',
        'description': 'dummy description',
        'software_name': 'Dummy Software',
        'it_is_not_installed_correctly': False,
        'run_with_errors': False,
        'does_not_respond_to_commands_and_interactions': False,
        'not_displaying_data_and_content_correctly': False,
        'generates_unexpected_results': True,
        'not_integrating_with_other_systems_or_devices': False,
        'not_using_required_system_resources': False,
        'not_maintaining_security_and_not_protecting_data': False,
        'it_is_not_updated_with_the_latest_versions': False,
        'other_users_are_having_the_same_problem': False,
    }
    software_problem_1 = Software(**payload_1)
    software_problem_2 = Software(**payload_2)
    software_problem_3 = Software(**payload_3)

    repository = IssueRepository()
    await repository.add(software_problem_1)
    await repository.add(software_problem_2)
    await repository.add(software_problem_3)

    software_problem_2.created_at = str(software_problem_2.created_at)
    software_problem_3.created_at = str(software_problem_3.created_at)

    issues = await repository.list(category=Category.SOFTWARE.value, priority=Priority.MEDIUM.value)

    assert len(issues) == 2
    assert issues == [software_problem_2.dict(), software_problem_3.dict()]


@pytest.mark.parametrize(
    'category_value, priority_value',
    [
        ('', Priority.MEDIUM.value),
        ('dummy value for category', Priority.MEDIUM.value),
        (Category.NOTEBOOK.value, ''),
        (Category.NOTEBOOK.value, 'dummy value for priority'),
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


async def test_it_should_return_items_from_the_given_category(clean_collection):
    await clean_collection(COLLECTION_NAME)
    payload_1 = {
        'username': 'dummy name',
        'user_id': '111111111',
        'user_email': 'user@email.com',
        'contact_phone': 'AA 9NNNN-NNNN',
        'description': 'dummy description',
        'it_is_not_turning_on': True,
        'power_button_is_not_working': False,
        'screen_is_not_working': False,
        'keyboard_is_not_working': False,
        'touchpad_is_not_working': False,
        'not_connecting_to_the_internet': False,
        'displays_error_message': False,
        'does_not_recognize_peripherals': False,
        'operating_system_does_not_start_correctly': False,
    }
    payload_2 = {
        'username': 'dummy name',
        'user_id': '111111111',
        'user_email': 'user@email.com',
        'contact_phone': 'AA 9NNNN-NNNN',
        'description': 'dummy description',
        'software_name': 'Dummy Software',
        'it_is_not_installed_correctly': False,
        'run_with_errors': False,
        'does_not_respond_to_commands_and_interactions': False,
        'not_displaying_data_and_content_correctly': True,
        'generates_unexpected_results': False,
        'not_integrating_with_other_systems_or_devices': False,
        'not_using_required_system_resources': False,
        'not_maintaining_security_and_not_protecting_data': False,
        'it_is_not_updated_with_the_latest_versions': False,
        'other_users_are_having_the_same_problem': False,
    }
    payload_3 = {
        'username': 'dummy name',
        'user_id': '55',
        'user_email': 'user@email.com',
        'contact_phone': 'AA 9NNNN-NNNN',
        'description': 'dummy description',
        'software_name': 'Dummy Software',
        'it_is_not_installed_correctly': False,
        'run_with_errors': False,
        'does_not_respond_to_commands_and_interactions': False,
        'not_displaying_data_and_content_correctly': False,
        'generates_unexpected_results': True,
        'not_integrating_with_other_systems_or_devices': False,
        'not_using_required_system_resources': False,
        'not_maintaining_security_and_not_protecting_data': False,
        'it_is_not_updated_with_the_latest_versions': False,
        'other_users_are_having_the_same_problem': False,
    }
    notebook_problem_1 = Notebook(**payload_1)
    software_problem_2 = Software(**payload_2)
    software_problem_3 = Software(**payload_3)

    repository = IssueRepository()
    await repository.add(notebook_problem_1)
    await repository.add(software_problem_2)
    await repository.add(software_problem_3)

    software_problem_2.created_at = str(software_problem_2.created_at)
    software_problem_3.created_at = str(software_problem_3.created_at)

    issues = await repository.list(category=Category.SOFTWARE.value)

    assert len(issues) == 2
    assert issues == [software_problem_2, software_problem_3]


async def test_it_should_return_items_of_given_priority(clean_collection):
    await clean_collection(COLLECTION_NAME)
    payload_1 = {
        'username': 'dummy name',
        'user_id': '111111111',
        'user_email': 'user@email.com',
        'contact_phone': 'AA 9NNNN-NNNN',
        'description': 'dummy description',
        'it_is_not_turning_on': True,
        'power_button_is_not_working': False,
        'screen_is_not_working': False,
        'keyboard_is_not_working': False,
        'touchpad_is_not_working': False,
        'not_connecting_to_the_internet': False,
        'displays_error_message': False,
        'does_not_recognize_peripherals': False,
        'operating_system_does_not_start_correctly': False,
    }
    payload_2 = {
        'username': 'dummy name',
        'user_id': '111111111',
        'user_email': 'user@email.com',
        'contact_phone': 'AA 9NNNN-NNNN',
        'description': 'dummy description',
        'software_name': 'Dummy Software',
        'it_is_not_installed_correctly': False,
        'run_with_errors': False,
        'does_not_respond_to_commands_and_interactions': False,
        'not_displaying_data_and_content_correctly': False,
        'generates_unexpected_results': False,
        'not_integrating_with_other_systems_or_devices': False,
        'not_using_required_system_resources': False,
        'not_maintaining_security_and_not_protecting_data': False,
        'it_is_not_updated_with_the_latest_versions': False,
        'other_users_are_having_the_same_problem': True,
    }
    payload_3 = {
        'username': 'dummy name',
        'user_id': '111111111',
        'user_email': 'user@email.com',
        'contact_phone': 'AA 9NNNN-NNNN',
        'description': 'dummy description',
        'peripheral_type': 'Dummy Peripheral',
        'does_not_connect': True,
        'operating_system_is_not_recognizing': False,
        'does_not_work_without_displaying_errors_or_failure_messages': False,
        'does_not_respond_to_commands': False,
        'does_not_perform_its_main_functions': False,
        'does_not_integrate_with_other_devices_or_components': False,
        'does_not_receive_power_or_is_not_turned_on': False,
        'is_not_up_to_date_with_the_latest_versions_of_drivers_or_firmware': False,
        'other_users_are_using_the_same_peripheral_and_are_having_the_same_problem': False,
        'does_not_maintain_data_security_and_protection': False,
    }
    notebook_problem_1 = Notebook(**payload_1)
    software_problem_2 = Software(**payload_2)
    peripheral_problem_3 = Peripheral(**payload_3)

    repository = IssueRepository()
    await repository.add(notebook_problem_1)
    await repository.add(software_problem_2)
    await repository.add(peripheral_problem_3)

    notebook_problem_1.created_at = str(notebook_problem_1.created_at)
    peripheral_problem_3.created_at = str(peripheral_problem_3.created_at)
    issues = await repository.list(priority=Priority.HIGH.value)

    assert len(issues) == 2
    assert issues == [notebook_problem_1, peripheral_problem_3]


async def test_it_should_update_all_fields_provided(notebook_payload, clean_collection):
    await clean_collection(COLLECTION_NAME)
    notebook_payload['it_is_not_turning_on'] = True
    new_issue = Notebook(**notebook_payload)
    repository = IssueRepository()
    issue_id = await repository.add(new_issue)
    item_to_update = {
        'responsible_engineer': 'email@updated.com',
        'status': Status.IN_PROGRESS,
        'priority': Priority.LOW,
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
