from pytodoist import todoist
from typing import List

from rplugin.python3.model.task import create_task
from rplugin.python3.model.task import Task

from rplugin.python3.anticorruption.project import TodoistProjectTransfer


class TodoistTaskListTransfer:
    def __init__(self, task: todoist.Task) -> None:
        self.task = task

    def to_my_tasks(self) -> list:
        _project_transfer = TodoistProjectTransfer(self.task.project)
        _parent_project = _project_transfer.to_my_project()
        return create_task(
            task_id=orig_task.id,
            content=orig_task.content,
            parent_project=_parent_project,
            project_id=orig_task.project_id,
            is_checked=orig_task.checked,
            user_id=orig_task.user_id
        )


class TodoistTaskListTransfer:
    def __init__(self, tasks: list) -> None:
        self.tasks = tasks

    def to_my_tasks(self) -> list:
        tasks: List(Task) = []
        for orig_task in self.tasks:
            _project_transfer = TodoistProjectTransfer(orig_task.project)
            _parent_project = _project_transfer.to_my_project()
            tasks.append(create_task(
                task_id=orig_task.id,
                content=orig_task.content,
                parent_project=_parent_project,
                project_id=orig_task.project_id,
                is_checked=orig_task.checked,
                user_id=orig_task.user_id
            ))
        return tasks
