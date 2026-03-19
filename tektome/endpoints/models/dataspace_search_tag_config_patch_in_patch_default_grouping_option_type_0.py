from enum import Enum


class DataspaceSearchTagConfigPatchInPatchDefaultGroupingOptionType0(str, Enum):
    PROJECT = "project"
    RESOURCE = "resource"

    def __str__(self) -> str:
        return str(self.value)
