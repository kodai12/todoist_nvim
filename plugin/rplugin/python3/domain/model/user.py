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


class IsPremium(Value):
    def __init__(self, value: bool) -> None:
        self.value = value


class PremiumUntil(Value):
    def __init__(self, vallue: datetime):
        self.value = value


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
                 is_premium: IsPremium,
                 premium_until: PremiumUntil,
                 start_day: StartDay,
                 api_token: ApiToken) -> None:
        self.user_id = user_id
        self.email = email
        self.password = password
        self.full_name = full_name
        self.is_premium = is_premium
        self.premium_until = premium_until
        self.start_day = start_day
        self.api_token = api_token

    def validate_premium(self) -> bool:
        now = datetime.now
        if self.is_premium && self.premium_until > now:
            return True
        return False
