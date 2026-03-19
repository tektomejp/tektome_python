from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BimQueryToKeysValuesResponse")


@_attrs_define
class BimQueryToKeysValuesResponse:
    """Schema for BIM query key-value output response.

    Attributes:
        keys: List of keys extracted from the BIM query result.
        values: List of values extracted from the BIM query result.
        error: Optional error message if the query processing failed, None if successful.

        Attributes:
            error (None | str):
            keys (list[str] | Unset):
            values (list[str] | Unset):
    """

    error: None | str
    keys: list[str] | Unset = UNSET
    values: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error: None | str
        error = self.error

        keys: list[str] | Unset = UNSET
        if not isinstance(self.keys, Unset):
            keys = self.keys

        values: list[str] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
            }
        )
        if keys is not UNSET:
            field_dict["keys"] = keys
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error = _parse_error(d.pop("error"))

        keys = cast(list[str], d.pop("keys", UNSET))

        values = cast(list[str], d.pop("values", UNSET))

        bim_query_to_keys_values_response = cls(
            error=error,
            keys=keys,
            values=values,
        )

        bim_query_to_keys_values_response.additional_properties = d
        return bim_query_to_keys_values_response

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
