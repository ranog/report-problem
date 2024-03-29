import pytest
from google.cloud import firestore
from httpx import AsyncClient

from src.main import app


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
def notebook_payload():
    return {
        'username': 'dummy name',
        'user_id': '111111111',
        'user_email': 'user@email.com',
        'contact_phone': 'AA 9NNNN-NNNN',
        'description': 'dummy description',
        'it_is_not_turning_on': False,
        'power_button_is_not_working': False,
        'screen_is_not_working': False,
        'keyboard_is_not_working': False,
        'touchpad_is_not_working': False,
        'not_connecting_to_the_internet': False,
        'displays_error_message': False,
        'does_not_recognize_peripherals': False,
        'operating_system_does_not_start_correctly': False,
    }


@pytest.fixture
def software_payload():
    return {
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
        'other_users_are_having_the_same_problem': False,
    }


@pytest.fixture
def peripheral_payload():
    return {
        'username': 'dummy name',
        'user_id': '111111111',
        'user_email': 'user@email.com',
        'contact_phone': 'AA 9NNNN-NNNN',
        'description': 'dummy description',
        'peripheral_type': 'Dummy Peripheral',
        'does_not_connect': False,
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


@pytest.fixture
def notebook_error_message():
    return {
        'detail': 'Validation error',
        'errors': [
            {'loc': ['body', 'username'], 'msg': 'field required', 'type': 'value_error.missing'},
            {'loc': ['body', 'user_id'], 'msg': 'field required', 'type': 'value_error.missing'},
            {'loc': ['body', 'user_email'], 'msg': 'field required', 'type': 'value_error.missing'},
            {'loc': ['body', 'contact_phone'], 'msg': 'field required', 'type': 'value_error.missing'},
            {'loc': ['body', 'description'], 'msg': 'field required', 'type': 'value_error.missing'},
            {'loc': ['body', 'it_is_not_turning_on'], 'msg': 'field required', 'type': 'value_error.missing'},
            {'loc': ['body', 'power_button_is_not_working'], 'msg': 'field required', 'type': 'value_error.missing'},
            {'loc': ['body', 'screen_is_not_working'], 'msg': 'field required', 'type': 'value_error.missing'},
            {'loc': ['body', 'keyboard_is_not_working'], 'msg': 'field required', 'type': 'value_error.missing'},
            {'loc': ['body', 'touchpad_is_not_working'], 'msg': 'field required', 'type': 'value_error.missing'},
            {'loc': ['body', 'not_connecting_to_the_internet'], 'msg': 'field required', 'type': 'value_error.missing'},
            {'loc': ['body', 'displays_error_message'], 'msg': 'field required', 'type': 'value_error.missing'},
            {'loc': ['body', 'does_not_recognize_peripherals'], 'msg': 'field required', 'type': 'value_error.missing'},
            {
                'loc': ['body', 'operating_system_does_not_start_correctly'],
                'msg': 'field required',
                'type': 'value_error.missing',
            },
            {'loc': ['body', '__root__'], 'msg': 'Form has not been filled out', 'type': 'value_error'},
        ],
    }


@pytest.fixture
def software_error_message():
    return {
        'detail': 'Validation error',
        'errors': [
            {'loc': ['body', 'username'], 'msg': 'field required', 'type': 'value_error.missing'},
            {'loc': ['body', 'user_id'], 'msg': 'field required', 'type': 'value_error.missing'},
            {'loc': ['body', 'user_email'], 'msg': 'field required', 'type': 'value_error.missing'},
            {'loc': ['body', 'contact_phone'], 'msg': 'field required', 'type': 'value_error.missing'},
            {'loc': ['body', 'description'], 'msg': 'field required', 'type': 'value_error.missing'},
            {'loc': ['body', 'software_name'], 'msg': 'field required', 'type': 'value_error.missing'},
            {'loc': ['body', 'it_is_not_installed_correctly'], 'msg': 'field required', 'type': 'value_error.missing'},
            {'loc': ['body', 'run_with_errors'], 'msg': 'field required', 'type': 'value_error.missing'},
            {
                'loc': ['body', 'does_not_respond_to_commands_and_interactions'],
                'msg': 'field required',
                'type': 'value_error.missing',
            },
            {
                'loc': ['body', 'not_displaying_data_and_content_correctly'],
                'msg': 'field required',
                'type': 'value_error.missing',
            },
            {'loc': ['body', 'generates_unexpected_results'], 'msg': 'field required', 'type': 'value_error.missing'},
            {
                'loc': ['body', 'not_integrating_with_other_systems_or_devices'],
                'msg': 'field required',
                'type': 'value_error.missing',
            },
            {
                'loc': ['body', 'not_using_required_system_resources'],
                'msg': 'field required',
                'type': 'value_error.missing',
            },
            {
                'loc': ['body', 'not_maintaining_security_and_not_protecting_data'],
                'msg': 'field required',
                'type': 'value_error.missing',
            },
            {
                'loc': ['body', 'it_is_not_updated_with_the_latest_versions'],
                'msg': 'field required',
                'type': 'value_error.missing',
            },
            {
                'loc': ['body', 'other_users_are_having_the_same_problem'],
                'msg': 'field required',
                'type': 'value_error.missing',
            },
            {'loc': ['body', '__root__'], 'msg': 'Form has not been filled out', 'type': 'value_error'},
        ],
    }


@pytest.fixture
def peripheral_error_message():
    return {
        'detail': 'Validation error',
        'errors': [
            {'loc': ['body', 'username'], 'msg': 'field required', 'type': 'value_error.missing'},
            {'loc': ['body', 'user_id'], 'msg': 'field required', 'type': 'value_error.missing'},
            {'loc': ['body', 'user_email'], 'msg': 'field required', 'type': 'value_error.missing'},
            {'loc': ['body', 'contact_phone'], 'msg': 'field required', 'type': 'value_error.missing'},
            {'loc': ['body', 'description'], 'msg': 'field required', 'type': 'value_error.missing'},
            {'loc': ['body', 'peripheral_type'], 'msg': 'field required', 'type': 'value_error.missing'},
            {'loc': ['body', 'does_not_connect'], 'msg': 'field required', 'type': 'value_error.missing'},
            {
                'loc': ['body', 'operating_system_is_not_recognizing'],
                'msg': 'field required',
                'type': 'value_error.missing',
            },
            {
                'loc': ['body', 'does_not_work_without_displaying_errors_or_failure_messages'],
                'msg': 'field required',
                'type': 'value_error.missing',
            },
            {'loc': ['body', 'does_not_respond_to_commands'], 'msg': 'field required', 'type': 'value_error.missing'},
            {
                'loc': ['body', 'does_not_perform_its_main_functions'],
                'msg': 'field required',
                'type': 'value_error.missing',
            },
            {
                'loc': ['body', 'does_not_integrate_with_other_devices_or_components'],
                'msg': 'field required',
                'type': 'value_error.missing',
            },
            {
                'loc': ['body', 'does_not_receive_power_or_is_not_turned_on'],
                'msg': 'field required',
                'type': 'value_error.missing',
            },
            {
                'loc': ['body', 'is_not_up_to_date_with_the_latest_versions_of_drivers_or_firmware'],
                'msg': 'field required',
                'type': 'value_error.missing',
            },
            {
                'loc': ['body', 'other_users_are_using_the_same_peripheral_and_are_having_the_same_problem'],
                'msg': 'field required',
                'type': 'value_error.missing',
            },
            {
                'loc': ['body', 'does_not_maintain_data_security_and_protection'],
                'msg': 'field required',
                'type': 'value_error.missing',
            },
            {'loc': ['body', '__root__'], 'msg': 'Form has not been filled out', 'type': 'value_error'},
        ],
    }
