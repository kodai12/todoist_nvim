from datetime import datetime

from rplugin.python3.domain.model.entity import Entity
from rplugin.python3.domain.model.value import Value


class ProjectId(Value):
    def __init__(self, value: int) -> None:
        self.value = value


class Name(Value):
    def __init__(self, value: str) -> None:
        self.value = value


class Color(Value):
    def __init__(self, value: str) -> None:
        self.value = value


class Owner(Value):
    def __init__(self, value: str) -> None:
        self.value = value


class LastUpdated(Value):
    def __init__(self, value: datetime) -> None:
        self.value = value


class IsDeleted(Value):
    def __init__(self, value: bool) -> None:
        self.value = value


class IsArchived(Value):
    def __init__(self, value: bool) -> None:
        self.value = value


class Project(Entity):
    def __init__(self,
                 project_id: ProjectId,
                 name: Name,
                 color: Color,
                 owner: Owner,
                 is_deleted: IsDeleted) -> None:
        self.project_id = project_id
        self.name = name
        self.color = color
        self.owner = owner
        self.is_deleted = is_deleted
