from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BimViewObjectLinkPostOut")


@_attrs_define
class BimViewObjectLinkPostOut:
    """Response schema for linking BIM views with objects.

    Attributes:
        process_ids (list[str] | Unset):
    """

    process_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        process_ids: list[str] | Unset = UNSET
        if not isinstance(self.process_ids, Unset):
            process_ids = self.process_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if process_ids is not UNSET:
            field_dict["process_ids"] = process_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        process_ids = cast(list[str], d.pop("process_ids", UNSET))

        bim_view_object_link_post_out = cls(
            process_ids=process_ids,
        )

        bim_view_object_link_post_out.additional_properties = d
        return bim_view_object_link_post_out

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
