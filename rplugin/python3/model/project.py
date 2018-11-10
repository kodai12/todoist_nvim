import sys
from pytodoist import todoist

class Project:
    def __init__(self, original_project: todoist.Project) -> None:
        self = original_project

