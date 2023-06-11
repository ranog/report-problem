from src.model import NotebookCheck, Priority


def check_notebook(notebook_check: NotebookCheck):
    if (
        notebook_check.it_is_not_turning_on
        or notebook_check.power_button_is_not_working
        or notebook_check.screen_is_not_working
    ):
        return Priority.HIGH

    if (
        notebook_check.keyboard_is_not_working
        or notebook_check.touchpad_is_not_working
        or notebook_check.not_connecting_to_the_internet
    ):
        return Priority.MEDIUM

    if (
        notebook_check.displays_error_message
        or notebook_check.does_not_recognize_peripherals
        or notebook_check.operating_system_does_not_start_correctly
    ):
        return Priority.LOW
