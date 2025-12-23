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


T = TypeVar("T", bound="DataspaceResourceFileAttributeSchemaOut")


@_attrs_define
class DataspaceResourceFileAttributeSchemaOut:
    """Schema for the response of resource file attributes to a project in a dataspace.

    Attributes:
        created_by (UserMetadata):
        updated_by (UserMetadata):
        attribute_name (str):
        attribute_type (str):
        index (int):
        created (datetime.datetime):
        updated (datetime.datetime):
        id (None | Unset | UUID):
        attribute_label (str | Unset):  Default: ''.
        description (None | str | Unset):  Default: ''.
        enabled (bool | Unset):  Default: True.
        hidden (bool | Unset):  Default: False.
    """

    created_by: UserMetadata
    updated_by: UserMetadata
    attribute_name: str
    attribute_type: str
    index: int
    created: datetime.datetime
    updated: datetime.datetime
    id: None | Unset | UUID = UNSET
    attribute_label: str | Unset = ""
    description: None | str | Unset = ""
    enabled: bool | Unset = True
    hidden: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_by = self.created_by.to_dict()

        updated_by = self.updated_by.to_dict()

        attribute_name = self.attribute_name

        attribute_type = self.attribute_type

        index = self.index

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        attribute_label = self.attribute_label

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        enabled = self.enabled

        hidden = self.hidden

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_by": created_by,
                "updated_by": updated_by,
                "attribute_name": attribute_name,
                "attribute_type": attribute_type,
                "index": index,
                "created": created,
                "updated": updated,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if attribute_label is not UNSET:
            field_dict["attribute_label"] = attribute_label
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if hidden is not UNSET:
            field_dict["hidden"] = hidden

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)
        created_by = UserMetadata.from_dict(d.pop("created_by"))

        updated_by = UserMetadata.from_dict(d.pop("updated_by"))

        attribute_name = d.pop("attribute_name")

        attribute_type = d.pop("attribute_type")

        index = d.pop("index")

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

        attribute_label = d.pop("attribute_label", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        enabled = d.pop("enabled", UNSET)

        hidden = d.pop("hidden", UNSET)

        dataspace_resource_file_attribute_schema_out = cls(
            created_by=created_by,
            updated_by=updated_by,
            attribute_name=attribute_name,
            attribute_type=attribute_type,
            index=index,
            created=created,
            updated=updated,
            id=id,
            attribute_label=attribute_label,
            description=description,
            enabled=enabled,
            hidden=hidden,
        )

        dataspace_resource_file_attribute_schema_out.additional_properties = d
        return dataspace_resource_file_attribute_schema_out

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
