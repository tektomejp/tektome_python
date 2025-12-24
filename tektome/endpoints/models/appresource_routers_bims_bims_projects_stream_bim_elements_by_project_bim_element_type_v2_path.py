from enum import Enum


class AppresourceRoutersBimsBimsProjectsStreamBimElementsByProjectBimElementTypeV2Path(str, Enum):
    BIM_OBJECT = "bim-object"
    BIM_SHEET = "bim-sheet"
    BIM_VIEW = "bim-view"

    def __str__(self) -> str:
        return str(self.value)
