from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCaptureSectionComponentQuery")


@_attrs_define
class GetCaptureSectionComponentQuery:
    """
    Attributes:
        page_number (list[int] | Unset):
    """

    page_number: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_number: list[int] | Unset = UNSET
        if not isinstance(self.page_number, Unset):
            page_number = self.page_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page_number is not UNSET:
            field_dict["page_number"] = page_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page_number = cast(list[int], d.pop("page_number", UNSET))

        get_capture_section_component_query = cls(
            page_number=page_number,
        )

        get_capture_section_component_query.additional_properties = d
        return get_capture_section_component_query

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
