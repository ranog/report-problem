from src.model import Priority
from src.service import check_peripheral


def test_it_should_return_high_priority_when_not_connecting(peripheral_check):
    peripheral_check.does_not_connect = True
    priority = check_peripheral(peripheral_check)
    assert priority == Priority.HIGH


def test_it_should_return_high_priority_when_the_operating_system_is_not_recognizing(peripheral_check):
    peripheral_check.operating_system_is_not_recognizing = True
    priority = check_peripheral(peripheral_check)
    assert priority == Priority.HIGH


def test_it_should_return_high_priority_when_not_working_without_displaying_errors_or_failure_messages(
    peripheral_check,
):
    peripheral_check.does_not_work_without_displaying_errors_or_failure_messages = True
    priority = check_peripheral(peripheral_check)
    assert priority == Priority.HIGH


def test_it_should_return_medium_priority_when_not_responding_to_commands(peripheral_check):
    peripheral_check.does_not_respond_to_commands = True
    priority = check_peripheral(peripheral_check)
    assert priority == Priority.MEDIUM


def test_it_should_return_high_priority_when_not_performing_its_main_functions(peripheral_check):
    peripheral_check.does_not_perform_its_main_functions = True
    priority = check_peripheral(peripheral_check)
    assert priority == Priority.MEDIUM


def test_it_should_return_medium_priority_when_not_integrating_with_other_devices_or_components(peripheral_check):
    peripheral_check.does_not_integrate_with_other_devices_or_components = True
    priority = check_peripheral(peripheral_check)
    assert priority == Priority.MEDIUM


def test_it_should_return_low_priority_when_not_receiving_power_or_not_powered_on(peripheral_check):
    peripheral_check.does_not_receive_power_or_is_not_turned_on = True
    priority = check_peripheral(peripheral_check)
    assert priority == Priority.LOW


def test_it_should_return_low_priority_when_not_up_to_date_with_latest_drivers_or_firmware_versions(peripheral_check):
    peripheral_check.is_not_up_to_date_with_the_latest_versions_of_drivers_or_firmware = True
    priority = check_peripheral(peripheral_check)
    assert priority == Priority.LOW


def test_it_should_return_low_priority_when_other_users_are_using_the_same_peripheral_and_are_having_the_same_problem(
    peripheral_check,
):
    peripheral_check.other_users_are_using_the_same_peripheral_and_are_having_the_same_problem = True
    priority = check_peripheral(peripheral_check)
    assert priority == Priority.LOW


def test_it_should_return_low_priority_when_not_maintaining_data_security_and_protection(peripheral_check):
    peripheral_check.does_not_maintain_data_security_and_protection = True
    priority = check_peripheral(peripheral_check)
    assert priority == Priority.LOW
