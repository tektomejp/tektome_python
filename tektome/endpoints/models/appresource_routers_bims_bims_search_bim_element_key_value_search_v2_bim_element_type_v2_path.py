from enum import Enum


class AppresourceRoutersBimsBimsSearchBimElementKeyValueSearchV2BimElementTypeV2Path(str, Enum):
    BIM_OBJECT = "bim-object"
    BIM_SHEET = "bim-sheet"
    BIM_VIEW = "bim-view"

    def __str__(self) -> str:
        return str(self.value)
