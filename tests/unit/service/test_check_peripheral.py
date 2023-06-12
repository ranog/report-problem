from src.model import PeripheralCheck, Priority
from src.service import check_peripheral


def test_it_should_return_high_priority_when_not_connecting():
    priority = check_peripheral(PeripheralCheck(peripheral_type='Dummy Peripheral', does_not_connect=True))
    assert priority == Priority.HIGH


def test_it_should_return_high_priority_when_the_operating_system_is_not_recognizing():
    priority = check_peripheral(
        PeripheralCheck(peripheral_type='Dummy Peripheral', operating_system_is_not_recognizing=True)
    )
    assert priority == Priority.HIGH


def test_it_should_return_high_priority_when_not_working_without_displaying_errors_or_failure_messages():
    priority = check_peripheral(
        PeripheralCheck(
            peripheral_type='Dummy Peripheral',
            does_not_work_without_displaying_errors_or_failure_messages=True,
        )
    )
    assert priority == Priority.HIGH


def test_it_should_return_medium_priority_when_not_responding_to_commands():
    priority = check_peripheral(PeripheralCheck(peripheral_type='Dummy Peripheral', does_not_respond_to_commands=True))
    assert priority == Priority.MEDIUM


def test_it_should_return_high_priority_when_not_performing_its_main_functions():
    priority = check_peripheral(
        PeripheralCheck(peripheral_type='Dummy Peripheral', does_not_perform_its_main_functions=True)
    )
    assert priority == Priority.MEDIUM


def test_it_should_return_medium_priority_when_not_integrating_with_other_devices_or_components():
    priority = check_peripheral(
        PeripheralCheck(peripheral_type='Dummy Peripheral', does_not_integrate_with_other_devices_or_components=True)
    )
    assert priority == Priority.MEDIUM


def test_it_should_return_low_priority_when_not_receiving_power_or_not_powered_on():
    priority = check_peripheral(
        PeripheralCheck(peripheral_type='Dummy Peripheral', does_not_receive_power_or_is_not_turned_on=True)
    )
    assert priority == Priority.LOW


def test_it_should_return_low_priority_when_not_up_to_date_with_latest_drivers_or_firmware_versions():
    priority = check_peripheral(
        PeripheralCheck(
            peripheral_type='Dummy Peripheral',
            is_not_up_to_date_with_the_latest_versions_of_drivers_or_firmware=True,
        )
    )
    assert priority == Priority.LOW


def test_it_should_return_low_priority_when_other_users_are_using_the_same_peripheral_and_are_having_the_same_problem():
    priority = check_peripheral(
        PeripheralCheck(
            peripheral_type='Dummy Peripheral',
            other_users_are_using_the_same_peripheral_and_are_having_the_same_problem=True,
        )
    )
    assert priority == Priority.LOW


def test_it_should_return_low_priority_when_not_maintaining_data_security_and_protection():
    priority = check_peripheral(
        PeripheralCheck(peripheral_type='Dummy Peripheral', does_not_maintain_data_security_and_protection=True)
    )
    assert priority == Priority.LOW
