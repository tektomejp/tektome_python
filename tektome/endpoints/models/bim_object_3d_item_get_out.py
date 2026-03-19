from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.tekton_instance import TektonInstance


T = TypeVar("T", bound="BimObject3DItemGetOut")


@_attrs_define
class BimObject3DItemGetOut:
    """Schema for a BIM object with 3D data.

    Attributes:
        id (str):
        created (datetime.datetime):
        updated (datetime.datetime):
        instances (list[TektonInstance]):
    """

    id: str
    created: datetime.datetime
    updated: datetime.datetime
    instances: list[TektonInstance]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        instances = []
        for instances_item_data in self.instances:
            instances_item = instances_item_data.to_dict()
            instances.append(instances_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created": created,
                "updated": updated,
                "instances": instances,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tekton_instance import TektonInstance

        d = dict(src_dict)
        id = d.pop("id")

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        instances = []
        _instances = d.pop("instances")
        for instances_item_data in _instances:
            instances_item = TektonInstance.from_dict(instances_item_data)

            instances.append(instances_item)

        bim_object_3d_item_get_out = cls(
            id=id,
            created=created,
            updated=updated,
            instances=instances,
        )

        bim_object_3d_item_get_out.additional_properties = d
        return bim_object_3d_item_get_out

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
