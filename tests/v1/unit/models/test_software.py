from src.v1.models.base_payload import Priority
from src.v1.models.software import Software


def test_it_should_return_high_priority_when_not_properly_installed(software_payload):
    software_payload['it_is_not_installed_correctly'] = True
    software_problem = Software(**software_payload)
    assert software_problem.priority == Priority.HIGH


def test_it_should_return_high_priority_when_run_with_errors(software_payload):
    software_payload['run_with_errors'] = True
    software_problem = Software(**software_payload)
    assert software_problem.priority == Priority.HIGH


def test_it_should_return_high_priority_when_not_responding_to_commands_and_interactions(software_payload):
    software_payload['does_not_respond_to_commands_and_interactions'] = True
    software_problem = Software(**software_payload)
    assert software_problem.priority == Priority.HIGH


def test_it_should_return_medium_priority_when_not_displaying_data_and_contents_correctly(software_payload):
    software_payload['not_displaying_data_and_content_correctly'] = True
    software_problem = Software(**software_payload)
    assert software_problem.priority == Priority.MEDIUM


def test_it_should_return_medium_priority_when_generating_unexpected_results(software_payload):
    software_payload['generates_unexpected_results'] = True
    software_problem = Software(**software_payload)
    assert software_problem.priority == Priority.MEDIUM


def test_it_should_return_medium_priority_when_not_integrating_with_other_systems_or_devices(software_payload):
    software_payload['not_integrating_with_other_systems_or_devices'] = True
    software_problem = Software(**software_payload)
    assert software_problem.priority == Priority.MEDIUM


def test_it_should_return_low_priority_when_not_using_required_system_resources(software_payload):
    software_payload['not_using_required_system_resources'] = True
    software_problem = Software(**software_payload)
    assert software_problem.priority == Priority.LOW


def test_it_should_return_low_priority_when_not_maintaining_security_and_not_protecting_data(software_payload):
    software_payload['not_maintaining_security_and_not_protecting_data'] = True
    software_problem = Software(**software_payload)
    assert software_problem.priority == Priority.LOW


def test_it_should_return_low_priority_when_not_updated_with_latest_versions(software_payload):
    software_payload['it_is_not_updated_with_the_latest_versions'] = True
    software_problem = Software(**software_payload)
    assert software_problem.priority == Priority.LOW


def test_it_should_return_low_priority_when_other_users_have_the_same_problem(software_payload):
    software_payload['other_users_are_having_the_same_problem'] = True
    software_problem = Software(**software_payload)
    assert software_problem.priority == Priority.LOW
