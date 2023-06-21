from src.model import Peripheral, Priority


def test_it_should_return_high_priority_when_not_connecting(peripheral_payload):
    peripheral_payload['does_not_connect'] = True
    peripheral_problem = Peripheral(**peripheral_payload)
    peripheral_problem.select_priority()
    assert peripheral_problem.priority == Priority.HIGH


def test_it_should_return_high_priority_when_the_operating_system_is_not_recognizing(peripheral_payload):
    peripheral_payload['operating_system_is_not_recognizing'] = True
    peripheral_problem = Peripheral(**peripheral_payload)
    peripheral_problem.select_priority()
    assert peripheral_problem.priority == Priority.HIGH


def test_it_should_return_high_priority_when_not_working_without_displaying_errors_or_failure_messages(
    peripheral_payload,
):
    peripheral_payload['does_not_work_without_displaying_errors_or_failure_messages'] = True
    peripheral_problem = Peripheral(**peripheral_payload)
    peripheral_problem.select_priority()
    assert peripheral_problem.priority == Priority.HIGH


def test_it_should_return_medium_priority_when_not_responding_to_commands(peripheral_payload):
    peripheral_payload['does_not_respond_to_commands'] = True
    peripheral_problem = Peripheral(**peripheral_payload)
    peripheral_problem.select_priority()
    assert peripheral_problem.priority == Priority.MEDIUM


def test_it_should_return_high_priority_when_not_performing_its_main_functions(peripheral_payload):
    peripheral_payload['does_not_perform_its_main_functions'] = True
    peripheral_problem = Peripheral(**peripheral_payload)
    peripheral_problem.select_priority()
    assert peripheral_problem.priority == Priority.MEDIUM


def test_it_should_return_medium_priority_when_not_integrating_with_other_devices_or_components(peripheral_payload):
    peripheral_payload['does_not_integrate_with_other_devices_or_components'] = True
    peripheral_problem = Peripheral(**peripheral_payload)
    peripheral_problem.select_priority()
    assert peripheral_problem.priority == Priority.MEDIUM


def test_it_should_return_low_priority_when_not_receiving_power_or_not_powered_on(peripheral_payload):
    peripheral_payload['does_not_receive_power_or_is_not_turned_on'] = True
    peripheral_problem = Peripheral(**peripheral_payload)
    peripheral_problem.select_priority()
    assert peripheral_problem.priority == Priority.LOW


def test_it_should_return_low_priority_when_not_up_to_date_with_latest_drivers_or_firmware_versions(peripheral_payload):
    peripheral_payload['is_not_up_to_date_with_the_latest_versions_of_drivers_or_firmware'] = True
    peripheral_problem = Peripheral(**peripheral_payload)
    peripheral_problem.select_priority()
    assert peripheral_problem.priority == Priority.LOW


def test_it_should_return_low_priority_when_other_users_are_using_the_same_peripheral_and_are_having_the_same_problem(
    peripheral_payload,
):
    peripheral_payload['other_users_are_using_the_same_peripheral_and_are_having_the_same_problem'] = True
    peripheral_problem = Peripheral(**peripheral_payload)
    peripheral_problem.select_priority()
    assert peripheral_problem.priority == Priority.LOW


def test_it_should_return_low_priority_when_not_maintaining_data_security_and_protection(peripheral_payload):
    peripheral_payload['does_not_maintain_data_security_and_protection'] = True
    peripheral_problem = Peripheral(**peripheral_payload)
    peripheral_problem.select_priority()
    assert peripheral_problem.priority == Priority.LOW
