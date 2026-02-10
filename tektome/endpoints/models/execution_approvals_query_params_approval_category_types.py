from enum import Enum


class ExecutionApprovalsQueryParamsApprovalCategoryTypes(str, Enum):
    ATTRIBUTE_UPDATE = "Attribute Update"
    FILE_EXTRACTION = "File Extraction"

    def __str__(self) -> str:
        return str(self.value)
