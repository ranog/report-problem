from src.repository import COLLECTION_NAME, IssueRepository


async def test_it_should_persist_in_the_repository(clean_collection, new_issue):
    await clean_collection(COLLECTION_NAME)
    issue_repository = IssueRepository()
    issue_id = await issue_repository.add(new_issue)
    response = await issue_repository.get(issue_id)
    new_issue_doc = new_issue.dict()
    new_issue_doc['category'] = new_issue_doc['category'].value
    new_issue_doc['priority'] = new_issue_doc['priority'].value
    new_issue_doc['status'] = new_issue_doc['status'].value
    assert response == new_issue_doc


async def test_it_should_add_two_new_issues_but_ids_should_be_different(clean_collection, new_issue):
    await clean_collection(COLLECTION_NAME)
    issue_repository = IssueRepository()
    await issue_repository.add(new_issue)
    await issue_repository.add(new_issue)
    issues = await issue_repository.collection.where(
        field_path='user_id',
        op_string='==',
        value=new_issue.user_id,
    ).get()
    assert len(issues) == 2
    assert issues[0].id != issues[1].id


async def test_it_should_return_an_empty_dict_when_the_issue_id_does_not_exist_in_the_repository(clean_collection):
    await clean_collection(COLLECTION_NAME)
    issue = await IssueRepository().get('dummy_issue_id')
    assert issue == {}
