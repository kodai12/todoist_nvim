from pytodoist import todoist


class PytodoistAPIDataSource:
    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.password = password

    def get_user(self) -> todoist.User:
        return todoist.login(self.email, self.password)

    def get_project(self, project_name: str) -> todoist.Project:
        orig_user = self.get_user()
        return orig_user.get_project(project_name)

    def get_all_projects(self) -> list:
        orig_user = self.get_user()
        return orig_user.get_projects()

    def get_all_tasks(self, project_name: str) -> list:
        orig_user = self.get_user()
        orig_project = orig_user.get_project(project_name)
        return orig_project.get_tasks()

    def add_task(self,
                 project_name: str,
                 content: str,
                 date=None,
                 priority=None) -> todoist.Task:
        orig_project = self.get_project(project_name)
        orig_task = orig_project.add_task(content, date, priority)
        return orig_task

    def complete_task(self,
                      project_name: str,
                      task_id: int) -> None:
        orig_task = self._get_task_by_task_id(project_name, task_id)
        orig_task.complete()
        return orig_task

    def delete_task(self,
                    project_name: str,
                    task_id: int) -> None:
        orig_task = self._get_task_by_task_id(project_name, task_id)
        orig_task.delete()
        return orig_task

    def _get_task_by_task_id(self, project_name: str, task_id: int) -> todoist.Task:
        orig_tasks = self.get_all_tasks(project_name)
        orig_task = [task for task in orig_tasks if task.__dict__['id'] == task_id]
        if len(orig_task) == 0:
            return None  # MEMO 例外処理を追加する
        return orig_task[0]

