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
    from ..models.dataspace_search_filter_field_out import DataspaceSearchFilterFieldOut
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="DataspaceSearchFilterConfigurationOut")


@_attrs_define
class DataspaceSearchFilterConfigurationOut:
    """Schema for the response of posting resource file attributes to a project in a dataspace.

    Attributes:
        created_by (UserMetadata):
        updated_by (UserMetadata):
        fields (list[DataspaceSearchFilterFieldOut]):
        name (str):
        created (datetime.datetime):
        updated (datetime.datetime):
        id (None | Unset | UUID):
        description (None | str | Unset):
        is_active (bool | Unset):  Default: False.
    """

    created_by: UserMetadata
    updated_by: UserMetadata
    fields: list[DataspaceSearchFilterFieldOut]
    name: str
    created: datetime.datetime
    updated: datetime.datetime
    id: None | Unset | UUID = UNSET
    description: None | str | Unset = UNSET
    is_active: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_by = self.created_by.to_dict()

        updated_by = self.updated_by.to_dict()

        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()
            fields.append(fields_item)

        name = self.name

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

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_by": created_by,
                "updated_by": updated_by,
                "fields": fields,
                "name": name,
                "created": created,
                "updated": updated,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataspace_search_filter_field_out import DataspaceSearchFilterFieldOut
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)
        created_by = UserMetadata.from_dict(d.pop("created_by"))

        updated_by = UserMetadata.from_dict(d.pop("updated_by"))

        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:
            fields_item = DataspaceSearchFilterFieldOut.from_dict(fields_item_data)

            fields.append(fields_item)

        name = d.pop("name")

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

        is_active = d.pop("is_active", UNSET)

        dataspace_search_filter_configuration_out = cls(
            created_by=created_by,
            updated_by=updated_by,
            fields=fields,
            name=name,
            created=created,
            updated=updated,
            id=id,
            description=description,
            is_active=is_active,
        )

        dataspace_search_filter_configuration_out.additional_properties = d
        return dataspace_search_filter_configuration_out

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
