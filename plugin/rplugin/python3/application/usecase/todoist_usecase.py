from rplugin.python3.domain.model.user import User
from rplugin.python3.domain.model.project import Project
from rplugin.python3.domain.model.task import Task

from rplugin.python3.dataaccess.pytodoist import PytodoistAPIDataSource

from rplugin.python3.anticorruption.user import TodoistUserTransfer
from rplugin.python3.anticorruption.project import TodoistProjectTransfer
from rplugin.python3.anticorruption.project import TodoistProjectListTransfer
from rplugin.python3.anticorruption.task import TodoistTaskTransfer
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

    def add_task(self,
                 project_name: str,
                 content: str) -> Task:
        orig_task = self.datasource.add_task(project_name, content)
        transfer = TodoistTaskTransfer(orig_task)
        return transfer.to_my_task()

    def complete_task(self,
                      project_name: str,
                      task_id: int) -> Task:
        completed_orig_task = self.datasource.complete_task(project_name, task_id)
        transfer = TodoistTaskTransfer(completed_orig_task)
        return transfer.to_my_task()

    def delete_task(self,
                    project_name: str,
                    task_id: int) -> Task:
        deleted_orig_task = self.datasource.delete_task(project_name, task_id)
        transfer = TodoistTaskTransfer(deleted_orig_task)
        return transfer.to_my_task()
