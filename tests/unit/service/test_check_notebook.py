from src.model import Priority
from src.service import check_notebook


def test_it_should_return_high_priority_when_notebook_will_not_turn_on(notebook_check):
    notebook_check.it_is_not_turning_on = True
    priority = check_notebook(notebook_check)
    assert priority == Priority.HIGH


def test_it_should_return_high_priority_when_power_button_is_not_working(notebook_check):
    notebook_check.power_button_is_not_working = True
    priority = check_notebook(notebook_check)
    assert priority == Priority.HIGH


def test_it_should_return_high_priority_when_screen_is_not_working(notebook_check):
    notebook_check.screen_is_not_working = True
    priority = check_notebook(notebook_check)
    assert priority == Priority.HIGH


def test_it_should_return_medium_priority_when_keyboard_is_not_working(notebook_check):
    notebook_check.keyboard_is_not_working = True
    priority = check_notebook(notebook_check)
    assert priority == Priority.MEDIUM


def test_it_should_return_medium_priority_when_touchpad_is_not_working(notebook_check):
    notebook_check.touchpad_is_not_working = True
    priority = check_notebook(notebook_check)
    assert priority == Priority.MEDIUM


def test_it_should_return_medium_priority_when_not_connecting_to_the_internet(notebook_check):
    notebook_check.not_connecting_to_the_internet = True
    priority = check_notebook(notebook_check)
    assert priority == Priority.MEDIUM


def test_it_should_return_low_priority_when_displaying_error_message(notebook_check):
    notebook_check.displays_error_message = True
    priority = check_notebook(notebook_check)
    assert priority == Priority.LOW


def test_it_should_return_low_priority_when_not_recognizing_peripherals(notebook_check):
    notebook_check.does_not_recognize_peripherals = True
    priority = check_notebook(notebook_check)
    assert priority == Priority.LOW


def test_it_should_return_low_priority_when_operating_system_fails_to_start_properly(notebook_check):
    notebook_check.operating_system_does_not_start_correctly = True
    priority = check_notebook(notebook_check)
    assert priority == Priority.LOW
