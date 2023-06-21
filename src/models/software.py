from pydantic import root_validator

from src.models.base_payload import BasePayload, Category, Priority


class Software(BasePayload):
    software_name: str
    category: Category = Category.SOFTWARE
    it_is_not_installed_correctly: bool
    run_with_errors: bool
    does_not_respond_to_commands_and_interactions: bool
    not_displaying_data_and_content_correctly: bool
    generates_unexpected_results: bool
    not_integrating_with_other_systems_or_devices: bool
    not_using_required_system_resources: bool
    not_maintaining_security_and_not_protecting_data: bool
    it_is_not_updated_with_the_latest_versions: bool
    other_users_are_having_the_same_problem: bool

    @root_validator
    def _validate_form(cls, values):
        form_has_been_completed = [
            values.get('it_is_not_installed_correctly'),
            values.get('run_with_errors'),
            values.get('does_not_respond_to_commands_and_interactions'),
            values.get('not_displaying_data_and_content_correctly'),
            values.get('generates_unexpected_results'),
            values.get('not_integrating_with_other_systems_or_devices'),
            values.get('not_using_required_system_resources'),
            values.get('not_maintaining_security_and_not_protecting_data'),
            values.get('it_is_not_updated_with_the_latest_versions'),
            values.get('other_users_are_having_the_same_problem'),
        ]
        if any(form_has_been_completed):
            return values
        raise ValueError('Form has not been filled out')

    def select_priority(self):
        priorities = {
            Priority.HIGH: [
                self.it_is_not_installed_correctly,
                self.run_with_errors,
                self.does_not_respond_to_commands_and_interactions,
            ],
            Priority.MEDIUM: [
                self.not_displaying_data_and_content_correctly,
                self.generates_unexpected_results,
                self.not_integrating_with_other_systems_or_devices,
            ],
            Priority.LOW: [
                self.not_using_required_system_resources,
                self.not_maintaining_security_and_not_protecting_data,
                self.it_is_not_updated_with_the_latest_versions,
                self.other_users_are_having_the_same_problem,
            ],
        }
        for key, value in priorities.items():
            if any(value):
                self.priority = key
                break
