from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.research_mode_enum import ResearchModeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="RequirementResearchTemplatePostIn")


@_attrs_define
class RequirementResearchTemplatePostIn:
    """Serializer for Requirement Template Research Template Post Input.

    Attributes:
        name (str):
        prompt (str):
        research_mode (ResearchModeEnum): Enum for Research Mode.
        public_resource_groups (list[UUID] | Unset):
        project_specific_resource_groups_keywords (list[str] | Unset):
    """

    name: str
    prompt: str
    research_mode: ResearchModeEnum
    public_resource_groups: list[UUID] | Unset = UNSET
    project_specific_resource_groups_keywords: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        prompt = self.prompt

        research_mode = self.research_mode.value

        public_resource_groups: list[str] | Unset = UNSET
        if not isinstance(self.public_resource_groups, Unset):
            public_resource_groups = []
            for public_resource_groups_item_data in self.public_resource_groups:
                public_resource_groups_item = str(public_resource_groups_item_data)
                public_resource_groups.append(public_resource_groups_item)

        project_specific_resource_groups_keywords: list[str] | Unset = UNSET
        if not isinstance(self.project_specific_resource_groups_keywords, Unset):
            project_specific_resource_groups_keywords = self.project_specific_resource_groups_keywords

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "prompt": prompt,
                "research_mode": research_mode,
            }
        )
        if public_resource_groups is not UNSET:
            field_dict["public_resource_groups"] = public_resource_groups
        if project_specific_resource_groups_keywords is not UNSET:
            field_dict["project_specific_resource_groups_keywords"] = project_specific_resource_groups_keywords

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        prompt = d.pop("prompt")

        research_mode = ResearchModeEnum(d.pop("research_mode"))

        _public_resource_groups = d.pop("public_resource_groups", UNSET)
        public_resource_groups: list[UUID] | Unset = UNSET
        if _public_resource_groups is not UNSET:
            public_resource_groups = []
            for public_resource_groups_item_data in _public_resource_groups:
                public_resource_groups_item = UUID(public_resource_groups_item_data)

                public_resource_groups.append(public_resource_groups_item)

        project_specific_resource_groups_keywords = cast(
            list[str], d.pop("project_specific_resource_groups_keywords", UNSET)
        )

        requirement_research_template_post_in = cls(
            name=name,
            prompt=prompt,
            research_mode=research_mode,
            public_resource_groups=public_resource_groups,
            project_specific_resource_groups_keywords=project_specific_resource_groups_keywords,
        )

        requirement_research_template_post_in.additional_properties = d
        return requirement_research_template_post_in

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
