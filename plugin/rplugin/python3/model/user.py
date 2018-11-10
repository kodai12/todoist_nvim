
from rplugin.python3.model.project import Project
from pytodoist import todoist
import sys
sys.path.append('/Users/sakochikodai/Desktop/todoist_nvim')


class UserDomainService:
    @staticmethod
    def get_user(email: str, password: str) -> object:
        original_user = todoist.login(email, password)
        return User(original_user)

    @staticmethod
    def get_original_user(email: str, password: str) -> object:
        return todoist.login(email, password)


class User(todoist.User):
    def __init__(self) -> None:
        pass

    def get_project(self, project_name: str):
        project_orig = super().get_project(project_name)
        return Project(project_orig)

    def get_all_project(self):
        projects_orig = super().get_projects()
        projects: list(Project) = []
        for project_orig in projects_orig:
            projects.append(Project(project_orig))
        return projects
