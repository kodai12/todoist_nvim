from pytodoist import todoist

from rplugin.python3.model.user import create_user


class TodoistUserTransfer:
    def __init__(self, user: todoist.User) -> None:
        self.user = user

    # convert処理(必要であれば)

    # to_my_userメソッド(自分で定義したUserクラスへ変換)
    # to_my_userメソッドはUserクラスが持つファクトリを呼び出す
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
