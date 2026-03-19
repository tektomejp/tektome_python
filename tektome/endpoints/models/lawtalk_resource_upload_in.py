from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LawtalkResourceUploadIn")


@_attrs_define
class LawtalkResourceUploadIn:
    """
    Attributes:
        initialize (bool | Unset):  Default: True.
    """

    initialize: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        initialize = self.initialize

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if initialize is not UNSET:
            field_dict["initialize"] = initialize

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        initialize = d.pop("initialize", UNSET)

        lawtalk_resource_upload_in = cls(
            initialize=initialize,
        )

        lawtalk_resource_upload_in.additional_properties = d
        return lawtalk_resource_upload_in

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
