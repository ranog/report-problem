from pydantic import root_validator

from src.models.base_payload import BasePayload, Category, Priority


class Notebook(BasePayload):
    category: Category = Category.NOTEBOOK
    it_is_not_turning_on: bool
    power_button_is_not_working: bool
    screen_is_not_working: bool
    keyboard_is_not_working: bool
    touchpad_is_not_working: bool
    not_connecting_to_the_internet: bool
    displays_error_message: bool
    does_not_recognize_peripherals: bool
    operating_system_does_not_start_correctly: bool

    @root_validator
    def _validate_form(cls, values):
        form_has_been_completed = [
            values.get('it_is_not_turning_on'),
            values.get('power_button_is_not_working'),
            values.get('screen_is_not_working'),
            values.get('keyboard_is_not_working'),
            values.get('touchpad_is_not_working'),
            values.get('not_connecting_to_the_internet'),
            values.get('displays_error_message'),
            values.get('does_not_recognize_peripherals'),
            values.get('operating_system_does_not_start_correctly'),
        ]
        if any(form_has_been_completed):
            return values
        raise ValueError('Form has not been filled out')

    def select_priority(self):
        priorities = {
            Priority.HIGH: [
                self.it_is_not_turning_on,
                self.power_button_is_not_working,
                self.screen_is_not_working,
            ],
            Priority.MEDIUM: [
                self.keyboard_is_not_working,
                self.touchpad_is_not_working,
                self.not_connecting_to_the_internet,
            ],
            Priority.LOW: [
                self.displays_error_message,
                self.does_not_recognize_peripherals,
                self.operating_system_does_not_start_correctly,
            ],
        }
        for key, value in priorities.items():
            if any(value):
                self.priority = key
                break
