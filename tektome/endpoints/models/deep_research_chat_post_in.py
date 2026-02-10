from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deep_research_models_type import DeepResearchModelsType
from ..models.recipeschoices import RECIPESCHOICES
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeepResearchChatPostIn")


@_attrs_define
class DeepResearchChatPostIn:
    """Serializer for posting a deep research chat message.

    Attributes:
        prompt (str): User's message to the chat
        recipe (RECIPESCHOICES):
        requirement_id (UUID):
        model (DeepResearchModelsType):
        resource_ids (list[UUID]): List of lawtalk Resource IDs to use for research
        chatroom_id (None | Unset | UUID):
        enable_web_search (bool | Unset): Enable web search for the deep research Default: False.
        reference_note_id (None | Unset | UUID): Existing reference note ID to create new version for
        clarifying_questions (None | str | Unset): Clarifying questions from the user to improve the research
        user_answers (None | str | Unset): User answers to the clarifying questions
        auto_generate_specs (bool | Unset): Auto-generate specification table after the DR process Default: False.
        output_format_prompt (None | str | Unset): Custom output format prompt for the deep research model. If not
            provided, a default format will be used.
        deep_research_uses_ocr (bool | Unset):
            Flag indicating whether OCR-extracted text from resources should be used in the deep research, as opposed to the
            PDFs themselves.
            Defaults to True.
            Using OCR text reduces the analysis time by around half, and handles raster PDFs.
            It is recommended, but PDF analysis is provided for backwards compatibility with existing workflows.
             Default: True.
        ocr_deep_research_uses_prefilter (bool | Unset): Flag indicating whether to use prefiltering for OCR deep
            research. Default: True.
    """

    prompt: str
    recipe: RECIPESCHOICES
    requirement_id: UUID
    model: DeepResearchModelsType
    resource_ids: list[UUID]
    chatroom_id: None | Unset | UUID = UNSET
    enable_web_search: bool | Unset = False
    reference_note_id: None | Unset | UUID = UNSET
    clarifying_questions: None | str | Unset = UNSET
    user_answers: None | str | Unset = UNSET
    auto_generate_specs: bool | Unset = False
    output_format_prompt: None | str | Unset = UNSET
    deep_research_uses_ocr: bool | Unset = True
    ocr_deep_research_uses_prefilter: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prompt = self.prompt

        recipe = self.recipe.value

        requirement_id = str(self.requirement_id)

        model = self.model.value

        resource_ids = []
        for resource_ids_item_data in self.resource_ids:
            resource_ids_item = str(resource_ids_item_data)
            resource_ids.append(resource_ids_item)

        chatroom_id: None | str | Unset
        if isinstance(self.chatroom_id, Unset):
            chatroom_id = UNSET
        elif isinstance(self.chatroom_id, UUID):
            chatroom_id = str(self.chatroom_id)
        else:
            chatroom_id = self.chatroom_id

        enable_web_search = self.enable_web_search

        reference_note_id: None | str | Unset
        if isinstance(self.reference_note_id, Unset):
            reference_note_id = UNSET
        elif isinstance(self.reference_note_id, UUID):
            reference_note_id = str(self.reference_note_id)
        else:
            reference_note_id = self.reference_note_id

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

        auto_generate_specs = self.auto_generate_specs

        output_format_prompt: None | str | Unset
        if isinstance(self.output_format_prompt, Unset):
            output_format_prompt = UNSET
        else:
            output_format_prompt = self.output_format_prompt

        deep_research_uses_ocr = self.deep_research_uses_ocr

        ocr_deep_research_uses_prefilter = self.ocr_deep_research_uses_prefilter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prompt": prompt,
                "recipe": recipe,
                "requirement_id": requirement_id,
                "model": model,
                "resource_ids": resource_ids,
            }
        )
        if chatroom_id is not UNSET:
            field_dict["chatroom_id"] = chatroom_id
        if enable_web_search is not UNSET:
            field_dict["enable_web_search"] = enable_web_search
        if reference_note_id is not UNSET:
            field_dict["reference_note_id"] = reference_note_id
        if clarifying_questions is not UNSET:
            field_dict["clarifying_questions"] = clarifying_questions
        if user_answers is not UNSET:
            field_dict["user_answers"] = user_answers
        if auto_generate_specs is not UNSET:
            field_dict["auto_generate_specs"] = auto_generate_specs
        if output_format_prompt is not UNSET:
            field_dict["output_format_prompt"] = output_format_prompt
        if deep_research_uses_ocr is not UNSET:
            field_dict["deep_research_uses_ocr"] = deep_research_uses_ocr
        if ocr_deep_research_uses_prefilter is not UNSET:
            field_dict["ocr_deep_research_uses_prefilter"] = ocr_deep_research_uses_prefilter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        prompt = d.pop("prompt")

        recipe = RECIPESCHOICES(d.pop("recipe"))

        requirement_id = UUID(d.pop("requirement_id"))

        model = DeepResearchModelsType(d.pop("model"))

        resource_ids = []
        _resource_ids = d.pop("resource_ids")
        for resource_ids_item_data in _resource_ids:
            resource_ids_item = UUID(resource_ids_item_data)

            resource_ids.append(resource_ids_item)

        def _parse_chatroom_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                chatroom_id_type_0 = UUID(data)

                return chatroom_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        chatroom_id = _parse_chatroom_id(d.pop("chatroom_id", UNSET))

        enable_web_search = d.pop("enable_web_search", UNSET)

        def _parse_reference_note_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reference_note_id_type_0 = UUID(data)

                return reference_note_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        reference_note_id = _parse_reference_note_id(d.pop("reference_note_id", UNSET))

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

        auto_generate_specs = d.pop("auto_generate_specs", UNSET)

        def _parse_output_format_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        output_format_prompt = _parse_output_format_prompt(d.pop("output_format_prompt", UNSET))

        deep_research_uses_ocr = d.pop("deep_research_uses_ocr", UNSET)

        ocr_deep_research_uses_prefilter = d.pop("ocr_deep_research_uses_prefilter", UNSET)

        deep_research_chat_post_in = cls(
            prompt=prompt,
            recipe=recipe,
            requirement_id=requirement_id,
            model=model,
            resource_ids=resource_ids,
            chatroom_id=chatroom_id,
            enable_web_search=enable_web_search,
            reference_note_id=reference_note_id,
            clarifying_questions=clarifying_questions,
            user_answers=user_answers,
            auto_generate_specs=auto_generate_specs,
            output_format_prompt=output_format_prompt,
            deep_research_uses_ocr=deep_research_uses_ocr,
            ocr_deep_research_uses_prefilter=ocr_deep_research_uses_prefilter,
        )

        deep_research_chat_post_in.additional_properties = d
        return deep_research_chat_post_in

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
