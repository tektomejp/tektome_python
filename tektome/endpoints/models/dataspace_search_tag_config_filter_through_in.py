from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataspaceSearchTagConfigFilterThroughIn")


@_attrs_define
class DataspaceSearchTagConfigFilterThroughIn:
    """Schema for assigning a filter with default search conditions to a tag config.

    Attributes:
        filter_id (UUID):
        default_operator (None | str | Unset):
        default_value (None | str | Unset):
    """

    filter_id: UUID
    default_operator: None | str | Unset = UNSET
    default_value: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_id = str(self.filter_id)

        default_operator: None | str | Unset
        if isinstance(self.default_operator, Unset):
            default_operator = UNSET
        else:
            default_operator = self.default_operator

        default_value: None | str | Unset
        if isinstance(self.default_value, Unset):
            default_value = UNSET
        else:
            default_value = self.default_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filter_id": filter_id,
            }
        )
        if default_operator is not UNSET:
            field_dict["default_operator"] = default_operator
        if default_value is not UNSET:
            field_dict["default_value"] = default_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filter_id = UUID(d.pop("filter_id"))

        def _parse_default_operator(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_operator = _parse_default_operator(d.pop("default_operator", UNSET))

        def _parse_default_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_value = _parse_default_value(d.pop("default_value", UNSET))

        dataspace_search_tag_config_filter_through_in = cls(
            filter_id=filter_id,
            default_operator=default_operator,
            default_value=default_value,
        )

        dataspace_search_tag_config_filter_through_in.additional_properties = d
        return dataspace_search_tag_config_filter_through_in

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
