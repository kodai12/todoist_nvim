from datetime import datetime

from rplugin.python3.domain.model.reminder import Reminder
from rplugin.python3.domain.model.reminder import ReminderId
from rplugin.python3.domain.model.reminder import ItemId
from rplugin.python3.domain.model.reminder import Service
from rplugin.python3.domain.model.reminder import DueDate

def create_reminder(reminder_id: int,
                    item_id: int,
                    service: str,
                    due_date: datetime) -> Reminder:
    return Reminder(
        reminder_id=ReminderId(reminder_id),
        item_id=ItemId(item_id),
        service=Service(service),
        due_date=DueDate(due_date)
    )
