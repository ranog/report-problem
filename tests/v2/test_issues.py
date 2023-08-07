from src.v2.model import Engineer, Issue, User


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
