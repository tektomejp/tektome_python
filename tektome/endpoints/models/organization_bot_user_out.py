from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="OrganizationBotUserOut")


@_attrs_define
class OrganizationBotUserOut:
    """Response schema for bot user creation

    Attributes:
        id (UUID):
        username (str):
        email (str):
        organization_id (UUID):
        roles (list[str]):
        date_joined (datetime.datetime):
    """

    id: UUID
    username: str
    email: str
    organization_id: UUID
    roles: list[str]
    date_joined: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        username = self.username

        email = self.email

        organization_id = str(self.organization_id)

        roles = self.roles

        date_joined = self.date_joined.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "username": username,
                "email": email,
                "organization_id": organization_id,
                "roles": roles,
                "date_joined": date_joined,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        username = d.pop("username")

        email = d.pop("email")

        organization_id = UUID(d.pop("organization_id"))

        roles = cast(list[str], d.pop("roles"))

        date_joined = isoparse(d.pop("date_joined"))

        organization_bot_user_out = cls(
            id=id,
            username=username,
            email=email,
            organization_id=organization_id,
            roles=roles,
            date_joined=date_joined,
        )

        organization_bot_user_out.additional_properties = d
        return organization_bot_user_out

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
