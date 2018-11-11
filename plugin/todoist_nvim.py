import vim
from rplugin.python3.dataaccess.pytodoist import PytodoistAPIDataSource
from rplugin.python3.service.todoist import TodoistService


def get_user():
    datasource = PytodoistAPIDataSource(_get_email(), _get_password())
    service = TodoistService(datasource)
    user = service.get_user()
    if user:  # MEMO Entityの存在チェックどうするか
        print('Id: {}\nユーザー名 {}\nEmail: {}'
              .format(user.user_id.value,
                      user.full_name.value,
                      user.email.value))
    else:
        print('User not found.')


def get_project(project_name: str):
    datasource = PytodoistAPIDataSource(_get_email(), _get_password())
    service = TodoistService(datasource)
    project = service.get_project(project_name)
    if project:
        print('Id: {}\nプロジェクト名: {}\n削除ステータス: {}'
              .format(project.project_id.value,
                      project.name.value,
                      '削除済み' if project.is_deleted.value else '削除されていません'))
    else:
        print('プロジェクトが見つかりませんでした')


def get_all_projects():
    datasource = PytodoistAPIDataSource(_get_email(), _get_password())
    service = TodoistService(datasource)
    projects = service.get_all_projects()
    if len(projects) == 0:
        print('プロジェクトが見つかりませんでした')
    for project in projects:
        print('Id: {}\nプロジェクト名: {}\n削除ステータス: {}\n============================='
              .format(project.project_id.value,
                      project.name.value,
                      '削除済み' if project.is_deleted.value else '削除されていません'))


def get_all_tasks(args: str):
    args = _parse_args(args)
    datasource = PytodoistAPIDataSource(_get_email(), _get_password())
    service = TodoistService(datasource)
    tasks = []
    if 'project' in args and args.project != '':
        tasks = service.get_all_tasks(args.project)
    if len(tasks) == 0:
        print('タスクが見つかりませんでした')
    for task in tasks:
        print('Id: {}\nタスク: {}\n親プロジェクト: {}\n============================='
              .format(task.task_id.value,
                      task.content.value,
                      task.parent_project.name.value))


def get_all_notes():
    pass


def _get_api_token():
    token_exists = int(vim.eval('exists("g:todoist_api_token")'))

    if token_exists:
        return vim.eval('g:todoist_api_token')
    else:
        print("API Token is not set. Please type: \
              let g:todoist_api_token = 'YOUR_TOKEN'")
        return 0


def _get_email():
    email_exists = vim.eval('exists("g:todoist_email")')

    if email_exists:
        return vim.eval('g:todoist_email')


def _get_password():
    password_exists = vim.eval('exists("g:todoist_password")')

    if password_exists:
        return vim.eval('g:todoist_password')


def _parse_args(arg_str: str) -> object:
    arg_list: list = arg_str.split()
    project_symbol = '+'
    tag_symbol = '@'
    result = {
        'args': '',
        'project': '',
        'tag': '',
    }
    for arg in arg_list:
        if arg.find(project_symbol) > -1:
            result.project = arg[1:]
        if arg.find(tag_symbol) > -1:
            result.tag = arg[1:]
        else:
            result.args = arg

    return result
