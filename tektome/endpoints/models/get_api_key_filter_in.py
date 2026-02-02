from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAPIKeyFilterIn")


@_attrs_define
class GetAPIKeyFilterIn:
    """Schema for filtering API keys.

    Attributes:
        include_system (bool | Unset):  Default: False.
        include_expired (bool | Unset):  Default: False.
    """

    include_system: bool | Unset = False
    include_expired: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        include_system = self.include_system

        include_expired = self.include_expired

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if include_system is not UNSET:
            field_dict["include_system"] = include_system
        if include_expired is not UNSET:
            field_dict["include_expired"] = include_expired

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        include_system = d.pop("include_system", UNSET)

        include_expired = d.pop("include_expired", UNSET)

        get_api_key_filter_in = cls(
            include_system=include_system,
            include_expired=include_expired,
        )

        get_api_key_filter_in.additional_properties = d
        return get_api_key_filter_in

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
