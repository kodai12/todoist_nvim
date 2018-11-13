from datetime import datetime

from rplugin.python3.domain.model.user import User
from rplugin.python3.domain.model.user import UserId
from rplugin.python3.domain.model.user import Email
from rplugin.python3.domain.model.user import Password
from rplugin.python3.domain.model.user import FullName
from rplugin.python3.domain.model.user import PremiumStatus
from rplugin.python3.domain.model.user import StartDay
from rplugin.python3.domain.model.user import ApiToken


def create_user(user_id: int,
                email: str,
                password: str,
                full_name: str,
                is_premium: bool,
                premium_until: datetime,
                start_day: datetime,
                api_token: str) -> User:
    return User(
        user_id=UserId(user_id),
        email=Email(email),
        password=Password(password),
        full_name=FullName(full_name),
        premium_status=PremiumStatus(is_premium, premium_until),
        start_day=StartDay(start_day),
        api_token=ApiToken(api_token)
    )
