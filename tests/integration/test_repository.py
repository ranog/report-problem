from src.repository import COLLECTION_NAME, IssueRepository


async def test_it_should_persist_in_the_repository(clean_collection, issue):
    await clean_collection(COLLECTION_NAME)
    issue_repository = IssueRepository()
    issue_id = await issue_repository.add(issue)
    response = await issue_repository.get(issue_id)
    assert response == issue


async def test_it_should_add_two_new_issues_but_ids_should_be_different(clean_collection, issue):
    await clean_collection(COLLECTION_NAME)
    issue_repository = IssueRepository()
    await issue_repository.add(issue)
    await issue_repository.add(issue)
    issues = await issue_repository.collection.where(
        field_path='created_by',
        op_string='==',
        value=issue['created_by'],
    ).get()
    assert len(issues) == 2
    assert issues[0].id != issues[1].id


async def test_it_should_return_an_empty_dict_when_the_issue_id_does_not_exist_in_the_repository(clean_collection):
    await clean_collection(COLLECTION_NAME)
    issue = await IssueRepository().get('dummy_issue_id')
    assert issue == {}
