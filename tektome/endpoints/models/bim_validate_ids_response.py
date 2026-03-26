from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BimValidateIdsResponse")


@_attrs_define
class BimValidateIdsResponse:
    """Schema for batch element ID validation result.
    Returns the subset of input IDs that exist in the index.

        Attributes:
            existing_ids (list[str]): Element IDs that were found in the index
    """

    existing_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        existing_ids = self.existing_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "existing_ids": existing_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        existing_ids = cast(list[str], d.pop("existing_ids"))

        bim_validate_ids_response = cls(
            existing_ids=existing_ids,
        )

        bim_validate_ids_response.additional_properties = d
        return bim_validate_ids_response

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
