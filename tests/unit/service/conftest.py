import pytest

from src.model import NotebookCheck, PeripheralCheck, SoftwareCheck


@pytest.fixture
def notebook_check():
    return NotebookCheck(
        it_is_not_turning_on=False,
        power_button_is_not_working=False,
        screen_is_not_working=False,
        keyboard_is_not_working=False,
        touchpad_is_not_working=False,
        not_connecting_to_the_internet=False,
        displays_error_message=False,
        does_not_recognize_peripherals=False,
        operating_system_does_not_start_correctly=False,
    )


@pytest.fixture
def software_check():
    return SoftwareCheck(
        name='Dummy Software',
        it_is_not_installed_correctly=False,
        run_with_errors=False,
        does_not_respond_to_commands_and_interactions=False,
        not_displaying_data_and_content_correctly=False,
        generates_unexpected_results=False,
        not_integrating_with_other_systems_or_devices=False,
        not_using_required_system_resources=False,
        not_maintaining_security_and_not_protecting_data=False,
        it_is_not_updated_with_the_latest_versions=False,
        other_users_are_having_the_same_problem=False,
    )


@pytest.fixture
def peripheral_check():
    return PeripheralCheck(
        peripheral_type='Dummy Peripheral',
        does_not_connect=False,
        operating_system_is_not_recognizing=False,
        does_not_work_without_displaying_errors_or_failure_messages=False,
        does_not_respond_to_commands=False,
        does_not_perform_its_main_functions=False,
        does_not_integrate_with_other_devices_or_components=False,
        does_not_receive_power_or_is_not_turned_on=False,
        is_not_up_to_date_with_the_latest_versions_of_drivers_or_firmware=False,
        other_users_are_using_the_same_peripheral_and_are_having_the_same_problem=False,
        does_not_maintain_data_security_and_protection=False,
    )
