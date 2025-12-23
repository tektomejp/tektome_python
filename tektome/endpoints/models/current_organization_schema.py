from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CurrentOrganizationSchema")


@_attrs_define
class CurrentOrganizationSchema:
    """
    Attributes:
        created (datetime.datetime):
        updated (datetime.datetime):
        id (None | Unset | UUID):
        created_by (None | Unset | UUID):
        updated_by (None | Unset | UUID):
        name (str | Unset):  Default: ''.
        logo_file (None | str | Unset):
        description (None | str | Unset):  Default: ''.
        timezone (str | Unset): Default timezone for the organization. Default: 'Asia/Tokyo'.
        language (str | Unset): Default language code for the organization. Default: 'en'.
        is_root (bool | Unset): Indicates if this organization is the root organization. Default: False.
    """

    created: datetime.datetime
    updated: datetime.datetime
    id: None | Unset | UUID = UNSET
    created_by: None | Unset | UUID = UNSET
    updated_by: None | Unset | UUID = UNSET
    name: str | Unset = ""
    logo_file: None | str | Unset = UNSET
    description: None | str | Unset = ""
    timezone: str | Unset = "Asia/Tokyo"
    language: str | Unset = "en"
    is_root: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created.isoformat()

        updated = self.updated.isoformat()

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        elif isinstance(self.created_by, UUID):
            created_by = str(self.created_by)
        else:
            created_by = self.created_by

        updated_by: None | str | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        elif isinstance(self.updated_by, UUID):
            updated_by = str(self.updated_by)
        else:
            updated_by = self.updated_by

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
                "created": created,
                "updated": updated,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by
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
        d = dict(src_dict)
        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

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

        def _parse_created_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_type_0 = UUID(data)

                return created_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_updated_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_by_type_0 = UUID(data)

                return updated_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))

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

        current_organization_schema = cls(
            created=created,
            updated=updated,
            id=id,
            created_by=created_by,
            updated_by=updated_by,
            name=name,
            logo_file=logo_file,
            description=description,
            timezone=timezone,
            language=language,
            is_root=is_root,
        )

        current_organization_schema.additional_properties = d
        return current_organization_schema

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
