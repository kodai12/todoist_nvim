import vim
from rplugin.python3.dataaccess.pytodoist import PytodoistAPIDataSource


def get_user():
    dataaccess = PytodoistAPIDataSource(_get_email(), _get_password())
    user = dataaccess.get_user()
    print(user)
    print('type of return value is {}'.format(type(user)))

def get_project(project_name: str):
    dataaccess = PytodoistAPIDataSource(_get_email(), _get_password())
    project_name = str(project_name.strip())
    print(dataaccess.get_project(project_name))


def get_all_projects():
    pass


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

