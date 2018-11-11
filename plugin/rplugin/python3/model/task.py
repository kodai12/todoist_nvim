from datetime import datetime

from rplugin.python3.model.entity import Entity
from rplugin.python3.model.value import Value


class TaskId(Value):
    def __init__(self, value: int) -> None:
        self.value = value


class Content(Value):
    def __init__(self, value: str) -> None:
        self.value = value


class Project(Value):
    def __init__(self, value: str) -> None:
        self.value = value


class ProjectId(Value):
    def __init__(self, value: int) -> None:
        self.value = value


class IsChecked(Value):
    def __init__(self, value: bool) -> None:
        self.value = value


class UserId(Value):
    def __init__(self, value: int) -> None:
        self.value = value


class Task(Entity):
    def __init__(self,
                 task_id: TaskId,
                 content: Content,
                 project: Project,
                 project_id: ProjectId,
                 is_checked: IsChecked,
                 user_id: UserId) -> None:
        self.task_id = task_id
        self.content = content
        self.project = project
        self.project_id = project_id
        self.is_checked = is_checked
        self.user_id = user_id

def create_task(task_id: int,
                content: str,
                project: str,
                project_id: int,
                is_checked: bool,
                user_id: int) -> Task:
    return Task(
        task_id=TaskId(task_id),
        content=Content(content),
        project=Project(project),
        project_id=ProjectId(project_id),
        is_checked=IsChecked(is_checked),
        user_id=UserId(user_id)
    )
