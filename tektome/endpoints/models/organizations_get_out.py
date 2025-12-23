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
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="OrganizationsGetOut")


@_attrs_define
class OrganizationsGetOut:
    """
    Attributes:
        created_by (UserMetadata):
        updated_by (UserMetadata):
        created (datetime.datetime):
        updated (datetime.datetime):
        users_count (int | Unset): Number of users in the organization Default: 0.
        dataspaces_count (int | Unset): Number of dataspaces in the organization Default: 0.
        projects_count (int | Unset): Number of projects in the organization Default: 0.
        files_count (int | Unset): Number of files in the organization Default: 0.
        id (None | Unset | UUID):
        name (str | Unset):  Default: ''.
        logo_file (None | str | Unset):
        description (None | str | Unset):  Default: ''.
        timezone (str | Unset): Default timezone for the organization. Default: 'Asia/Tokyo'.
        language (str | Unset): Default language code for the organization. Default: 'en'.
        is_root (bool | Unset): Indicates if this organization is the root organization. Default: False.
    """

    created_by: UserMetadata
    updated_by: UserMetadata
    created: datetime.datetime
    updated: datetime.datetime
    users_count: int | Unset = 0
    dataspaces_count: int | Unset = 0
    projects_count: int | Unset = 0
    files_count: int | Unset = 0
    id: None | Unset | UUID = UNSET
    name: str | Unset = ""
    logo_file: None | str | Unset = UNSET
    description: None | str | Unset = ""
    timezone: str | Unset = "Asia/Tokyo"
    language: str | Unset = "en"
    is_root: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_by = self.created_by.to_dict()

        updated_by = self.updated_by.to_dict()

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        users_count = self.users_count

        dataspaces_count = self.dataspaces_count

        projects_count = self.projects_count

        files_count = self.files_count

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        name = self.name

        logo_file: None | str | Unset
        if isinstance(self.logo_file, Unset):
            logo_file = UNSET
        else:
            logo_file = self.logo_file

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        timezone = self.timezone

        language = self.language

        is_root = self.is_root

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_by": created_by,
                "updated_by": updated_by,
                "created": created,
                "updated": updated,
            }
        )
        if users_count is not UNSET:
            field_dict["users_count"] = users_count
        if dataspaces_count is not UNSET:
            field_dict["dataspaces_count"] = dataspaces_count
        if projects_count is not UNSET:
            field_dict["projects_count"] = projects_count
        if files_count is not UNSET:
            field_dict["files_count"] = files_count
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if logo_file is not UNSET:
            field_dict["logo_file"] = logo_file
        if description is not UNSET:
            field_dict["description"] = description
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if language is not UNSET:
            field_dict["language"] = language
        if is_root is not UNSET:
            field_dict["is_root"] = is_root

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)
        created_by = UserMetadata.from_dict(d.pop("created_by"))

        updated_by = UserMetadata.from_dict(d.pop("updated_by"))

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        users_count = d.pop("users_count", UNSET)

        dataspaces_count = d.pop("dataspaces_count", UNSET)

        projects_count = d.pop("projects_count", UNSET)

        files_count = d.pop("files_count", UNSET)

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

        name = d.pop("name", UNSET)

        def _parse_logo_file(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_file = _parse_logo_file(d.pop("logo_file", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        timezone = d.pop("timezone", UNSET)

        language = d.pop("language", UNSET)

        is_root = d.pop("is_root", UNSET)

        organizations_get_out = cls(
            created_by=created_by,
            updated_by=updated_by,
            created=created,
            updated=updated,
            users_count=users_count,
            dataspaces_count=dataspaces_count,
            projects_count=projects_count,
            files_count=files_count,
            id=id,
            name=name,
            logo_file=logo_file,
            description=description,
            timezone=timezone,
            language=language,
            is_root=is_root,
        )

        organizations_get_out.additional_properties = d
        return organizations_get_out

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
