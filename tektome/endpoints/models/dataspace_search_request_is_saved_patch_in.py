from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DataspaceSearchRequestIsSavedPatchIn")


@_attrs_define
class DataspaceSearchRequestIsSavedPatchIn:
    """For updating is_saved field of a search request

    Attributes:
        is_saved (bool): Whether the search request is saved
    """

    is_saved: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_saved = self.is_saved

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "is_saved": is_saved,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_saved = d.pop("is_saved")

        dataspace_search_request_is_saved_patch_in = cls(
            is_saved=is_saved,
        )

        dataspace_search_request_is_saved_patch_in.additional_properties = d
        return dataspace_search_request_is_saved_patch_in

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
