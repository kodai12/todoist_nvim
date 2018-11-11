from pytodoist import todoist

from rplugin.python3.anticorruption.user import TodoistUserTransfer
from rplugin.python3.anticorruption.project import TodoistProjectTransfer
from rplugin.python3.anticorruption.project import TodoistProjectListTransfer

from rplugin.python3.model.user import User
from rplugin.python3.model.project import Project


class PytodoistAPIDataSource:
    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.password = password

    def get_user(self) -> User:
        orig_user = todoist.login(self.email, self.password)
        transfer = TodoistUserTransfer(orig_user)
        return transfer.to_my_user()

    def get_project(self, project_name: str) -> Project:
        orig_user = todoist.login(self.email, self.password)
        orig_project = orig_user.get_project(project_name)
        transfer = TodoistProjectTransfer(orig_project)
        return transfer.to_my_project()

    def get_all_projects(self) -> list:
        orig_user = todoist.login(self.email, self.password)
        orig_projects = orig_user.get_projects()
        transfer = TodoistProjectListTransfer(orig_projects)
        return transfer.to_my_projects()
