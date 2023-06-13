from src.model import Priority
from src.service import select_priority


def test_it_should_return_high_priority_when_not_properly_installed(software_check):
    software_check['it_is_not_installed_correctly'] = True
    priority = select_priority(software_check)
    assert priority == Priority.HIGH


def test_it_should_return_high_priority_when_run_with_errors(software_check):
    software_check['run_with_errors'] = True
    priority = select_priority(software_check)
    assert priority == Priority.HIGH


def test_it_should_return_high_priority_when_not_responding_to_commands_and_interactions(software_check):
    software_check['does_not_respond_to_commands_and_interactions'] = True
    priority = select_priority(software_check)
    assert priority == Priority.HIGH


def test_it_should_return_medium_priority_when_not_displaying_data_and_contents_correctly(software_check):
    software_check['not_displaying_data_and_content_correctly'] = True
    priority = select_priority(software_check)
    assert priority == Priority.MEDIUM


def test_it_should_return_medium_priority_when_generating_unexpected_results(software_check):
    software_check['generates_unexpected_results'] = True
    priority = select_priority(software_check)
    assert priority == Priority.MEDIUM


def test_it_should_return_medium_priority_when_not_integrating_with_other_systems_or_devices(software_check):
    software_check['not_integrating_with_other_systems_or_devices'] = True
    priority = select_priority(software_check)
    assert priority == Priority.MEDIUM


def test_it_should_return_low_priority_when_not_using_required_system_resources(software_check):
    software_check['not_using_required_system_resources'] = True
    priority = select_priority(software_check)
    assert priority == Priority.LOW


def test_it_should_return_low_priority_when_not_maintaining_security_and_not_protecting_data(software_check):
    software_check['not_maintaining_security_and_not_protecting_data'] = True
    priority = select_priority(software_check)
    assert priority == Priority.LOW


def test_it_should_return_low_priority_when_not_updated_with_latest_versions(software_check):
    software_check['it_is_not_updated_with_the_latest_versions'] = True
    priority = select_priority(software_check)
    assert priority == Priority.LOW


def test_it_should_return_low_priority_when_other_users_have_the_same_problem(software_check):
    software_check['other_users_are_having_the_same_problem'] = True
    priority = select_priority(software_check)
    assert priority == Priority.LOW
