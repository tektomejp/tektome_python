from enum import Enum


class DeleteBimElementBimElementTypePath(str, Enum):
    BIM_AGNOSTIC = "bim-agnostic"
    BIM_OBJECT = "bim-object"
    BIM_VIEW = "bim-view"

    def __str__(self) -> str:
        return str(self.value)
