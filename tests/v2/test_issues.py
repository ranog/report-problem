from src.v2.model import Engineer, Issue, Status, User


def test_should_assign_the_issue_to_a_collaborator():
    user = User(
        id='dummy_user_id',
        name='Dummy User',
        email='dummy_user_email',
        phone_number='dummy_user_phone',
    )
    issue = Issue(
        user=user,
        description='dummy_description',
        priority='dummy_priority',
        created_at='dummy_created_at',
        status='dummy_status',
        responsible_collaborator='',
    )
    engineer = Engineer(
        id='dummy_id',
        name='dummy_name',
        email='dummy_email',
    )

    issue.assign(engineer)

    assert issue.responsible_collaborator == engineer.email


def test_should_create_issue_with_status_to_do():
    user = User(
        id='dummy_user_id',
        name='Dummy User',
        email='dummy_user_email',
        phone_number='dummy_user_phone',
    )
    issue = Issue(
        user=user,
        description='dummy_description',
        priority='dummy_priority',
        created_at='dummy_created_at',
        responsible_collaborator='',
    )

    assert issue.status == Status.TO_DO


def test_should_change_problem_status():
    user = User(
        id='dummy_user_id',
        name='Dummy User',
        email='dummy_user_email',
        phone_number='dummy_user_phone',
    )
    issue = Issue(
        user=user,
        description='dummy_description',
        priority='dummy_priority',
        created_at='dummy_created_at',
        responsible_collaborator='',
    )

    issue.change_status(Status.IN_PROGRESS)

    assert issue.status == Status.IN_PROGRESS
