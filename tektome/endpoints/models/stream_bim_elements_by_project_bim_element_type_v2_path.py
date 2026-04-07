from enum import Enum


class StreamBimElementsByProjectBimElementTypeV2Path(str, Enum):
    OBJECT = "bim-object"
    SHEET = "bim-sheet"
    VIEW = "bim-view"

    def __str__(self) -> str:
        return str(self.value)
