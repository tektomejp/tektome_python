from enum import Enum


class NonPrimitiveRoleName(str, Enum):
    EXTERNAL_ORGANIZATION_MEMBER = "External Organization Member"

    def __str__(self) -> str:
        return str(self.value)
