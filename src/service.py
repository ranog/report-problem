from src.model import NotebookCheck, Priority


def check_notebook(notebook_check: NotebookCheck) -> Priority:
    high_priority = [
        notebook_check.it_is_not_turning_on,
        notebook_check.power_button_is_not_working,
        notebook_check.screen_is_not_working,
    ]
    medium_priority = [
        notebook_check.keyboard_is_not_working,
        notebook_check.touchpad_is_not_working,
        notebook_check.not_connecting_to_the_internet,
    ]
    low_priority = [
        notebook_check.displays_error_message,
        notebook_check.does_not_recognize_peripherals,
        notebook_check.operating_system_does_not_start_correctly,
    ]

    if any(high_priority):
        return Priority.HIGH
    if any(medium_priority):
        return Priority.MEDIUM
    if any(low_priority):
        return Priority.LOW
