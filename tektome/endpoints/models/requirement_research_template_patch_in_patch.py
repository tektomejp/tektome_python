from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RequirementResearchTemplatePatchInPatch")


@_attrs_define
class RequirementResearchTemplatePatchInPatch:
    """
    Attributes:
        name (None | str | Unset):
        prompt (None | str | Unset):
        public_resource_groups (list[UUID] | None | Unset):
        project_specific_resource_groups_keywords (list[str] | None | Unset):
        output_format_prompt (None | str | Unset):
    """

    name: None | str | Unset = UNSET
    prompt: None | str | Unset = UNSET
    public_resource_groups: list[UUID] | None | Unset = UNSET
    project_specific_resource_groups_keywords: list[str] | None | Unset = UNSET
    output_format_prompt: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        prompt: None | str | Unset
        if isinstance(self.prompt, Unset):
            prompt = UNSET
        else:
            prompt = self.prompt

        public_resource_groups: list[str] | None | Unset
        if isinstance(self.public_resource_groups, Unset):
            public_resource_groups = UNSET
        elif isinstance(self.public_resource_groups, list):
            public_resource_groups = []
            for public_resource_groups_type_0_item_data in self.public_resource_groups:
                public_resource_groups_type_0_item = str(public_resource_groups_type_0_item_data)
                public_resource_groups.append(public_resource_groups_type_0_item)

        else:
            public_resource_groups = self.public_resource_groups

        project_specific_resource_groups_keywords: list[str] | None | Unset
        if isinstance(self.project_specific_resource_groups_keywords, Unset):
            project_specific_resource_groups_keywords = UNSET
        elif isinstance(self.project_specific_resource_groups_keywords, list):
            project_specific_resource_groups_keywords = self.project_specific_resource_groups_keywords

        else:
            project_specific_resource_groups_keywords = self.project_specific_resource_groups_keywords

        output_format_prompt: None | str | Unset
        if isinstance(self.output_format_prompt, Unset):
            output_format_prompt = UNSET
        else:
            output_format_prompt = self.output_format_prompt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if public_resource_groups is not UNSET:
            field_dict["public_resource_groups"] = public_resource_groups
        if project_specific_resource_groups_keywords is not UNSET:
            field_dict["project_specific_resource_groups_keywords"] = project_specific_resource_groups_keywords
        if output_format_prompt is not UNSET:
            field_dict["output_format_prompt"] = output_format_prompt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prompt = _parse_prompt(d.pop("prompt", UNSET))

        def _parse_public_resource_groups(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                public_resource_groups_type_0 = []
                _public_resource_groups_type_0 = data
                for public_resource_groups_type_0_item_data in _public_resource_groups_type_0:
                    public_resource_groups_type_0_item = UUID(public_resource_groups_type_0_item_data)

                    public_resource_groups_type_0.append(public_resource_groups_type_0_item)

                return public_resource_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        public_resource_groups = _parse_public_resource_groups(d.pop("public_resource_groups", UNSET))

        def _parse_project_specific_resource_groups_keywords(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                project_specific_resource_groups_keywords_type_0 = cast(list[str], data)

                return project_specific_resource_groups_keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        project_specific_resource_groups_keywords = _parse_project_specific_resource_groups_keywords(
            d.pop("project_specific_resource_groups_keywords", UNSET)
        )

        def _parse_output_format_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        output_format_prompt = _parse_output_format_prompt(d.pop("output_format_prompt", UNSET))

        requirement_research_template_patch_in_patch = cls(
            name=name,
            prompt=prompt,
            public_resource_groups=public_resource_groups,
            project_specific_resource_groups_keywords=project_specific_resource_groups_keywords,
            output_format_prompt=output_format_prompt,
        )

        requirement_research_template_patch_in_patch.additional_properties = d
        return requirement_research_template_patch_in_patch

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
