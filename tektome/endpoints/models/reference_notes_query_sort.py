from enum import Enum


class ReferenceNotesQuerySort(str, Enum):
    ASC = "asc"
    DESC = "desc"

    def __str__(self) -> str:
        return str(self.value)
