from src.model import NotebookCheck, Priority


def check_notebook(notebook: NotebookCheck):
    if notebook.does_not_turn_on or notebook.power_button_not_working or notebook.screen_not_working:
        return Priority.HIGH
