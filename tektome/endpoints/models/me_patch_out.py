from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assigned_role_schema_out import AssignedRoleSchemaOut
    from ..models.current_organization_schema import CurrentOrganizationSchema


T = TypeVar("T", bound="MePatchOut")


@_attrs_define
class MePatchOut:
    """
    Attributes:
        created (datetime.datetime):
        updated (datetime.datetime):
        id (UUID):
        username (str):
        language (str):
        email (str):
        is_timezone_auto_detect (bool):
        current_organization (CurrentOrganizationSchema):
        first_name (str | Unset):  Default: ''.
        last_name (str | Unset):  Default: ''.
        avatar_url (None | str | Unset):
        tos_accepted_at (datetime.datetime | None | Unset):
        role_assignments (list[AssignedRoleSchemaOut] | Unset):
    """

    created: datetime.datetime
    updated: datetime.datetime
    id: UUID
    username: str
    language: str
    email: str
    is_timezone_auto_detect: bool
    current_organization: CurrentOrganizationSchema
    first_name: str | Unset = ""
    last_name: str | Unset = ""
    avatar_url: None | str | Unset = UNSET
    tos_accepted_at: datetime.datetime | None | Unset = UNSET
    role_assignments: list[AssignedRoleSchemaOut] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created.isoformat()

        updated = self.updated.isoformat()

        id = str(self.id)

        username = self.username

        language = self.language

        email = self.email

        is_timezone_auto_detect = self.is_timezone_auto_detect

        current_organization = self.current_organization.to_dict()

        first_name = self.first_name

        last_name = self.last_name

        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        tos_accepted_at: None | str | Unset
        if isinstance(self.tos_accepted_at, Unset):
            tos_accepted_at = UNSET
        elif isinstance(self.tos_accepted_at, datetime.datetime):
            tos_accepted_at = self.tos_accepted_at.isoformat()
        else:
            tos_accepted_at = self.tos_accepted_at

        role_assignments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.role_assignments, Unset):
            role_assignments = []
            for role_assignments_item_data in self.role_assignments:
                role_assignments_item = role_assignments_item_data.to_dict()
                role_assignments.append(role_assignments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "updated": updated,
                "id": id,
                "username": username,
                "language": language,
                "email": email,
                "is_timezone_auto_detect": is_timezone_auto_detect,
                "current_organization": current_organization,
            }
        )
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if tos_accepted_at is not UNSET:
            field_dict["tos_accepted_at"] = tos_accepted_at
        if role_assignments is not UNSET:
            field_dict["role_assignments"] = role_assignments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.assigned_role_schema_out import AssignedRoleSchemaOut
        from ..models.current_organization_schema import CurrentOrganizationSchema

        d = dict(src_dict)
        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        id = UUID(d.pop("id"))

        username = d.pop("username")

        language = d.pop("language")

        email = d.pop("email")

        is_timezone_auto_detect = d.pop("is_timezone_auto_detect")

        current_organization = CurrentOrganizationSchema.from_dict(d.pop("current_organization"))

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        def _parse_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url = _parse_avatar_url(d.pop("avatar_url", UNSET))

        def _parse_tos_accepted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tos_accepted_at_type_0 = isoparse(data)

                return tos_accepted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        tos_accepted_at = _parse_tos_accepted_at(d.pop("tos_accepted_at", UNSET))

        _role_assignments = d.pop("role_assignments", UNSET)
        role_assignments: list[AssignedRoleSchemaOut] | Unset = UNSET
        if _role_assignments is not UNSET:
            role_assignments = []
            for role_assignments_item_data in _role_assignments:
                role_assignments_item = AssignedRoleSchemaOut.from_dict(role_assignments_item_data)

                role_assignments.append(role_assignments_item)

        me_patch_out = cls(
            created=created,
            updated=updated,
            id=id,
            username=username,
            language=language,
            email=email,
            is_timezone_auto_detect=is_timezone_auto_detect,
            current_organization=current_organization,
            first_name=first_name,
            last_name=last_name,
            avatar_url=avatar_url,
            tos_accepted_at=tos_accepted_at,
            role_assignments=role_assignments,
        )

        me_patch_out.additional_properties = d
        return me_patch_out

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
