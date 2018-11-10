import vim
from rplugin.python3.service.todoist import TodoistService

def get_project(project_name: str):
    service = TodoistService(_get_email(), _get_password())
    return service.get_project(project_name)

def get_all_projects():
    service = TodoistService(_get_email(), _get_password())
    projects = service.get_all_projects()
    for project in projects:
        print(project.name)

def _get_api_token():
    token_exists = int(vim.eval('exists("g:todoist_api_token")'))

    if token_exists:
        return vim.eval('g:todoist_api_token')
    else:
        print("API Token is not set. Please type: let g:todoist_api_token = 'YOUR_TOKEN'")
        return 0

def _get_email():
    email_exists = vim.eval('exists("g:todoist_email")')

    if email_exists:
        return vim.eval('g:todoist_email')

def _get_password():
    password_exists = vim.eval('exists("g:todoist_password")')

    if password_exists:
        return vim.eval('g:todoist_password')

