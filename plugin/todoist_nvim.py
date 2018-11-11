import vim
from rplugin.python3.dataaccess.pytodoist import PytodoistAPIDataSource
from rplugin.python3.service.todoist import TodoistService


def get_user():
    datasource = PytodoistAPIDataSource(_get_email(), _get_password())
    service = TodoistService(datasource)
    user = service.get_user()
    if user:  # TODO Entityの存在チェックどうするか
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

