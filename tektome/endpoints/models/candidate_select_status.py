from enum import Enum


class CandidateSelectStatus(str, Enum):
    SELECT = "Selected"
    UNSELECTED = "Unselected"

    def __str__(self) -> str:
        return str(self.value)
