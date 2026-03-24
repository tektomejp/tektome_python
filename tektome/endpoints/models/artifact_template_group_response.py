from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArtifactTemplateGroupResponse")


@_attrs_define
class ArtifactTemplateGroupResponse:
    """
    Attributes:
        template_count (int):
        name (str):
        kind (str):
        created (datetime.datetime):
        updated (datetime.datetime):
        id (None | Unset | UUID):
        description (None | str | Unset):  Default: ''.
        version (str | Unset):  Default: '1.0.0'.
        is_system (bool | Unset):  Default: True.
        is_active (bool | Unset):  Default: True.
        is_default (bool | Unset):  Default: False.
    """

    template_count: int
    name: str
    kind: str
    created: datetime.datetime
    updated: datetime.datetime
    id: None | Unset | UUID = UNSET
    description: None | str | Unset = ""
    version: str | Unset = "1.0.0"
    is_system: bool | Unset = True
    is_active: bool | Unset = True
    is_default: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template_count = self.template_count

        name = self.name

        kind = self.kind

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        version = self.version

        is_system = self.is_system

        is_active = self.is_active

        is_default = self.is_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "template_count": template_count,
                "name": name,
                "kind": kind,
                "created": created,
                "updated": updated,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if version is not UNSET:
            field_dict["version"] = version
        if is_system is not UNSET:
            field_dict["is_system"] = is_system
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_default is not UNSET:
            field_dict["is_default"] = is_default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        template_count = d.pop("template_count")

        name = d.pop("name")

        kind = d.pop("kind")

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

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        version = d.pop("version", UNSET)

        is_system = d.pop("is_system", UNSET)

        is_active = d.pop("is_active", UNSET)

        is_default = d.pop("is_default", UNSET)

        artifact_template_group_response = cls(
            template_count=template_count,
            name=name,
            kind=kind,
            created=created,
            updated=updated,
            id=id,
            description=description,
            version=version,
            is_system=is_system,
            is_active=is_active,
            is_default=is_default,
        )

        artifact_template_group_response.additional_properties = d
        return artifact_template_group_response

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
