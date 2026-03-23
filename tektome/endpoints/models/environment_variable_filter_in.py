from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnvironmentVariableFilterIn")


@_attrs_define
class EnvironmentVariableFilterIn:
    """Filter schema for querying environment variables.

    Attributes:
        keys (list[str] | None | Unset):
    """

    keys: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keys: list[str] | None | Unset
        if isinstance(self.keys, Unset):
            keys = UNSET
        elif isinstance(self.keys, list):
            keys = self.keys

        else:
            keys = self.keys

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keys is not UNSET:
            field_dict["keys"] = keys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_keys(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keys_type_0 = cast(list[str], data)

                return keys_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        keys = _parse_keys(d.pop("keys", UNSET))

        environment_variable_filter_in = cls(
            keys=keys,
        )

        environment_variable_filter_in.additional_properties = d
        return environment_variable_filter_in

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
