from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ImproveUserPromptQueryIn")


@_attrs_define
class ImproveUserPromptQueryIn:
    """Serializer for improving user prompt query.

    Attributes:
        user_prompt (str): User prompt to improve
        project_id (UUID):
        requirement_title (str):
        web_search_enabled (bool):
    """

    user_prompt: str
    project_id: UUID
    requirement_title: str
    web_search_enabled: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_prompt = self.user_prompt

        project_id = str(self.project_id)

        requirement_title = self.requirement_title

        web_search_enabled = self.web_search_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_prompt": user_prompt,
                "project_id": project_id,
                "requirement_title": requirement_title,
                "web_search_enabled": web_search_enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_prompt = d.pop("user_prompt")

        project_id = UUID(d.pop("project_id"))

        requirement_title = d.pop("requirement_title")

        web_search_enabled = d.pop("web_search_enabled")

        improve_user_prompt_query_in = cls(
            user_prompt=user_prompt,
            project_id=project_id,
            requirement_title=requirement_title,
            web_search_enabled=web_search_enabled,
        )

        improve_user_prompt_query_in.additional_properties = d
        return improve_user_prompt_query_in

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
