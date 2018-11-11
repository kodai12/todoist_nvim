from pytodoist import todoist

from rplugin.python3.anticorruption.todoist import TodoistUserTransfer


class PytodoistAPIDataSource:
    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.password = password

    def get_user(self) -> todoist.User:
        orig_user = todoist.login(self.email, self.password)
        transfer = TodoistUserTransfer(orig_user)
        return transfer.to_my_user()

    def get_project(self, project_name: str) -> todoist.Project:
        pass

    def get_projects(self):
        pass
