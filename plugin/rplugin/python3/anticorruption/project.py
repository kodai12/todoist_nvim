from pytodoist import todoist

from rplugin.python3.model.project import create_project

class TodoistProjectTransfer:
    def __init__(self, project: todoist.Projec) -> None:
        self.project = project

    def to_my_project(self):
        return create_project(
            project_id=self.project_id,
            name=self.name,
            color=self.color,
            owner=self.owner,
            last_updated=self.last_updated,
            is_deleted=self.is_deleted,
            is_archived=self.is_archived
        )
