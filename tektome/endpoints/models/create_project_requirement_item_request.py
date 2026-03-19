from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.create_project_requirement_item_request_value_item import CreateProjectRequirementItemRequestValueItem


T = TypeVar("T", bound="CreateProjectRequirementItemRequest")


@_attrs_define
class CreateProjectRequirementItemRequest:
    """
    Attributes:
        nonce (int):
        value (list[CreateProjectRequirementItemRequestValueItem]):
    """

    nonce: int
    value: list[CreateProjectRequirementItemRequestValueItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nonce = self.nonce

        value = []
        for value_item_data in self.value:
            value_item = value_item_data.to_dict()
            value.append(value_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nonce": nonce,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_project_requirement_item_request_value_item import (
            CreateProjectRequirementItemRequestValueItem,
        )

        d = dict(src_dict)
        nonce = d.pop("nonce")

        value = []
        _value = d.pop("value")
        for value_item_data in _value:
            value_item = CreateProjectRequirementItemRequestValueItem.from_dict(value_item_data)

            value.append(value_item)

        create_project_requirement_item_request = cls(
            nonce=nonce,
            value=value,
        )

        create_project_requirement_item_request.additional_properties = d
        return create_project_requirement_item_request

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
