from pytodoist import todoist

from typing import List

from rplugin.python3.domain.model.reminder import Reminder
from rplugin.python3.domain.factory.reminder import create_reminder


class TodoistReminderTransfer:
    def __init__(self, reminder: todoist.Reminder) -> None:
        self.reminder = reminder

    def to_my_reminder(self) -> Reminder:
        return create_reminder(
            reminder_id=self.reminder.id,
            item_id=self.reminder.item_id,
            service=self.reminder_id.service,
            due_date=self.reminder.due_date
        )


class TodoistReminderListTransfer:
    def __init__(self, reminders: list) -> None:
        self.reminders = reminders

    def to_my_reminders(self) -> list:
        reminders: List(Reminder) = []
        for orig_reminedr in self.reminders:
            reminders.append(create_reminder(
                reminder_id=self.reminder.id,
                item_id=self.reminder.item_id,
                service=self.reminder_id.service,
                due_date=self.reminder.due_date
            ))
        return reminders
