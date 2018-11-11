from rplugin.python3.dataaccess.pytodoist import PytodoistAPIDataSource
from rplugin.python3.model.user import User
from rplugin.python3.model.project import Project

from rplugin.python3.anticorruption.user import TodoistUserTransfer
from rplugin.python3.anticorruption.project import TodoistProjectTransfer
from rplugin.python3.anticorruption.project import TodoistProjectListTransfer
from rplugin.python3.anticorruption.task import TodoistTaskListTransfer


class TodoistQueryService:
    def __init__(self, datasource: PytodoistAPIDataSource):
        self.datasource = datasource

    def get_user(self) -> User:
        orig_user = self.datasource.get_user()
        transfer = TodoistUserTransfer(orig_user)
        return transfer.to_my_user()

    def get_project(self, project_name: str) -> Project:
        orig_project = self.datasource.get_project(project_name)
        transfer = TodoistProjectTransfer(orig_project)
        return transfer.to_my_project()

    def get_all_projects(self) -> list:
        orig_projects = self.datasource.get_all_projects()
        transfer = TodoistProjectListTransfer(orig_projects)
        return transfer.to_my_projects()

    def get_all_tasks(self, project_name: str) -> list:
        orig_tasks = self.datasource.get_all_tasks(project_name)
        transfer = TodoistTaskListTransfer(orig_tasks)
        return transfer.to_my_tasks()


class TodoistCommandService:
    def __init__(self, datasource: PytodoistAPIDataSource):
        self.datasource = datasource
