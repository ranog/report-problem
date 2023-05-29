from src.model import NewIssue


def build_new_issue(data: dict):
    return NewIssue.parse_obj(data)
