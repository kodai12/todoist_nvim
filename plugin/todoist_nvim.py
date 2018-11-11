import vim
from rplugin.python3.dataaccess.pytodoist import PytodoistAPIDataSource
from rplugin.python3.service.todoist import TodoistQueryService


def get_user():
    datasource = PytodoistAPIDataSource(_get_email(), _get_password())
    service = TodoistQueryService(datasource)
    user = service.get_user()
    if user:  # MEMO Entityの存在チェックどうするか
        print('Id: {}\nユーザー名 {}\nEmail: {}'
              .format(user.user_id.value,
                      user.full_name.value,
                      user.email.value))
    else:
        print('User not found.')


def get_project(args: str):
    args = _parse_args(args)
    if 'project' not in args or args['project'] == '':
        print('プロジェクト名を入力してください ex) :TodoistProject +Inbox')
        return
    datasource = PytodoistAPIDataSource(_get_email(), _get_password())
    service = TodoistQueryService(datasource)
    project = service.get_project(args['project'])
    if project:  # MEMO 存在チェック
        print('Id: {}\nプロジェクト名: {}\n削除ステータス: {}'
              .format(project.project_id.value,
                      project.name.value,
                      '削除済み' if project.is_deleted.value else '削除されていません'))
    else:
        print('プロジェクトが見つかりませんでした')


def get_all_projects():
    datasource = PytodoistAPIDataSource(_get_email(), _get_password())
    service = TodoistQueryService(datasource)
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
    if 'project' not in args or args['project'] == '':
        print('プロジェクト名を入力してください ex) :TodoistTasks +Inbox')
        return
    datasource = PytodoistAPIDataSource(_get_email(), _get_password())
    service = TodoistQueryService(datasource)
    tasks = service.get_all_tasks(args['project'])
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
    _arg_list: list = arg_str.split()
    _project_symbol = '+'
    _tag_symbol = '@'
    result = {
        'args': '',
        'project': '',
        'tag': '',
    }
    for _arg in _arg_list:
        if _arg.find(_project_symbol) > -1:
            result['project'] = _arg[1:]
        if _arg.find(_tag_symbol) > -1:
            result['tag'] = _arg[1:]
        else:
            result['args'] = _arg

    return result
