import pytest
from pydantic import ValidationError

from src.model import Notebook, Peripheral, Software


def test_it_should_raise_exception_when_data_to_report_problem_with_notebook_is_incomplete():
    with pytest.raises(ValidationError) as error:
        Notebook(
            username='dummy name',
            user_id='1',
            user_email='user@email.com',
            contact_phone='AA 9NNNN-NNNN',
            description='dummy description',
        )
    expected_msg = (
        '9 validation errors for Notebook\n'
        'it_is_not_turning_on\n'
        '  field required (type=value_error.missing)\n'
        'power_button_is_not_working\n'
        '  field required (type=value_error.missing)\n'
        'screen_is_not_working\n'
        '  field required (type=value_error.missing)\n'
        'keyboard_is_not_working\n'
        '  field required (type=value_error.missing)\n'
        'touchpad_is_not_working\n'
        '  field required (type=value_error.missing)\n'
        'not_connecting_to_the_internet\n'
        '  field required (type=value_error.missing)\n'
        'displays_error_message\n'
        '  field required (type=value_error.missing)\n'
        'does_not_recognize_peripherals\n'
        '  field required (type=value_error.missing)\n'
        'operating_system_does_not_start_correctly\n'
        '  field required (type=value_error.missing)'
    )
    assert str(error.value) == expected_msg


def test_it_should_raise_exception_when_data_to_report_problem_with_software_is_incomplete():
    with pytest.raises(ValueError) as error:
        Software(
            username='dummy name',
            user_id='1',
            user_email='user@email.com',
            contact_phone='AA 9NNNN-NNNN',
            description='dummy description',
        )
    expected_msg = (
        '11 validation errors for Software\n'
        'software_name\n'
        '  field required (type=value_error.missing)\n'
        'it_is_not_installed_correctly\n'
        '  field required (type=value_error.missing)\n'
        'run_with_errors\n'
        '  field required (type=value_error.missing)\n'
        'does_not_respond_to_commands_and_interactions\n'
        '  field required (type=value_error.missing)\n'
        'not_displaying_data_and_content_correctly\n'
        '  field required (type=value_error.missing)\n'
        'generates_unexpected_results\n'
        '  field required (type=value_error.missing)\n'
        'not_integrating_with_other_systems_or_devices\n'
        '  field required (type=value_error.missing)\n'
        'not_using_required_system_resources\n'
        '  field required (type=value_error.missing)\n'
        'not_maintaining_security_and_not_protecting_data\n'
        '  field required (type=value_error.missing)\n'
        'it_is_not_updated_with_the_latest_versions\n'
        '  field required (type=value_error.missing)\n'
        'other_users_are_having_the_same_problem\n'
        '  field required (type=value_error.missing)'
    )
    assert str(error.value) == expected_msg


def test_it_should_raise_exception_when_data_to_report_problem_with_peripheral_is_incomplete():
    with pytest.raises(ValueError) as error:
        Peripheral(
            username='dummy name',
            user_id='1',
            user_email='user@email.com',
            contact_phone='AA 9NNNN-NNNN',
            description='dummy description',
        )
    expected_msg = (
        '11 validation errors for Peripheral\n'
        'peripheral_type\n'
        '  field required (type=value_error.missing)\n'
        'does_not_connect\n'
        '  field required (type=value_error.missing)\n'
        'operating_system_is_not_recognizing\n'
        '  field required (type=value_error.missing)\n'
        'does_not_work_without_displaying_errors_or_failure_messages\n'
        '  field required (type=value_error.missing)\n'
        'does_not_respond_to_commands\n'
        '  field required (type=value_error.missing)\n'
        'does_not_perform_its_main_functions\n'
        '  field required (type=value_error.missing)\n'
        'does_not_integrate_with_other_devices_or_components\n'
        '  field required (type=value_error.missing)\n'
        'does_not_receive_power_or_is_not_turned_on\n'
        '  field required (type=value_error.missing)\n'
        'is_not_up_to_date_with_the_latest_versions_of_drivers_or_firmware\n'
        '  field required (type=value_error.missing)\n'
        'other_users_are_using_the_same_peripheral_and_are_having_the_same_problem\n'
        '  field required (type=value_error.missing)\n'
        'does_not_maintain_data_security_and_protection\n'
        '  field required (type=value_error.missing)'
    )
    assert str(error.value) == expected_msg


def test_email_field_should_have_a_valid_form(notebook_payload):
    issue = Notebook(**notebook_payload)
    assert issue.user_email == 'user@email.com'


@pytest.mark.parametrize('email_value', ['', 'dummy email'])
def test_email_field_must_have_an_email_in_valid_format(email_value, notebook_payload):
    notebook_payload['user_email'] = email_value
    with pytest.raises(ValueError) as error:
        Notebook(**notebook_payload)
    expected_msg = (
        '1 validation error for Notebook\n'
        'user_email\n'
        '  value is not a valid email address (type=value_error.email)'
    )
    assert len(error.value.errors()) == 1
    assert str(error.value) == expected_msg


def test_owner_field_should_be_created_none(notebook_payload):
    issue = Notebook(**notebook_payload)
    assert issue.responsible_engineer is None
