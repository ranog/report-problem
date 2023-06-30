import pytest
from httpx import AsyncClient

from src.models.base_payload import Category, Priority, Status
from src.repository import COLLECTION_NAME


async def test_it_should_ping_successfully(async_http_client: AsyncClient):
    response = await async_http_client.get('/v1/ping/')

    assert response.status_code == 200
    assert response.json() == {'ping': 'pong'}


async def test_it_should_successfully_create_a_new_notebook_problem(
    notebook_payload, clean_collection, async_http_client: AsyncClient
):
    await clean_collection(COLLECTION_NAME)
    notebook_payload['it_is_not_turning_on'] = True

    response = await async_http_client.post('/v1/report-notebook-issue/', json=notebook_payload)

    assert response.status_code == 200


async def test_it_should_successfully_create_a_new_software_problem(
    software_payload, clean_collection, async_http_client: AsyncClient
):
    await clean_collection(COLLECTION_NAME)
    software_payload['it_is_not_installed_correctly'] = True

    response = await async_http_client.post('/v1/report-software-issue/', json=software_payload)

    assert response.status_code == 200


async def test_it_should_successfully_create_a_new_peripheral_problem(
    peripheral_payload, clean_collection, async_http_client: AsyncClient
):
    await clean_collection(COLLECTION_NAME)
    peripheral_payload['does_not_connect'] = True

    response = await async_http_client.post('/v1/report-peripheral-issue/', json=peripheral_payload)

    assert response.status_code == 200


async def test_it_should_return_status_code_400_when_the_new_notebook_problem_is_empty(
    notebook_error_message,
    clean_collection,
    async_http_client: AsyncClient,
):
    await clean_collection(COLLECTION_NAME)

    response = await async_http_client.post('/v1/report-notebook-issue/', json={})

    assert response.status_code == 400
    assert response.json() == notebook_error_message


async def test_it_should_return_status_code_400_when_the_new_software_problem_is_empty(
    software_error_message,
    clean_collection,
    async_http_client: AsyncClient,
):
    await clean_collection(COLLECTION_NAME)

    response = await async_http_client.post('/v1/report-software-issue/', json={})

    assert response.status_code == 400
    assert response.json() == software_error_message


async def test_it_should_return_status_code_400_when_the_new_peripheral_problem_is_empty(
    peripheral_error_message,
    clean_collection,
    async_http_client: AsyncClient,
):
    await clean_collection(COLLECTION_NAME)

    response = await async_http_client.post('/v1/report-peripheral-issue/', json={})

    assert response.status_code == 400
    assert response.json() == peripheral_error_message


async def test_it_should_successfully_get_issue(notebook_payload, clean_collection, async_http_client: AsyncClient):
    await clean_collection(COLLECTION_NAME)
    notebook_payload['it_is_not_turning_on'] = True
    issue_info = await async_http_client.post('/v1/report-notebook-issue/', json=notebook_payload)

    response = await async_http_client.get(f'/v1/issue/{issue_info.json()}/')

    assert response.status_code == 200
    assert response.json()['username'] == notebook_payload['username']
    assert response.json()['user_id'] == notebook_payload['user_id']
    assert response.json()['user_email'] == notebook_payload['user_email']
    assert response.json()['contact_phone'] == notebook_payload['contact_phone']
    assert response.json()['description'] == notebook_payload['description']


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


async def test_it_should_successfully_issue_list(
    notebook_payload, software_payload, clean_collection, async_http_client: AsyncClient
):
    await clean_collection(COLLECTION_NAME)
    notebook_payload['it_is_not_turning_on'] = True
    other_software_payload = software_payload
    other_software_payload['not_displaying_data_and_content_correctly'] = True
    software_payload['generates_unexpected_results'] = True

    await async_http_client.post('/v1/report-notebook-issue/', json=notebook_payload)
    await async_http_client.post('/v1/report-software-issue/', json=software_payload)
    await async_http_client.post('/v1/report-software-issue/', json=other_software_payload)

    response = await async_http_client.get(
        f'/v1/issues/?category={Category.SOFTWARE.value}&priority={Priority.MEDIUM.value}'
    )

    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]['generates_unexpected_results'] is True
    assert response.json()[1]['not_displaying_data_and_content_correctly'] is True


@pytest.mark.parametrize(
    'category_value, priority_value',
    [
        (Category.NOTEBOOK.value, 'dummy_priority'),
        ('dummy_category', Priority.MEDIUM.value),
        ('dummy_category', 'dummy_priority'),
        (Category.NOTEBOOK.value, ''),
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


async def test_it_should_return_the_calls_of_the_category_provided_in_the_query_parameters(
    notebook_payload,
    software_payload,
    clean_collection,
    async_http_client: AsyncClient,
):
    await clean_collection(COLLECTION_NAME)
    other_software_payload = software_payload
    software_payload['it_is_not_installed_correctly'] = True
    other_software_payload['other_users_are_having_the_same_problem'] = True
    notebook_payload['power_button_is_not_working'] = True
    await async_http_client.post('/v1/report-notebook-issue/', json=notebook_payload)
    await async_http_client.post('/v1/report-software-issue/', json=software_payload)
    await async_http_client.post('/v1/report-software-issue/', json=other_software_payload)

    response = await async_http_client.get(f'/v1/issues/?category={Category.SOFTWARE.value}')

    assert response.status_code == 200
    assert len(response.json()) == 2


async def test_it_should_return_the_calls_of_the_priority_provided_in_the_query_parameters(
    notebook_payload,
    software_payload,
    peripheral_payload,
    clean_collection,
    async_http_client: AsyncClient,
):
    await clean_collection(COLLECTION_NAME)
    notebook_payload['it_is_not_turning_on'] = True
    software_payload['it_is_not_installed_correctly'] = True
    peripheral_payload['does_not_connect'] = True
    await async_http_client.post('/v1/report-notebook-issue/', json=notebook_payload)
    await async_http_client.post('/v1/report-software-issue/', json=software_payload)
    await async_http_client.post('/v1/report-peripheral-issue/', json=peripheral_payload)

    response = await async_http_client.get(f'/v1/issues/?priority={Priority.HIGH.value}')

    assert response.status_code == 200
    assert len(response.json()) == 3


async def test_it_should_return_all_alerts_when_no_query_parameter_is_passed(
    notebook_payload,
    software_payload,
    peripheral_payload,
    clean_collection,
    async_http_client: AsyncClient,
):
    await clean_collection(COLLECTION_NAME)
    notebook_payload['it_is_not_turning_on'] = True
    software_payload['not_integrating_with_other_systems_or_devices'] = True
    peripheral_payload['does_not_maintain_data_security_and_protection'] = True
    await async_http_client.post('/v1/report-notebook-issue/', json=notebook_payload)
    await async_http_client.post('/v1/report-software-issue/', json=software_payload)
    await async_http_client.post('/v1/report-peripheral-issue/', json=peripheral_payload)

    response = await async_http_client.get('/v1/issues/')

    assert response.status_code == 200
    assert len(response.json()) == 3


async def test_it_should_successfully_update_the_fields_provided_in_items(
    notebook_payload,
    clean_collection,
    async_http_client: AsyncClient,
):
    await clean_collection(COLLECTION_NAME)
    notebook_payload['it_is_not_turning_on'] = True
    issue_post_response = await async_http_client.post('/v1/report-notebook-issue/', json=notebook_payload)
    issue_id = issue_post_response.json()
    items = {
        'responsible_engineer': 'email@updated.com',
        'status': Status.IN_PROGRESS,
        'priority': Priority.LOW,
    }

    response = await async_http_client.patch(f'/v1/issue/{issue_id}/', json=items)
    issue_get_response = await async_http_client.get(f'/v1/issue/{issue_id}/')
    issue = issue_get_response.json()

    assert response.status_code == 200
    assert issue['responsible_engineer'] == items['responsible_engineer']
    assert issue['status'] == items['status']
    assert issue['priority'] == items['priority']


async def test_it_should_return_not_found_when_issue_id_is_not_valid(
    clean_collection,
    async_http_client: AsyncClient,
):
    await clean_collection(COLLECTION_NAME)
    items = {
        'responsible_engineer': 'email@updated.com',
        'status': Status.IN_PROGRESS,
        'priority': Priority.LOW,
    }

    response = await async_http_client.patch('/v1/issue/dummy_id/', json=items)

    assert response.status_code == 404
    assert response.json() == 'dummy_id not found.'


async def test_it_should_return_bad_resquest_when_issue_id_is_not_valid(
    notebook_payload,
    clean_collection,
    async_http_client: AsyncClient,
):
    await clean_collection(COLLECTION_NAME)
    notebook_payload['it_is_not_turning_on'] = True
    issue_doc = await async_http_client.post('/v1/report-notebook-issue/', json=notebook_payload)
    issue_id = issue_doc.json()
    items = {
        'responsible_engineer': 'email@updated.com',
        'status': Status.IN_PROGRESS.value,
        'dummy_field': 'dummy_value',
    }

    response = await async_http_client.patch(f'/v1/issue/{issue_id}/', json=items)

    assert response.status_code == 400
    assert response.json() == 'dummy_field field not exist.'


async def test_it_should_return_bad_request_when_no_question_is_answered_for_the_notebook_issue(
    notebook_payload,
    clean_collection,
    async_http_client: AsyncClient,
):
    await clean_collection(COLLECTION_NAME)
    response = await async_http_client.post('/v1/report-notebook-issue/', json=notebook_payload)

    assert response.status_code == 400


async def test_it_should_return_bad_request_when_no_question_is_answered_for_the_software_issue(
    software_payload,
    clean_collection,
    async_http_client: AsyncClient,
):
    await clean_collection(COLLECTION_NAME)
    response = await async_http_client.post('/v1/report-software-issue/', json=software_payload)

    assert response.status_code == 400


async def test_it_should_return_bad_request_when_no_question_is_answered_for_the_peripheral_issue(
    peripheral_payload,
    clean_collection,
    async_http_client: AsyncClient,
):
    await clean_collection(COLLECTION_NAME)
    response = await async_http_client.post('/v1/report-peripheral-issue/', json=peripheral_payload)

    assert response.status_code == 400


async def test_it_should_return_the_necessary_parameters_to_open_the_ticket_for_notebook_problems(
    clean_collection,
    async_http_client: AsyncClient,
):
    await clean_collection(COLLECTION_NAME)
    expected_result = {
        'username': 'string',
        'user_id': 'string',
        'user_email': 'string',
        'contact_phone': 'string',
        'description': 'string',
        'it_is_not_turning_on': 'boolean',
        'power_button_is_not_working': 'boolean',
        'screen_is_not_working': 'boolean',
        'keyboard_is_not_working': 'boolean',
        'touchpad_is_not_working': 'boolean',
        'not_connecting_to_the_internet': 'boolean',
        'displays_error_message': 'boolean',
        'does_not_recognize_peripherals': 'boolean',
        'operating_system_does_not_start_correctly': 'boolean',
    }

    response = await async_http_client.get('/v1/payloads/notebook/')

    assert response.status_code == 200
    assert response.json() == expected_result


async def test_it_should_return_the_necessary_parameters_to_open_the_ticket_for_software_problems(
    clean_collection,
    async_http_client: AsyncClient,
):
    await clean_collection(COLLECTION_NAME)
    expected_result = {
        'username': 'string',
        'user_id': 'string',
        'user_email': 'string',
        'contact_phone': 'string',
        'description': 'string',
        'software_name': 'string',
        'it_is_not_installed_correctly': 'boolean',
        'run_with_errors': 'boolean',
        'does_not_respond_to_commands_and_interactions': 'boolean',
        'not_displaying_data_and_content_correctly': 'boolean',
        'generates_unexpected_results': 'boolean',
        'not_integrating_with_other_systems_or_devices': 'boolean',
        'not_using_required_system_resources': 'boolean',
        'not_maintaining_security_and_not_protecting_data': 'boolean',
        'it_is_not_updated_with_the_latest_versions': 'boolean',
        'other_users_are_having_the_same_problem': 'boolean',
    }

    response = await async_http_client.get('/v1/payloads/software/')

    assert response.status_code == 200
    assert response.json() == expected_result


async def test_it_should_return_the_necessary_parameters_to_open_the_ticket_for_peripheral_problems(
    clean_collection,
    async_http_client: AsyncClient,
):
    await clean_collection(COLLECTION_NAME)
    expected_result = {
        'username': 'string',
        'user_id': 'string',
        'user_email': 'string',
        'contact_phone': 'string',
        'description': 'string',
        'peripheral_type': 'string',
        'does_not_connect': 'boolean',
        'operating_system_is_not_recognizing': 'boolean',
        'does_not_work_without_displaying_errors_or_failure_messages': 'boolean',
        'does_not_respond_to_commands': 'boolean',
        'does_not_perform_its_main_functions': 'boolean',
        'does_not_integrate_with_other_devices_or_components': 'boolean',
        'does_not_receive_power_or_is_not_turned_on': 'boolean',
        'is_not_up_to_date_with_the_latest_versions_of_drivers_or_firmware': 'boolean',
        'other_users_are_using_the_same_peripheral_and_are_having_the_same_problem': 'boolean',
        'does_not_maintain_data_security_and_protection': 'boolean',
    }

    response = await async_http_client.get('/v1/payloads/peripheral/')

    assert response.status_code == 200
    assert response.json() == expected_result


async def test_it_should_return_not_found_when_category_is_not_valid(clean_collection, async_http_client: AsyncClient):
    await clean_collection(COLLECTION_NAME)
    category = 'dummy_category'
    expected_msg = (
        f'{category} not found. Categories with available payload: '
        f'{Category.NOTEBOOK.value}, {Category.SOFTWARE.value} and {Category.PERIPHERAL.value}'
    )

    response = await async_http_client.get(f'/v1/payloads/{category}/')

    assert response.status_code == 400
    assert response.json() == expected_msg
