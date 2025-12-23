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
    from ..models.approval_entry_schema import ApprovalEntrySchema
    from ..models.lawtalk_reference_note_version_required_schema import LawtalkReferenceNoteVersionRequiredSchema
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="ReferenceNoteVersionGetOut")


@_attrs_define
class ReferenceNoteVersionGetOut:
    """
    Attributes:
        approvals (list[ApprovalEntrySchema]):
        created_by (UserMetadata):
        updated_by (UserMetadata):
        core_attributes (LawtalkReferenceNoteVersionRequiredSchema):
        created (datetime.datetime):
        updated (datetime.datetime):
        requirement_title (str):
        resources (list[str]):
        id (None | Unset | UUID):
        is_active (bool | Unset):  Default: True.
        version (int | Unset):  Default: 1.
        requirement_prompt (None | str | Unset):
        content (None | str | Unset):
        ai_model (None | str | Unset):
        enable_web_search (bool | Unset):  Default: False.
        clarifying_questions (None | str | Unset):
        user_answers (None | str | Unset):
    """

    approvals: list[ApprovalEntrySchema]
    created_by: UserMetadata
    updated_by: UserMetadata
    core_attributes: LawtalkReferenceNoteVersionRequiredSchema
    created: datetime.datetime
    updated: datetime.datetime
    requirement_title: str
    resources: list[str]
    id: None | Unset | UUID = UNSET
    is_active: bool | Unset = True
    version: int | Unset = 1
    requirement_prompt: None | str | Unset = UNSET
    content: None | str | Unset = UNSET
    ai_model: None | str | Unset = UNSET
    enable_web_search: bool | Unset = False
    clarifying_questions: None | str | Unset = UNSET
    user_answers: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        approvals = []
        for approvals_item_data in self.approvals:
            approvals_item = approvals_item_data.to_dict()
            approvals.append(approvals_item)

        created_by = self.created_by.to_dict()

        updated_by = self.updated_by.to_dict()

        core_attributes = self.core_attributes.to_dict()

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        requirement_title = self.requirement_title

        resources = self.resources

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        is_active = self.is_active

        version = self.version

        requirement_prompt: None | str | Unset
        if isinstance(self.requirement_prompt, Unset):
            requirement_prompt = UNSET
        else:
            requirement_prompt = self.requirement_prompt

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        ai_model: None | str | Unset
        if isinstance(self.ai_model, Unset):
            ai_model = UNSET
        else:
            ai_model = self.ai_model

        enable_web_search = self.enable_web_search

        clarifying_questions: None | str | Unset
        if isinstance(self.clarifying_questions, Unset):
            clarifying_questions = UNSET
        else:
            clarifying_questions = self.clarifying_questions

        user_answers: None | str | Unset
        if isinstance(self.user_answers, Unset):
            user_answers = UNSET
        else:
            user_answers = self.user_answers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "approvals": approvals,
                "created_by": created_by,
                "updated_by": updated_by,
                "core_attributes": core_attributes,
                "created": created,
                "updated": updated,
                "requirement_title": requirement_title,
                "resources": resources,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if version is not UNSET:
            field_dict["version"] = version
        if requirement_prompt is not UNSET:
            field_dict["requirement_prompt"] = requirement_prompt
        if content is not UNSET:
            field_dict["content"] = content
        if ai_model is not UNSET:
            field_dict["ai_model"] = ai_model
        if enable_web_search is not UNSET:
            field_dict["enable_web_search"] = enable_web_search
        if clarifying_questions is not UNSET:
            field_dict["clarifying_questions"] = clarifying_questions
        if user_answers is not UNSET:
            field_dict["user_answers"] = user_answers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.approval_entry_schema import ApprovalEntrySchema
        from ..models.lawtalk_reference_note_version_required_schema import LawtalkReferenceNoteVersionRequiredSchema
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)
        approvals = []
        _approvals = d.pop("approvals")
        for approvals_item_data in _approvals:
            approvals_item = ApprovalEntrySchema.from_dict(approvals_item_data)

            approvals.append(approvals_item)

        created_by = UserMetadata.from_dict(d.pop("created_by"))

        updated_by = UserMetadata.from_dict(d.pop("updated_by"))

        core_attributes = LawtalkReferenceNoteVersionRequiredSchema.from_dict(d.pop("core_attributes"))

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        requirement_title = d.pop("requirement_title")

        resources = cast(list[str], d.pop("resources"))

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

        is_active = d.pop("is_active", UNSET)

        version = d.pop("version", UNSET)

        def _parse_requirement_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        requirement_prompt = _parse_requirement_prompt(d.pop("requirement_prompt", UNSET))

        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

        def _parse_ai_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ai_model = _parse_ai_model(d.pop("ai_model", UNSET))

        enable_web_search = d.pop("enable_web_search", UNSET)

        def _parse_clarifying_questions(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        clarifying_questions = _parse_clarifying_questions(d.pop("clarifying_questions", UNSET))

        def _parse_user_answers(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_answers = _parse_user_answers(d.pop("user_answers", UNSET))

        reference_note_version_get_out = cls(
            approvals=approvals,
            created_by=created_by,
            updated_by=updated_by,
            core_attributes=core_attributes,
            created=created,
            updated=updated,
            requirement_title=requirement_title,
            resources=resources,
            id=id,
            is_active=is_active,
            version=version,
            requirement_prompt=requirement_prompt,
            content=content,
            ai_model=ai_model,
            enable_web_search=enable_web_search,
            clarifying_questions=clarifying_questions,
            user_answers=user_answers,
        )

        reference_note_version_get_out.additional_properties = d
        return reference_note_version_get_out

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
