from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAPIKeyPostOut")


@_attrs_define
class CreateAPIKeyPostOut:
    """Schema for retrieving a list of API keys.

    Attributes:
        created (datetime.datetime):
        updated (datetime.datetime):
        expires_at (datetime.datetime):
        id (None | Unset | UUID):
        name (None | str | Unset):  Default: ''.
        key (str | Unset):
        scopes (list[Any] | Unset):
        is_system (bool | Unset):  Default: False.
    """

    created: datetime.datetime
    updated: datetime.datetime
    expires_at: datetime.datetime
    id: None | Unset | UUID = UNSET
    name: None | str | Unset = ""
    key: str | Unset = UNSET
    scopes: list[Any] | Unset = UNSET
    is_system: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created.isoformat()

        updated = self.updated.isoformat()

        expires_at = self.expires_at.isoformat()

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        key = self.key

        scopes: list[Any] | Unset = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = self.scopes

        is_system = self.is_system

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "updated": updated,
                "expires_at": expires_at,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if key is not UNSET:
            field_dict["key"] = key
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if is_system is not UNSET:
            field_dict["is_system"] = is_system

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        expires_at = isoparse(d.pop("expires_at"))

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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        key = d.pop("key", UNSET)

        scopes = cast(list[Any], d.pop("scopes", UNSET))

        is_system = d.pop("is_system", UNSET)

        create_api_key_post_out = cls(
            created=created,
            updated=updated,
            expires_at=expires_at,
            id=id,
            name=name,
            key=key,
            scopes=scopes,
            is_system=is_system,
        )

        create_api_key_post_out.additional_properties = d
        return create_api_key_post_out

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
