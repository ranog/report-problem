from src.model import Priority, SoftwareCheck
from src.service import check_software


def test_it_should_return_high_priority_when_not_properly_installed():
    priority = check_software(SoftwareCheck(name='Dummy Software', it_is_not_installed_correctly=True))
    assert priority == Priority.HIGH


def test_it_should_return_high_priority_when_run_with_errors():
    priority = check_software(SoftwareCheck(name='Dummy Software', run_with_errors=True))
    assert priority == Priority.HIGH


def test_it_should_return_high_priority_when_not_responding_to_commands_and_interactions():
    priority = check_software(SoftwareCheck(name='Dummy Software', does_not_respond_to_commands_and_interactions=True))
    assert priority == Priority.HIGH


def test_it_should_return_medium_priority_when_not_displaying_data_and_contents_correctly():
    priority = check_software(SoftwareCheck(name='Dummy Software', not_displaying_data_and_content_correctly=True))
    assert priority == Priority.MEDIUM


def test_it_should_return_medium_priority_when_generating_unexpected_results():
    priority = check_software(SoftwareCheck(name='Dummy Software', generates_unexpected_results=True))
    assert priority == Priority.MEDIUM


def test_it_should_return_medium_priority_when_not_integrating_with_other_systems_or_devices():
    priority = check_software(SoftwareCheck(name='Dummy Software', not_integrating_with_other_systems_or_devices=True))
    assert priority == Priority.MEDIUM


def test_it_should_return_low_priority_when_not_using_required_system_resources():
    priority = check_software(SoftwareCheck(name='Dummy Software', not_using_required_system_resources=True))
    assert priority == Priority.LOW


def test_it_should_return_low_priority_when_not_maintaining_security_and_not_protecting_data():
    priority = check_software(
        SoftwareCheck(name='Dummy Software', not_maintaining_security_and_not_protecting_data=True)
    )
    assert priority == Priority.LOW


def test_it_should_return_low_priority_when_not_updated_with_latest_versions():
    priority = check_software(SoftwareCheck(name='Dummy Software', it_is_not_updated_with_the_latest_versions=True))
    assert priority == Priority.LOW


def test_it_should_return_low_priority_when_other_users_have_the_same_problem():
    priority = check_software(SoftwareCheck(name='Dummy Software', other_users_are_having_the_same_problem=True))
    assert priority == Priority.LOW
