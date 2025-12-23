from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RequirementItemTemplate")


@_attrs_define
class RequirementItemTemplate:
    """
    Attributes:
        item (list[None | str] | Unset):
    """

    item: list[None | str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item: list[None | str] | Unset = UNSET
        if not isinstance(self.item, Unset):
            item = []
            for item_item_data in self.item:
                item_item: None | str
                item_item = item_item_data
                item.append(item_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item is not UNSET:
            field_dict["Item"] = item

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _item = d.pop("Item", UNSET)
        item: list[None | str] | Unset = UNSET
        if _item is not UNSET:
            item = []
            for item_item_data in _item:

                def _parse_item_item(data: object) -> None | str:
                    if data is None:
                        return data
                    return cast(None | str, data)

                item_item = _parse_item_item(item_item_data)

                item.append(item_item)

        requirement_item_template = cls(
            item=item,
        )

        requirement_item_template.additional_properties = d
        return requirement_item_template

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
