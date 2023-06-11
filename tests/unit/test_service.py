from src.model import NotebookCheck, Priority
from src.service import check_notebook


def test_it_should_return_high_priority_when_notebook_will_not_turn_on():
    priority = check_notebook(NotebookCheck(it_is_not_turning_on=True))
    assert priority == Priority.HIGH


def test_it_should_return_high_priority_when_power_button_is_not_working():
    priority = check_notebook(NotebookCheck(power_button_is_not_working=True))
    assert priority == Priority.HIGH


def test_it_should_return_high_priority_when_screen_is_not_working():
    priority = check_notebook(NotebookCheck(screen_is_not_working=True))
    assert priority == Priority.HIGH


def test_it_should_return_medium_priority_when_keyboard_is_not_working():
    priority = check_notebook(NotebookCheck(keyboard_is_not_working=True))
    assert priority == Priority.MEDIUM


def test_it_should_return_medium_priority_when_touchpad_is_not_working():
    priority = check_notebook(NotebookCheck(touchpad_is_not_working=True))
    assert priority == Priority.MEDIUM


def test_it_should_return_medium_priority_when_not_connecting_to_the_internet():
    priority = check_notebook(NotebookCheck(not_connecting_to_the_internet=True))
    assert priority == Priority.MEDIUM
