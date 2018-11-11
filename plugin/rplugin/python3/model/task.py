from rplugin.python3.model.entity import Entity
from rplugin.python3.model.value import Value
from rplugin.python3.model.project import Project


class TaskId(Value):
    def __init__(self, value: int) -> None:
        self.value = value


class Content(Value):
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
                 parent_project: Project,
                 project_id: ProjectId,
                 is_checked: IsChecked,
                 user_id: UserId) -> None:
        self.task_id = task_id
        self.content = content
        self.parent_project = parent_project
        self.project_id = project_id
        self.is_checked = is_checked
        self.user_id = user_id


def create_task(task_id: int,
                content: str,
                parent_project: Project,
                project_id: int,
                is_checked: bool,
                user_id: int) -> Task:
    return Task(
        task_id=TaskId(task_id),
        content=Content(content),
        parent_project=parent_project,
        project_id=ProjectId(project_id),
        is_checked=IsChecked(is_checked),
        user_id=UserId(user_id)
    )
