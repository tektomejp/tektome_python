from enum import Enum


class NotificationEntityType(str, Enum):
    APPROVAL_TICKET = "approval_ticket"
    EXECUTION = "execution"
    EXECUTION_GROUP = "execution_group"

    def __str__(self) -> str:
        return str(self.value)
