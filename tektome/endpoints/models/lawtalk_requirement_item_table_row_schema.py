from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LawtalkRequirementItemTableRowSchema")


@_attrs_define
class LawtalkRequirementItemTableRowSchema:
    """
    Attributes:
        item (str | Unset): Name of Item/part/point of views of requirement Default: ''.
        requirements (str | Unset): The requirements/values/specs related to the item Default: ''.
        reasons (str | Unset): The reasons related project attributes to explain why you decide the requirements.
            Default: ''.
        reference (str | Unset): The reference for the requirement item Default: ''.
    """

    item: str | Unset = ""
    requirements: str | Unset = ""
    reasons: str | Unset = ""
    reference: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item = self.item

        requirements = self.requirements

        reasons = self.reasons

        reference = self.reference

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item is not UNSET:
            field_dict["item"] = item
        if requirements is not UNSET:
            field_dict["requirements"] = requirements
        if reasons is not UNSET:
            field_dict["reasons"] = reasons
        if reference is not UNSET:
            field_dict["reference"] = reference

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item = d.pop("item", UNSET)

        requirements = d.pop("requirements", UNSET)

        reasons = d.pop("reasons", UNSET)

        reference = d.pop("reference", UNSET)

        lawtalk_requirement_item_table_row_schema = cls(
            item=item,
            requirements=requirements,
            reasons=reasons,
            reference=reference,
        )

        lawtalk_requirement_item_table_row_schema.additional_properties = d
        return lawtalk_requirement_item_table_row_schema

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
