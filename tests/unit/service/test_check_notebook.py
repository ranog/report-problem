from src.models.base_payload import Priority
from src.models.notebook import Notebook


def test_it_should_return_high_priority_when_notebook_will_not_turn_on(notebook_payload):
    notebook_payload['it_is_not_turning_on'] = True
    notebook_problem = Notebook(**notebook_payload)
    assert notebook_problem.priority == Priority.HIGH


def test_it_should_return_high_priority_when_power_button_is_not_working(notebook_payload):
    notebook_payload['power_button_is_not_working'] = True
    notebook_problem = Notebook(**notebook_payload)
    assert notebook_problem.priority == Priority.HIGH


def test_it_should_return_high_priority_when_screen_is_not_working(notebook_payload):
    notebook_payload['screen_is_not_working'] = True
    notebook_problem = Notebook(**notebook_payload)
    assert notebook_problem.priority == Priority.HIGH


def test_it_should_return_medium_priority_when_keyboard_is_not_working(notebook_payload):
    notebook_payload['keyboard_is_not_working'] = True
    notebook_problem = Notebook(**notebook_payload)
    assert notebook_problem.priority == Priority.MEDIUM


def test_it_should_return_medium_priority_when_touchpad_is_not_working(notebook_payload):
    notebook_payload['touchpad_is_not_working'] = True
    notebook_problem = Notebook(**notebook_payload)
    assert notebook_problem.priority == Priority.MEDIUM


def test_it_should_return_medium_priority_when_not_connecting_to_the_internet(notebook_payload):
    notebook_payload['not_connecting_to_the_internet'] = True
    notebook_problem = Notebook(**notebook_payload)
    assert notebook_problem.priority == Priority.MEDIUM


def test_it_should_return_low_priority_when_displaying_error_message(notebook_payload):
    notebook_payload['displays_error_message'] = True
    notebook_problem = Notebook(**notebook_payload)
    assert notebook_problem.priority == Priority.LOW


def test_it_should_return_low_priority_when_not_recognizing_peripherals(notebook_payload):
    notebook_payload['does_not_recognize_peripherals'] = True
    notebook_problem = Notebook(**notebook_payload)
    assert notebook_problem.priority == Priority.LOW


def test_it_should_return_low_priority_when_operating_system_fails_to_start_properly(notebook_payload):
    notebook_payload['operating_system_does_not_start_correctly'] = True
    notebook_problem = Notebook(**notebook_payload)
    assert notebook_problem.priority == Priority.LOW
