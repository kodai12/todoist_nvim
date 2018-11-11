from datetime import datetime

from rplugin.python3.model.entity import Entity
from rplugin.python3.model.value import Value

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
                 last_updated: LastUpdated,
                 is_deleted: IsDeleted,
                 is_archived: IsArchived) -> None:
        self.project_id = project_id
        self.name = name
        self.color = color
        self.owner = owner
        self.last_updated = last_updated
        self.is_deleted = is_deleted
        self.is_archived = is_archived

def create_project(project_id: int,
                   name: str,
                   color: str,
                   owner: str,
                   last_updated: datetime,
                   is_deleted: str,
                   is_archived: str) -> Project:
    return Project(
        project_id=ProjectId(project_id),
        name=Name(name),
        color=Color(color),
        owner=Owner(owner),
        last_updated=LastUpdated(last_updated),
        is_deleted=IsDeleted(is_deleted),
        is_archive=IsArchived(is_archived)
    )
