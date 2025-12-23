from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="DataspaceMembersSchemaOut")


@_attrs_define
class DataspaceMembersSchemaOut:
    """Schema for retrieving each member in a dataspace.

    Attributes:
        id (UUID):
        first_name (str):
        last_name (str):
        email (str):
        roles (list[str]):
        date_added (datetime.datetime | None):
        updated_by (UserMetadata):
    """

    id: UUID
    first_name: str
    last_name: str
    email: str
    roles: list[str]
    date_added: datetime.datetime | None
    updated_by: UserMetadata
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        updated_by = self.updated_by.to_dict()

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
                "updated_by": updated_by,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        updated_by = UserMetadata.from_dict(d.pop("updated_by"))

        dataspace_members_schema_out = cls(
            id=id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            roles=roles,
            date_added=date_added,
            updated_by=updated_by,
        )

        dataspace_members_schema_out.additional_properties = d
        return dataspace_members_schema_out

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
