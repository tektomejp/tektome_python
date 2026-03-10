from enum import Enum


class RoleName(str, Enum):
    DATASPACE_ADMIN = "Dataspace Admin"
    DATASPACE_MEMBER = "Dataspace Member"
    DATASPACE_OWNER = "Dataspace Owner"
    DATASPACE_VIEWER = "Dataspace Viewer"
    INDIVIDUAL_USER = "Individual User"
    ORGANIZATION_ADMIN = "Organization Admin"
    ORGANIZATION_MEMBER = "Organization Member"
    PROJECT_ADMIN = "Project Admin"
    PROJECT_MEMBER = "Project Member"
    PROJECT_OWNER = "Project Owner"
    PROJECT_VIEWER = "Project Viewer"
    SYSTEM_SUPER_ADMIN = "System Super Admin"

    def __str__(self) -> str:
        return str(self.value)
