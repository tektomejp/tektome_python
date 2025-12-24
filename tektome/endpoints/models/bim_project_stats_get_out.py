from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BimProjectStatsGetOut")


@_attrs_define
class BimProjectStatsGetOut:
    """Schema for BIM project statistics response.

    Attributes:
        id (UUID):
        name (str):
        created_at (datetime.datetime):
        modified_at (datetime.datetime):
        bim_objects_count (int | Unset):  Default: 0.
        bim_views_count (int | Unset):  Default: 0.
        bim_sheets_count (int | Unset):  Default: 0.
        resource_id (None | Unset | UUID):
    """

    id: UUID
    name: str
    created_at: datetime.datetime
    modified_at: datetime.datetime
    bim_objects_count: int | Unset = 0
    bim_views_count: int | Unset = 0
    bim_sheets_count: int | Unset = 0
    resource_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        created_at = self.created_at.isoformat()

        modified_at = self.modified_at.isoformat()

        bim_objects_count = self.bim_objects_count

        bim_views_count = self.bim_views_count

        bim_sheets_count = self.bim_sheets_count

        resource_id: None | str | Unset
        if isinstance(self.resource_id, Unset):
            resource_id = UNSET
        elif isinstance(self.resource_id, UUID):
            resource_id = str(self.resource_id)
        else:
            resource_id = self.resource_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "created_at": created_at,
                "modified_at": modified_at,
            }
        )
        if bim_objects_count is not UNSET:
            field_dict["bim_objects_count"] = bim_objects_count
        if bim_views_count is not UNSET:
            field_dict["bim_views_count"] = bim_views_count
        if bim_sheets_count is not UNSET:
            field_dict["bim_sheets_count"] = bim_sheets_count
        if resource_id is not UNSET:
            field_dict["resource_id"] = resource_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        created_at = isoparse(d.pop("created_at"))

        modified_at = isoparse(d.pop("modified_at"))

        bim_objects_count = d.pop("bim_objects_count", UNSET)

        bim_views_count = d.pop("bim_views_count", UNSET)

        bim_sheets_count = d.pop("bim_sheets_count", UNSET)

        def _parse_resource_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resource_id_type_0 = UUID(data)

                return resource_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        resource_id = _parse_resource_id(d.pop("resource_id", UNSET))

        bim_project_stats_get_out = cls(
            id=id,
            name=name,
            created_at=created_at,
            modified_at=modified_at,
            bim_objects_count=bim_objects_count,
            bim_views_count=bim_views_count,
            bim_sheets_count=bim_sheets_count,
            resource_id=resource_id,
        )

        bim_project_stats_get_out.additional_properties = d
        return bim_project_stats_get_out

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
