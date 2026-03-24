from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateRequirementViewResearchTemplateRequest")


@_attrs_define
class UpdateRequirementViewResearchTemplateRequest:
    """Schema for updating a Requirement Research Template.

    Attributes:
        is_visible (bool | Unset): Indicates if the research template is visible. Default: True.
    """

    is_visible: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_visible = self.is_visible

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_visible is not UNSET:
            field_dict["is_visible"] = is_visible

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_visible = d.pop("is_visible", UNSET)

        update_requirement_view_research_template_request = cls(
            is_visible=is_visible,
        )

        update_requirement_view_research_template_request.additional_properties = d
        return update_requirement_view_research_template_request

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
