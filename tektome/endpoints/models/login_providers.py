from enum import Enum


class LoginProviders(str, Enum):
    GOOGLE = "google"
    MICROSOFT_ENTRA_ID = "microsoft-entra-id"

    def __str__(self) -> str:
        return str(self.value)
