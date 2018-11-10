from datetime import datetime

from rplugin.python3.model.entity import Entity
from rplugin.python3.model.value import Value


class UserId(Value):
    def __init__(self, value: int) -> None:
        self.user_id = value


class Email(Value):
    def __init__(self, value: str) -> None:
        self.email = value


class Password(Value):
    def __init__(self, value: str) -> None:
        self.password = value


class FullName(Value):
    def __init__(self, value: str) -> None:
        self.full_name = value


class PremiumStatus(Value):
    def __init__(self, is_premium:bool, premium_until: datetime) -> None:
        self.is_premium = is_premium
        self.premium_until = premium_until


class StartDay(Value):
    def __init__(self, value: datetime) -> None:
        self.start_day = value


class ApiToken(Value):
    def __init__(self, value: str):
        self.api_token = value


class User(Entity):
    def __init__(self,
                 user_id: UserId,
                 email: Email,
                 password: Password,
                 full_name: FullName,
                 premium_status: PremiumStatus,
                 start_day: StartDay,
                 api_token: ApiToken) -> None:
        self.user_id = user_id,
        self.email = email,
        self.password = password,
        self.full_name = full_name,
        self.premium_status = premium_status,
        self.start_day = start_day,
        self.api_token = api_token,

    def get_project(self, project_name: str):
        pass

    def get_all_project(self):
        pass


