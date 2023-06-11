from src.model import NotebookCheck, Priority, SoftwareCheck


def _decide_priority(high: list[bool], medium: list[bool], low: list[bool]) -> Priority:
    if any(high):
        return Priority.HIGH
    if any(medium):
        return Priority.MEDIUM
    if any(low):
        return Priority.LOW


def check_notebook(notebook_check: NotebookCheck) -> Priority:
    high = [
        notebook_check.it_is_not_turning_on,
        notebook_check.power_button_is_not_working,
        notebook_check.screen_is_not_working,
    ]
    medium = [
        notebook_check.keyboard_is_not_working,
        notebook_check.touchpad_is_not_working,
        notebook_check.not_connecting_to_the_internet,
    ]
    low = [
        notebook_check.displays_error_message,
        notebook_check.does_not_recognize_peripherals,
        notebook_check.operating_system_does_not_start_correctly,
    ]

    return _decide_priority(high=high, medium=medium, low=low)


def check_software(software_check: SoftwareCheck) -> Priority:
    high = [
        software_check.it_is_not_installed_correctly,
        software_check.run_with_errors,
        software_check.does_not_respond_to_commands_and_interactions,
    ]
    medium = [
        software_check.not_displaying_data_and_content_correctly,
        software_check.generates_unexpected_results,
        software_check.not_integrating_with_other_systems_or_devices,
    ]
    low = [
        software_check.not_using_required_system_resources,
        software_check.not_maintaining_security_and_not_protecting_data,
        software_check.it_is_not_updated_with_the_latest_versions,
        software_check.other_users_are_having_the_same_problem,
    ]

    return _decide_priority(high=high, medium=medium, low=low)
