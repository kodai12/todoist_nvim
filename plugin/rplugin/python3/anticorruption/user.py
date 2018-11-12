from ...explugin.pytodoist import todoist

from rplugin.python3.model.user import create_user


class TodoistUserTransfer:
    def __init__(self, user: todoist.User) -> None:
        self.user = user

    def to_my_user(self):
        return create_user(
            user_id=self.user.id,
            email=self.user.email,
            password=self.user.password,
            full_name=self.user.full_name,
            is_premium=self.user.is_premium,
            premium_until=self.user.premium_until,
            start_day=self.user.start_day,
            api_token=self.user.api_token
        )
