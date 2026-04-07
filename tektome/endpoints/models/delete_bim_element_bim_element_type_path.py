from enum import Enum


class DeleteBimElementBimElementTypePath(str, Enum):
    AGNOSTIC = "bim-agnostic"
    OBJECT = "bim-object"
    VIEW = "bim-view"

    def __str__(self) -> str:
        return str(self.value)
