from datetime import datetime

from rplugin.python3.domain.model.entity import Entity
from rplugin.python3.domain.model.value import Value


class UserId(Value):
    def __init__(self, value: int) -> None:
        self.value = value


class Email(Value):
    def __init__(self, value: str) -> None:
        self.value = value


class Password(Value):
    def __init__(self, value: str) -> None:
        self.value = value


class FullName(Value):
    def __init__(self, value: str) -> None:
        self.value = value


class PremiumStatus(Value):
    def __init__(self, is_premium: bool, premium_until: datetime) -> None:
        self.is_premium = is_premium
        self.premium_until = premium_until


class StartDay(Value):
    def __init__(self, value: datetime) -> None:
        self.value = value


class ApiToken(Value):
    def __init__(self, value: str):
        self.value = value


class User(Entity):
    def __init__(self,
                 user_id: UserId,
                 email: Email,
                 password: Password,
                 full_name: FullName,
                 premium_status: PremiumStatus,
                 start_day: StartDay,
                 api_token: ApiToken) -> None:
        self.user_id = user_id
        self.email = email
        self.password = password
        self.full_name = full_name
        self.premium_status = premium_status
        self.start_day = start_day
        self.api_token = api_token


def create_user(user_id: int,
                email: str,
                password: str,
                full_name: str,
                is_premium: bool,
                premium_until: datetime,
                start_day: datetime,
                api_token: str):
    return User(
        user_id=UserId(user_id),
        email=Email(email),
        password=Password(password),
        full_name=FullName(full_name),
        premium_status=PremiumStatus(is_premium, premium_until),
        start_day=StartDay(start_day),
        api_token=ApiToken(api_token)
    )

