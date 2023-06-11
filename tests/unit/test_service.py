from src.model import NotebookCheck, Priority
from src.service import check_notebook


def test_it_should_return_high_priority_when_notebook_will_not_turn_on():
    priority = check_notebook(NotebookCheck(does_not_turn_on=True))
    assert priority == Priority.HIGH


def test_it_should_return_high_priority_when_power_button_does_not_work():
    priority = check_notebook(NotebookCheck(power_button_not_working=True))
    assert priority == Priority.HIGH


def test_it_should_return_high_priority_when_screen_is_not_working():
    priority = check_notebook(NotebookCheck(screen_not_working=True))
    assert priority == Priority.HIGH
