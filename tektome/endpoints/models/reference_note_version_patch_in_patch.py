from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReferenceNoteVersionPatchInPatch")


@_attrs_define
class ReferenceNoteVersionPatchInPatch:
    """
    Attributes:
        resource_ids (list[UUID] | None | Unset):
        content (None | str | Unset):
        is_active (bool | None | Unset):
        requirement_title (None | str | Unset):
        requirement_prompt (None | str | Unset):
        ai_model (None | str | Unset):
        enable_web_search (bool | None | Unset):
    """

    resource_ids: list[UUID] | None | Unset = UNSET
    content: None | str | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    requirement_title: None | str | Unset = UNSET
    requirement_prompt: None | str | Unset = UNSET
    ai_model: None | str | Unset = UNSET
    enable_web_search: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_ids: list[str] | None | Unset
        if isinstance(self.resource_ids, Unset):
            resource_ids = UNSET
        elif isinstance(self.resource_ids, list):
            resource_ids = []
            for resource_ids_type_0_item_data in self.resource_ids:
                resource_ids_type_0_item = str(resource_ids_type_0_item_data)
                resource_ids.append(resource_ids_type_0_item)

        else:
            resource_ids = self.resource_ids

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        requirement_title: None | str | Unset
        if isinstance(self.requirement_title, Unset):
            requirement_title = UNSET
        else:
            requirement_title = self.requirement_title

        requirement_prompt: None | str | Unset
        if isinstance(self.requirement_prompt, Unset):
            requirement_prompt = UNSET
        else:
            requirement_prompt = self.requirement_prompt

        ai_model: None | str | Unset
        if isinstance(self.ai_model, Unset):
            ai_model = UNSET
        else:
            ai_model = self.ai_model

        enable_web_search: bool | None | Unset
        if isinstance(self.enable_web_search, Unset):
            enable_web_search = UNSET
        else:
            enable_web_search = self.enable_web_search

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_ids is not UNSET:
            field_dict["resource_ids"] = resource_ids
        if content is not UNSET:
            field_dict["content"] = content
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if requirement_title is not UNSET:
            field_dict["requirement_title"] = requirement_title
        if requirement_prompt is not UNSET:
            field_dict["requirement_prompt"] = requirement_prompt
        if ai_model is not UNSET:
            field_dict["ai_model"] = ai_model
        if enable_web_search is not UNSET:
            field_dict["enable_web_search"] = enable_web_search

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_resource_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                resource_ids_type_0 = []
                _resource_ids_type_0 = data
                for resource_ids_type_0_item_data in _resource_ids_type_0:
                    resource_ids_type_0_item = UUID(resource_ids_type_0_item_data)

                    resource_ids_type_0.append(resource_ids_type_0_item)

                return resource_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        resource_ids = _parse_resource_ids(d.pop("resource_ids", UNSET))

        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        def _parse_requirement_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        requirement_title = _parse_requirement_title(d.pop("requirement_title", UNSET))

        def _parse_requirement_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        requirement_prompt = _parse_requirement_prompt(d.pop("requirement_prompt", UNSET))

        def _parse_ai_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ai_model = _parse_ai_model(d.pop("ai_model", UNSET))

        def _parse_enable_web_search(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_web_search = _parse_enable_web_search(d.pop("enable_web_search", UNSET))

        reference_note_version_patch_in_patch = cls(
            resource_ids=resource_ids,
            content=content,
            is_active=is_active,
            requirement_title=requirement_title,
            requirement_prompt=requirement_prompt,
            ai_model=ai_model,
            enable_web_search=enable_web_search,
        )

        reference_note_version_patch_in_patch.additional_properties = d
        return reference_note_version_patch_in_patch

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
