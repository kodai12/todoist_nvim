from enum import Enum
from datetime import datetime

from rplugin.python3.domain.model.entity import Entity
from rplugin.python3.domain.model.value import Value

class ReminderId(Value):
    def __init__(self, value: int) -> None:
        self.value = value


class ItemId(Value):
    def __init__(self, value: int) -> None:
        self.value = value


class Service(Enum):
    email = auto()
    sms = auto()
    push = auto()


class DueDate(Value):
    def __init__(self, value: datetime) -> None:
        self.value = value


class Reminder(Entity):
    def __init__(self,
                 reminder_id: ReminderId,
                 item_id: ItemId,
                 service: Service,
                 due_date: DueDate) -> None:
        self.reminder_id = reminder_id
        self.item_id = item_id
        self.service = service
        self.due_date = due_date
