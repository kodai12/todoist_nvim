
from rplugin.python3.model.user import UserDomainService


class TodoistService:
    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.password = password

    def get_project(self, project_name: str):
        user = UserDomainService.get_original_user(self.email, self.password)
        return user.get_project(project_name)

    def get_all_projects(self):
        user = UserDomainService.get_original_user(self.email, self.password)
        return user.get_projects()
