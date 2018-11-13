from rplugin.python3.domain.model.project import Project
from rplugin.python3.domain.model.project import ProjectId
from rplugin.python3.domain.model.project import Name
from rplugin.python3.domain.model.project import Color
from rplugin.python3.domain.model.project import Owner
from rplugin.python3.domain.model.project import IsDeleted
from rplugin.python3.domain.model.project import Project

def create_project(project_id: int,
                   name: str,
                   color: str,
                   owner: str,
                   is_deleted: str) -> Project:
    return Project(
        project_id=ProjectId(project_id),
        name=Name(name),
        color=Color(color),
        owner=Owner(owner),
        is_deleted=IsDeleted(is_deleted),
    )
