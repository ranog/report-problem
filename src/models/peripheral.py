from pydantic import root_validator

from src.models.base_payload import BasePayload, Category, Priority


class Peripheral(BasePayload):
    peripheral_type: str
    category: Category = Category.PERIPHERAL
    does_not_connect: bool
    operating_system_is_not_recognizing: bool
    does_not_work_without_displaying_errors_or_failure_messages: bool
    does_not_respond_to_commands: bool
    does_not_perform_its_main_functions: bool
    does_not_integrate_with_other_devices_or_components: bool
    does_not_receive_power_or_is_not_turned_on: bool
    is_not_up_to_date_with_the_latest_versions_of_drivers_or_firmware: bool
    other_users_are_using_the_same_peripheral_and_are_having_the_same_problem: bool
    does_not_maintain_data_security_and_protection: bool

    @root_validator
    def _validate_form(cls, values):
        form_has_been_completed = [
            values.get('does_not_connect'),
            values.get('operating_system_is_not_recognizing'),
            values.get('does_not_work_without_displaying_errors_or_failure_messages'),
            values.get('does_not_respond_to_commands'),
            values.get('does_not_perform_its_main_functions'),
            values.get('does_not_integrate_with_other_devices_or_components'),
            values.get('does_not_receive_power_or_is_not_turned_on'),
            values.get('is_not_up_to_date_with_the_latest_versions_of_drivers_or_firmware'),
            values.get('other_users_are_using_the_same_peripheral_and_are_having_the_same_problem'),
            values.get('does_not_maintain_data_security_and_protection'),
        ]
        if any(form_has_been_completed):
            return values
        raise ValueError('Form has not been filled out')

    def select_priority(self):
        priorities = {
            Priority.HIGH: [
                self.does_not_connect,
                self.operating_system_is_not_recognizing,
                self.does_not_work_without_displaying_errors_or_failure_messages,
            ],
            Priority.MEDIUM: [
                self.does_not_respond_to_commands,
                self.does_not_perform_its_main_functions,
                self.does_not_integrate_with_other_devices_or_components,
            ],
            Priority.LOW: [
                self.does_not_receive_power_or_is_not_turned_on,
                self.is_not_up_to_date_with_the_latest_versions_of_drivers_or_firmware,
                self.other_users_are_using_the_same_peripheral_and_are_having_the_same_problem,
                self.does_not_maintain_data_security_and_protection,
            ],
        }
        for key, value in priorities.items():
            if any(value):
                self.priority = key
                break
