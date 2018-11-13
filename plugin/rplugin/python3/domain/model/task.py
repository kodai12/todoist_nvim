from rplugin.python3.domain.model.entity import Entity
from rplugin.python3.domain.model.value import Value
from rplugin.python3.domain.model.project import Project
from rplugin.python3.domain.model.user import UserId


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
