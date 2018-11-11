from rplugin.python3.dataaccess.pytodoist import PytodoistAPIDataSource
from rplugin.python3.model.user import User
from rplugin.python3.model.project import Project


class TodoistService:
    def __init__(self, datasouce: PytodoistAPIDataSource):
        self.datasouce = datasouce

    def get_user(self) -> User:
        return self.datasouce.get_user()

    def get_project(self, project_name: str) -> Project:
        return self.datasouce.get_project(project_name)

    def get_all_projects(self) -> list:
        return self.datasouce.get_all_projects()
