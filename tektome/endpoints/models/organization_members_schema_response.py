from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.organization_members_schema_response_assigned_dataspaces import (
        OrganizationMembersSchemaResponseAssignedDataspaces,
    )
    from ..models.organization_members_schema_response_assigned_projects import (
        OrganizationMembersSchemaResponseAssignedProjects,
    )
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="OrganizationMembersSchemaResponse")


@_attrs_define
class OrganizationMembersSchemaResponse:
    """
    Attributes:
        id (UUID):
        first_name (str):
        last_name (str):
        email (str):
        roles (list[str]):
        date_added (datetime.datetime | None):
        assigned_dataspaces (OrganizationMembersSchemaResponseAssignedDataspaces):
        assigned_projects (OrganizationMembersSchemaResponseAssignedProjects):
        updated_by (None | UserMetadata):
    """

    id: UUID
    first_name: str
    last_name: str
    email: str
    roles: list[str]
    date_added: datetime.datetime | None
    assigned_dataspaces: OrganizationMembersSchemaResponseAssignedDataspaces
    assigned_projects: OrganizationMembersSchemaResponseAssignedProjects
    updated_by: None | UserMetadata
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_metadata import UserMetadata

        id = str(self.id)

        first_name = self.first_name

        last_name = self.last_name

        email = self.email

        roles = self.roles

        date_added: None | str
        if isinstance(self.date_added, datetime.datetime):
            date_added = self.date_added.isoformat()
        else:
            date_added = self.date_added

        assigned_dataspaces = self.assigned_dataspaces.to_dict()

        assigned_projects = self.assigned_projects.to_dict()

        updated_by: dict[str, Any] | None
        if isinstance(self.updated_by, UserMetadata):
            updated_by = self.updated_by.to_dict()
        else:
            updated_by = self.updated_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "roles": roles,
                "date_added": date_added,
                "assigned_dataspaces": assigned_dataspaces,
                "assigned_projects": assigned_projects,
                "updated_by": updated_by,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_members_schema_response_assigned_dataspaces import (
            OrganizationMembersSchemaResponseAssignedDataspaces,
        )
        from ..models.organization_members_schema_response_assigned_projects import (
            OrganizationMembersSchemaResponseAssignedProjects,
        )
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        email = d.pop("email")

        roles = cast(list[str], d.pop("roles"))

        def _parse_date_added(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_added_type_0 = isoparse(data)

                return date_added_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        date_added = _parse_date_added(d.pop("date_added"))

        assigned_dataspaces = OrganizationMembersSchemaResponseAssignedDataspaces.from_dict(
            d.pop("assigned_dataspaces")
        )

        assigned_projects = OrganizationMembersSchemaResponseAssignedProjects.from_dict(d.pop("assigned_projects"))

        def _parse_updated_by(data: object) -> None | UserMetadata:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                updated_by_type_0 = UserMetadata.from_dict(data)

                return updated_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UserMetadata, data)

        updated_by = _parse_updated_by(d.pop("updated_by"))

        organization_members_schema_response = cls(
            id=id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            roles=roles,
            date_added=date_added,
            assigned_dataspaces=assigned_dataspaces,
            assigned_projects=assigned_projects,
            updated_by=updated_by,
        )

        organization_members_schema_response.additional_properties = d
        return organization_members_schema_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
