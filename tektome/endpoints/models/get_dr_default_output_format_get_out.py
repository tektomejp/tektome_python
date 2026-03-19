from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetDRDefaultOutputFormatGetOut")


@_attrs_define
class GetDRDefaultOutputFormatGetOut:
    """
    Attributes:
        dr_default_output_format (str): The default output format for Deep Research. Empty string if not set.
    """

    dr_default_output_format: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dr_default_output_format = self.dr_default_output_format

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dr_default_output_format": dr_default_output_format,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dr_default_output_format = d.pop("dr_default_output_format")

        get_dr_default_output_format_get_out = cls(
            dr_default_output_format=dr_default_output_format,
        )

        get_dr_default_output_format_get_out.additional_properties = d
        return get_dr_default_output_format_get_out

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
