from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BimTrimQueryItem")


@_attrs_define
class BimTrimQueryItem:
    """
    Attributes:
        fields (list[str]): List of fields to include in the trim query result
        any_level (bool | Unset): Whether to search at any level of nesting Default: False.
        max_depth (int | Unset): Maximum depth to traverse for nested fields Default: 10.
    """

    fields: list[str]
    any_level: bool | Unset = False
    max_depth: int | Unset = 10
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fields = self.fields

        any_level = self.any_level

        max_depth = self.max_depth

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fields": fields,
            }
        )
        if any_level is not UNSET:
            field_dict["any_level"] = any_level
        if max_depth is not UNSET:
            field_dict["max_depth"] = max_depth

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fields = cast(list[str], d.pop("fields"))

        any_level = d.pop("any_level", UNSET)

        max_depth = d.pop("max_depth", UNSET)

        bim_trim_query_item = cls(
            fields=fields,
            any_level=any_level,
            max_depth=max_depth,
        )

        bim_trim_query_item.additional_properties = d
        return bim_trim_query_item

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
