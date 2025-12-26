from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.requirement_research_template_get_out_project_specific_resource_groups_keywords import (
        RequirementResearchTemplateGetOutProjectSpecificResourceGroupsKeywords,
    )
    from ..models.research_template_resources_out import ResearchTemplateResourcesOut
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="RequirementResearchTemplateGetOut")


@_attrs_define
class RequirementResearchTemplateGetOut:
    """
    Attributes:
        public_resource_groups (list[ResearchTemplateResourcesOut]):
        created_by (UserMetadata):
        updated_by (UserMetadata):
        name (str):
        research_mode (str):
        created (datetime.datetime):
        updated (datetime.datetime):
        id (None | Unset | UUID):
        prompt (None | str | Unset):
        project_specific_resource_groups_keywords
            (RequirementResearchTemplateGetOutProjectSpecificResourceGroupsKeywords | Unset):
    """

    public_resource_groups: list[ResearchTemplateResourcesOut]
    created_by: UserMetadata
    updated_by: UserMetadata
    name: str
    research_mode: str
    created: datetime.datetime
    updated: datetime.datetime
    id: None | Unset | UUID = UNSET
    prompt: None | str | Unset = UNSET
    project_specific_resource_groups_keywords: (
        RequirementResearchTemplateGetOutProjectSpecificResourceGroupsKeywords | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_resource_groups = []
        for public_resource_groups_item_data in self.public_resource_groups:
            public_resource_groups_item = public_resource_groups_item_data.to_dict()
            public_resource_groups.append(public_resource_groups_item)

        created_by = self.created_by.to_dict()

        updated_by = self.updated_by.to_dict()

        name = self.name

        research_mode = self.research_mode

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        prompt: None | str | Unset
        if isinstance(self.prompt, Unset):
            prompt = UNSET
        else:
            prompt = self.prompt

        project_specific_resource_groups_keywords: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_specific_resource_groups_keywords, Unset):
            project_specific_resource_groups_keywords = self.project_specific_resource_groups_keywords.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "public_resource_groups": public_resource_groups,
                "created_by": created_by,
                "updated_by": updated_by,
                "name": name,
                "research_mode": research_mode,
                "created": created,
                "updated": updated,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if project_specific_resource_groups_keywords is not UNSET:
            field_dict["project_specific_resource_groups_keywords"] = project_specific_resource_groups_keywords

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.requirement_research_template_get_out_project_specific_resource_groups_keywords import (
            RequirementResearchTemplateGetOutProjectSpecificResourceGroupsKeywords,
        )
        from ..models.research_template_resources_out import ResearchTemplateResourcesOut
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)
        public_resource_groups = []
        _public_resource_groups = d.pop("public_resource_groups")
        for public_resource_groups_item_data in _public_resource_groups:
            public_resource_groups_item = ResearchTemplateResourcesOut.from_dict(public_resource_groups_item_data)

            public_resource_groups.append(public_resource_groups_item)

        created_by = UserMetadata.from_dict(d.pop("created_by"))

        updated_by = UserMetadata.from_dict(d.pop("updated_by"))

        name = d.pop("name")

        research_mode = d.pop("research_mode")

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prompt = _parse_prompt(d.pop("prompt", UNSET))

        _project_specific_resource_groups_keywords = d.pop("project_specific_resource_groups_keywords", UNSET)
        project_specific_resource_groups_keywords: (
            RequirementResearchTemplateGetOutProjectSpecificResourceGroupsKeywords | Unset
        )
        if isinstance(_project_specific_resource_groups_keywords, Unset):
            project_specific_resource_groups_keywords = UNSET
        else:
            project_specific_resource_groups_keywords = (
                RequirementResearchTemplateGetOutProjectSpecificResourceGroupsKeywords.from_dict(
                    _project_specific_resource_groups_keywords
                )
            )

        requirement_research_template_get_out = cls(
            public_resource_groups=public_resource_groups,
            created_by=created_by,
            updated_by=updated_by,
            name=name,
            research_mode=research_mode,
            created=created,
            updated=updated,
            id=id,
            prompt=prompt,
            project_specific_resource_groups_keywords=project_specific_resource_groups_keywords,
        )

        requirement_research_template_get_out.additional_properties = d
        return requirement_research_template_get_out

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
