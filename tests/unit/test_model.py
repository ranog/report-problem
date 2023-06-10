from datetime import datetime, timezone

import pytest

from src.model import Defect, NewIssue, Priority, Status


@pytest.mark.parametrize('category_value', ['', 'dummy category'])
def test_category_field_must_not_accept_values_that_are_not_listed_in_the_defect_category(category_value):
    with pytest.raises(ValueError) as error:
        NewIssue(
            username='dummy name',
            category=category_value,
            user_id='1',
            user_email='user@email.com',
            contact_phone='AA 9NNNN-NNNN',
            description='dummy description',
            priority=Priority.HIGH.value,
            created_at=str(datetime.now(timezone.utc)),
            status=Status.TO_DO.value,
            responsible_engineer='specific@engineer.com',
        )
    expected_msg = '1 validation error for NewIssue\ncategory\n  value is not a valid enumeration member;'
    assert expected_msg in str(error.value)


@pytest.mark.parametrize('priority_value', ['', 'dummy priority'])
def test_priority_field_must_not_accept_values_that_are_not_listed_in_the_priority(priority_value):
    with pytest.raises(ValueError) as error:
        NewIssue(
            username='dummy name',
            category=Defect.SOFTWARE.value,
            user_id='1',
            user_email='user@email.com',
            contact_phone='AA 9NNNN-NNNN',
            description='dummy description',
            priority=priority_value,
            created_at=str(datetime.now(timezone.utc)),
            status=Status.TO_DO.value,
            responsible_engineer='specific@engineer.com',
        )
    expected_msg = '1 validation error for NewIssue\npriority\n  value is not a valid enumeration member;'
    assert expected_msg in str(error.value)


@pytest.mark.parametrize('status_value', ['', 'dummy status'])
def test_status_field_must_not_accept_values_that_are_not_listed_in_the_status(status_value):
    with pytest.raises(ValueError) as error:
        NewIssue(
            username='dummy name',
            category=Defect.PERIPHERAL.value,
            user_id='1',
            user_email='user@email.com',
            contact_phone='AA 9NNNN-NNNN',
            description='dummy description',
            priority=Priority.MEDIUM.value,
            created_at=str(datetime.now(timezone.utc)),
            status=status_value,
            responsible_engineer='specific@engineer.com',
        )
    expected_msg = '1 validation error for NewIssue\nstatus\n  value is not a valid enumeration member;'
    assert expected_msg in str(error.value)


def test_email_field_should_have_a_valid_form():
    issue = NewIssue(
        username='dummy name',
        category=Defect.NOTEBOOK.value,
        user_id='1',
        user_email='dummy@email.c',
        contact_phone='AA 9NNNN-NNNN',
        description='dummy description',
        priority=Priority.HIGH.value,
        created_at=str(datetime.now(timezone.utc)),
        status=Status.TO_DO.value,
        responsible_engineer='specific@engineer.com',
    )
    assert issue.user_email == 'dummy@email.c'


@pytest.mark.parametrize('email_value', ['', 'dummy email'])
def test_email_field_must_have_an_email_in_valid_format(email_value):
    with pytest.raises(ValueError) as error:
        NewIssue(
            username='dummy name',
            category=Defect.PERIPHERAL.value,
            user_id='1',
            user_email=email_value,
            contact_phone='AA 9NNNN-NNNN',
            description='dummy description',
            priority=Priority.MEDIUM.value,
            created_at=str(datetime.now(timezone.utc)),
            status=Status.IN_PROGRESS.value,
            responsible_engineer='specific@engineer.com',
        )
    assert len(error.value.errors()) == 1
    assert 'value is not a valid email address' in str(error.value)


def test_owner_field_should_be_a_valid_form_of_email():
    issue = NewIssue(
        username='dummy name',
        category=Defect.NOTEBOOK.value,
        user_id='1',
        user_email='dummy@email.c',
        contact_phone='AA 9NNNN-NNNN',
        description='dummy description',
        priority=Priority.HIGH.value,
        created_at=str(datetime.now(timezone.utc)),
        status=Status.TO_DO.value,
        responsible_engineer='owner@email.com',
    )
    assert issue.responsible_engineer == 'owner@email.com'


@pytest.mark.parametrize('responsible_engineer_value', ['', 'dummy owner email'])
def test_test_owner_field_must_have_an_email_in_valid_format(responsible_engineer_value):
    with pytest.raises(ValueError) as error:
        NewIssue(
            username='dummy name',
            category=Defect.PERIPHERAL.value,
            contact_phone='AA 9NNNN-NNNN',
            user_id='1',
            user_email='dummy@email.c',
            description='dummy description',
            priority=Priority.MEDIUM.value,
            created_at=str(datetime.now(timezone.utc)),
            status=Status.IN_PROGRESS.value,
            responsible_engineer=responsible_engineer_value,
        )
    assert len(error.value.errors()) == 1
    assert 'value is not a valid email address' in str(error.value)


def test_owner_field_should_be_created_empty_when_not_provided():
    issue = NewIssue(
        username='dummy name',
        category=Defect.NOTEBOOK.value,
        user_id='1',
        user_email='dummy@email.c',
        contact_phone='AA 9NNNN-NNNN',
        description='dummy description',
        priority=Priority.HIGH.value,
        created_at=str(datetime.now(timezone.utc)),
        status=Status.TO_DO.value,
    )
    assert issue.responsible_engineer == ''
