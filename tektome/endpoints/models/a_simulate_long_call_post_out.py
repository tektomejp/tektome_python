from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ASimulateLongCallPostOut")


@_attrs_define
class ASimulateLongCallPostOut:
    """For demonstration purpose, this should be in /serializers/<same_name_as_this_file>.py

    Attributes:
        sync_delay (float):
        async_delay (float):
    """

    sync_delay: float
    async_delay: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sync_delay = self.sync_delay

        async_delay = self.async_delay

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sync_delay": sync_delay,
                "async_delay": async_delay,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sync_delay = d.pop("sync_delay")

        async_delay = d.pop("async_delay")

        a_simulate_long_call_post_out = cls(
            sync_delay=sync_delay,
            async_delay=async_delay,
        )

        a_simulate_long_call_post_out.additional_properties = d
        return a_simulate_long_call_post_out

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
