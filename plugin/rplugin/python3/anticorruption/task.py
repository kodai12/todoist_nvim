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
                task_id=orig_task.id,
                content=orig_task.content,
                project=orig_task.project,
                project_id=orig_task.project_id,
                is_checked=orig_task.checked,
                user_id=orig_task.user_id
            ))
        return tasks
