from pydantic import BaseModel

from src.model import Category, Notebook, Peripheral, Priority, Software


def _check_notebook(notebook_check: Notebook) -> dict:
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

    return {'high': high, 'medium': medium, 'low': low}


def _check_software(software_check: Software) -> dict:
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

    return {'high': high, 'medium': medium, 'low': low}


def _check_peripheral(peripheral_check: Peripheral):
    high = [
        peripheral_check.does_not_connect,
        peripheral_check.operating_system_is_not_recognizing,
        peripheral_check.does_not_work_without_displaying_errors_or_failure_messages,
    ]
    medium = [
        peripheral_check.does_not_respond_to_commands,
        peripheral_check.does_not_perform_its_main_functions,
        peripheral_check.does_not_integrate_with_other_devices_or_components,
    ]
    low = [
        peripheral_check.does_not_receive_power_or_is_not_turned_on,
        peripheral_check.is_not_up_to_date_with_the_latest_versions_of_drivers_or_firmware,
        peripheral_check.other_users_are_using_the_same_peripheral_and_are_having_the_same_problem,
        peripheral_check.does_not_maintain_data_security_and_protection,
    ]

    return {'high': high, 'medium': medium, 'low': low}


def select_priority(any_base_model: BaseModel) -> Priority:
    match any_base_model.category:
        case Category.NOTEBOOK.value:
            priorities = _check_notebook(any_base_model)
        case Category.SOFTWARE.value:
            priorities = _check_software(any_base_model)
        case Category.PERIPHERAL.value:
            priorities = _check_peripheral(any_base_model)

    if any(priorities.get('high', [])):
        return Priority.HIGH.value
    if any(priorities.get('medium', [])):
        return Priority.MEDIUM.value
    if any(priorities.get('low', [])):
        return Priority.LOW.value
    raise ValueError(any_base_model)
