from typing import List

from rplugin.python3.model.task import create_task
from rplugin.python3.model.task import Task


class TodoistTaskListTransfer:
    def __init__(self, tasks: list) -> None:
        self.tasks = tasks

    def to_my_tasks(self) -> list:
        tasks: List(Task) = []
        for orig_task in self.tasks:
            tasks.append(create_task(
                task_id = self.task.id,
                content = self.task.content,
                project = self.task.project,
                project_id = self.task.project_id,
                is_checked = self.task.checked,
                user_id = self.task.user_id
            ))
        return tasks
