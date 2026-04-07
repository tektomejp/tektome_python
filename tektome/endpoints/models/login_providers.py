from enum import Enum


class LoginProviders(str, Enum):
    AZURE = "microsoft-entra-id"
    GOOGLE = "google"

    def __str__(self) -> str:
        return str(self.value)
