from enum import Enum


class AvailableLanguage(str, Enum):
    EN = "en"
    JA = "ja"

    def __str__(self) -> str:
        return str(self.value)
