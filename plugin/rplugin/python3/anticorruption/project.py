from pytodoist import todoist

from typing import List

from rplugin.python3.domain.model.project import Project
from rplugin.python3.domain.factory.project import create_project


class TodoistProjectTransfer:
    def __init__(self, project: todoist.Project) -> None:
        self.project = project

    def to_my_project(self) -> Project:
        return create_project(
            project_id=self.project.id,
            name=self.project.name,
            color=self.project.color,
            owner=self.project.owner,
            is_deleted=self.project.is_deleted,
        )


class TodoistProjectListTransfer:
    def __init__(self, projects: list) -> None:
        self.projects = projects

    def to_my_projects(self) -> list:
        projects: List(Project) = []
        for orig_project in self.projects:
            projects.append(create_project(
                project_id=orig_project.id,
                name=orig_project.name,
                color=orig_project.color,
                owner=orig_project.owner,
                is_deleted=orig_project.is_deleted,
            ))
        return projects
