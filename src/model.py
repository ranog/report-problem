from datetime import datetime, timezone
from enum import Enum

from pydantic import BaseModel, EmailStr, Field, root_validator


class Category(str, Enum):
    NOTEBOOK = 'notebook'
    SOFTWARE = 'software'
    PERIPHERAL = 'peripheral'


class Status(str, Enum):
    TO_DO = 'todo'
    IN_PROGRESS = 'in progress'
    DONE = 'done'


class Priority(str, Enum):
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'


class BasePayload(BaseModel):
    username: str
    user_id: str
    user_email: EmailStr
    contact_phone: str
    description: str
    priority: Priority = Priority.HIGH
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    status: Status = Status.TO_DO
    responsible_engineer: EmailStr = None


class Notebook(BasePayload):
    category: Category = Category.NOTEBOOK.value
    # high
    it_is_not_turning_on: bool
    power_button_is_not_working: bool
    screen_is_not_working: bool

    # medium
    keyboard_is_not_working: bool
    touchpad_is_not_working: bool
    not_connecting_to_the_internet: bool

    # low
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


class Software(BasePayload):
    software_name: str
    category: Category = Category.SOFTWARE.value

    # high
    it_is_not_installed_correctly: bool
    run_with_errors: bool
    does_not_respond_to_commands_and_interactions: bool

    # medium
    not_displaying_data_and_content_correctly: bool
    generates_unexpected_results: bool
    not_integrating_with_other_systems_or_devices: bool

    # low
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


class Peripheral(BasePayload):
    peripheral_type: str
    category: Category = Category.PERIPHERAL.value

    # high
    does_not_connect: bool
    operating_system_is_not_recognizing: bool
    does_not_work_without_displaying_errors_or_failure_messages: bool

    # medium
    does_not_respond_to_commands: bool
    does_not_perform_its_main_functions: bool
    does_not_integrate_with_other_devices_or_components: bool

    # low
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
