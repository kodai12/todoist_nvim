from rplugin.python3.domain.model.task import Task
from rplugin.python3.domain.model.task import TaskId
from rplugin.python3.domain.model.task import Content
from rplugin.python3.domain.model.task import IsChecked
from rplugin.python3.domain.model.project import Project
from rplugin.python3.domain.model.user import UserId

def create_task(task_id: int,
                content: str,
                parent_project: Project,
                project_id: int,
                is_checked: bool,
                user_id: UserId) -> Task:
    return Task(
        task_id=TaskId(task_id),
        content=Content(content),
        parent_project=parent_project,
        project_id=ProjectId(project_id),
        is_checked=IsChecked(is_checked),
        user_id=UserId(user_id)
    )
