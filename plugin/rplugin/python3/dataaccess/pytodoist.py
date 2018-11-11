from pytodoist import todoist


class PytodoistAPIDataSource:
    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.password = password

    def get_user(self) -> todoist.User:
        return todoist.login(self.email, self.password)

    def get_project(self, project_name: str) -> todoist.Project:
        orig_user = todoist.login(self.email, self.password)
        return orig_user.get_project(project_name)

    def get_all_projects(self) -> list:
        orig_user = todoist.login(self.email, self.password)
        return orig_user.get_projects()

    def get_all_tasks(self, project_name: str) -> list:
        orig_user = todoist.login(self.email, self.password)
        orig_project = orig_user.get_project(project_name)
        return orig_project.get_tasks()
