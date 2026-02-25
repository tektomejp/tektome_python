from enum import Enum


class CitationsSortKeys(str, Enum):
    CREATED = "created"
    TITLE = "title"
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)
