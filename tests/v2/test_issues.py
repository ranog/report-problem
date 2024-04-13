from datetime import datetime

import pytest
from src.v2.model import Engineer, Priority, Status


def test_should_assign_the_issue_to_a_collaborator(issue):
    engineer = Engineer(
        id='dummy_id',
        name='dummy_name',
        email='dummy_email',
    )

    issue.assign(engineer)

    assert issue.responsible_collaborator == engineer


def test_should_create_issue_with_status_to_do(issue):
    assert issue.status == Status.TO_DO


def test_it_should_create_a_problem_with_the_field_created_at_datetime_type(issue):
    assert isinstance(issue.created_at, datetime)


@pytest.mark.parametrize(
    'status',
    [
        Status.TO_DO,
        Status.IN_PROGRESS,
        Status.DONE,
    ],
)
def test_should_change_problem_status(issue, status):
    issue.change_status(status)

    assert issue.status == status


@pytest.mark.parametrize(
    'priority',
    [
        Priority.LOW,
        Priority.MEDIUM,
        Priority.HIGH,
    ],
)
def test_should_change_problem_priority(issue, priority):
    issue.change_priority(priority)

    assert issue.priority == priority
