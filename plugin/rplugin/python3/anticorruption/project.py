from pytodoist import todoist

from rplugin.python3.model.project import create_project


class TodoistProjectTransfer:
    def __init__(self, project: todoist.Project) -> None:
        self.project = project

    def to_my_project(self):
        return create_project(
            project_id=self.project.project_id,
            name=self.project.name,
            color=self.project.color,
            owner=self.project.owner,
            last_updated=self.project.last_updated,
            is_deleted=self.project.is_deleted,
            is_archived=self.project.is_archived
        )
