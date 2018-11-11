from rplugin.python3.dataaccess.pytodoist import PytodoistAPIDataSource
from rplugin.python3.model.user import User


class TodoistService:
    def __init__(self, datasouce: PytodoistAPIDataSource):
        self.datasouce = datasouce

    def get_user(self) -> User:
        return self.datasouce.get_user()

