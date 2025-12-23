from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetCitingAttributesGetOut")


@_attrs_define
class GetCitingAttributesGetOut:
    """
    Attributes:
        citing_attribute_ids (list[UUID]): The citing attributes for the resource.
    """

    citing_attribute_ids: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        citing_attribute_ids = []
        for citing_attribute_ids_item_data in self.citing_attribute_ids:
            citing_attribute_ids_item = str(citing_attribute_ids_item_data)
            citing_attribute_ids.append(citing_attribute_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "citing_attribute_ids": citing_attribute_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        citing_attribute_ids = []
        _citing_attribute_ids = d.pop("citing_attribute_ids")
        for citing_attribute_ids_item_data in _citing_attribute_ids:
            citing_attribute_ids_item = UUID(citing_attribute_ids_item_data)

            citing_attribute_ids.append(citing_attribute_ids_item)

        get_citing_attributes_get_out = cls(
            citing_attribute_ids=citing_attribute_ids,
        )

        get_citing_attributes_get_out.additional_properties = d
        return get_citing_attributes_get_out

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
