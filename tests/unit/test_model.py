from datetime import datetime

import pytest

from src.model import CreateNewIssue, DefectCategory, Priority, Status
from tests.conftest import TIMESTAMP_FORMAT


@pytest.mark.parametrize('category_value', ['', 'dummy category'])
def test_category_field_must_not_accept_values_that_are_not_listed_in_the_defect_category(category_value):
    with pytest.raises(ValueError) as error:
        CreateNewIssue(
            category=category_value,
            created_by='1',
            email='user@email.com',
            description='dummy description',
            priority=Priority.HIGH,
            created_at=datetime.utcnow().strftime(TIMESTAMP_FORMAT),
            status=Status.TO_DO,
            owner='specific@engineer.com',
        )
    expected_msg = '1 validation error for CreateNewIssue\ncategory\n  value is not a valid enumeration member;'
    assert expected_msg in str(error.value)


@pytest.mark.parametrize('priority_value', ['', 'dummy priority'])
def test_priority_field_must_not_accept_values_that_are_not_listed_in_the_priority(priority_value):
    with pytest.raises(ValueError) as error:
        CreateNewIssue(
            category=DefectCategory.SOFTWARE,
            created_by='1',
            email='user@email.com',
            description='dummy description',
            priority=priority_value,
            created_at=datetime.utcnow().strftime(TIMESTAMP_FORMAT),
            status=Status.TO_DO,
            owner='specific@engineer.com',
        )
    expected_msg = '1 validation error for CreateNewIssue\npriority\n  value is not a valid enumeration member;'
    assert expected_msg in str(error.value)


@pytest.mark.parametrize('status_value', ['', 'dummy status'])
def test_status_field_must_not_accept_values_that_are_not_listed_in_the_status(status_value):
    with pytest.raises(ValueError) as error:
        CreateNewIssue(
            category=DefectCategory.PERIPHERAL,
            created_by='1',
            email='user@email.com',
            description='dummy description',
            priority=Priority.MEDIUM,
            created_at=datetime.utcnow().strftime(TIMESTAMP_FORMAT),
            status=status_value,
            owner='specific@engineer.com',
        )
    expected_msg = '1 validation error for CreateNewIssue\nstatus\n  value is not a valid enumeration member;'
    assert expected_msg in str(error.value)


def test_email_field_should_have_a_valid_form():
    command = CreateNewIssue(
        category=DefectCategory.NOTEBOOK,
        created_by='1',
        email='dummy@email.c',
        description='dummy description',
        priority=Priority.HIGH,
        created_at=datetime.utcnow().strftime(TIMESTAMP_FORMAT),
        status=Status.TO_DO,
        owner='specific@engineer.com',
    )
    assert command.email == 'dummy@email.c'


@pytest.mark.parametrize('email_value', ['', 'dummy email'])
def test_email_field_must_have_an_email_in_valid_format(email_value):
    with pytest.raises(ValueError) as error:
        CreateNewIssue(
            category=DefectCategory.PERIPHERAL,
            created_by='1',
            email=email_value,
            description='dummy description',
            priority=Priority.MEDIUM,
            created_at=datetime.utcnow().strftime(TIMESTAMP_FORMAT),
            status=Status.IN_PROGRESS,
            owner='specific@engineer.com',
        )
    assert len(error.value.errors()) == 1
    assert 'value is not a valid email address' in str(error.value)


def test_owner_field_should_be_a_valid_form_of_email():
    command = CreateNewIssue(
        category=DefectCategory.NOTEBOOK,
        created_by='1',
        email='dummy@email.c',
        description='dummy description',
        priority=Priority.HIGH,
        created_at=datetime.utcnow().strftime(TIMESTAMP_FORMAT),
        status=Status.TO_DO,
        owner='owner@email.com',
    )
    assert command.owner == 'owner@email.com'


@pytest.mark.parametrize('owner_email_value', ['', 'dummy owner email'])
def test_test_owner_field_must_have_an_email_in_valid_format(owner_email_value):
    with pytest.raises(ValueError) as error:
        CreateNewIssue(
            category=DefectCategory.PERIPHERAL,
            created_by='1',
            email='dummy@email.c',
            description='dummy description',
            priority=Priority.MEDIUM,
            created_at=datetime.utcnow().strftime(TIMESTAMP_FORMAT),
            status=Status.IN_PROGRESS,
            owner=owner_email_value,
        )
    assert len(error.value.errors()) == 1
    assert 'value is not a valid email address' in str(error.value)
