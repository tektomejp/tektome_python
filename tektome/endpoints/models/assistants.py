from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.large_language_model_enum import LargeLanguageModelEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assistants_callback_payload import AssistantsCallbackPayload


T = TypeVar("T", bound="Assistants")


@_attrs_define
class Assistants:
    """
    Attributes:
        message (str):
        callback_url (str):
        model_name (LargeLanguageModelEnum | Unset):  Default: LargeLanguageModelEnum.OPENAI_GPT_4_1106_PREVIEW.
        system_prompt (None | str | Unset):
        conversation_id (UUID | Unset):
        callback_payload (AssistantsCallbackPayload | Unset):
        document_urls (list[str] | Unset):
    """

    message: str
    callback_url: str
    model_name: LargeLanguageModelEnum | Unset = LargeLanguageModelEnum.OPENAI_GPT_4_1106_PREVIEW
    system_prompt: None | str | Unset = UNSET
    conversation_id: UUID | Unset = UNSET
    callback_payload: AssistantsCallbackPayload | Unset = UNSET
    document_urls: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        callback_url = self.callback_url

        model_name: str | Unset = UNSET
        if not isinstance(self.model_name, Unset):
            model_name = self.model_name.value

        system_prompt: None | str | Unset
        if isinstance(self.system_prompt, Unset):
            system_prompt = UNSET
        else:
            system_prompt = self.system_prompt

        conversation_id: str | Unset = UNSET
        if not isinstance(self.conversation_id, Unset):
            conversation_id = str(self.conversation_id)

        callback_payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.callback_payload, Unset):
            callback_payload = self.callback_payload.to_dict()

        document_urls: list[str] | Unset = UNSET
        if not isinstance(self.document_urls, Unset):
            document_urls = self.document_urls

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "callback_url": callback_url,
            }
        )
        if model_name is not UNSET:
            field_dict["model_name"] = model_name
        if system_prompt is not UNSET:
            field_dict["system_prompt"] = system_prompt
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id
        if callback_payload is not UNSET:
            field_dict["callback_payload"] = callback_payload
        if document_urls is not UNSET:
            field_dict["document_urls"] = document_urls

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.assistants_callback_payload import AssistantsCallbackPayload

        d = dict(src_dict)
        message = d.pop("message")

        callback_url = d.pop("callback_url")

        _model_name = d.pop("model_name", UNSET)
        model_name: LargeLanguageModelEnum | Unset
        if isinstance(_model_name, Unset):
            model_name = UNSET
        else:
            model_name = LargeLanguageModelEnum(_model_name)

        def _parse_system_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        system_prompt = _parse_system_prompt(d.pop("system_prompt", UNSET))

        _conversation_id = d.pop("conversation_id", UNSET)
        conversation_id: UUID | Unset
        if isinstance(_conversation_id, Unset):
            conversation_id = UNSET
        else:
            conversation_id = UUID(_conversation_id)

        _callback_payload = d.pop("callback_payload", UNSET)
        callback_payload: AssistantsCallbackPayload | Unset
        if isinstance(_callback_payload, Unset):
            callback_payload = UNSET
        else:
            callback_payload = AssistantsCallbackPayload.from_dict(_callback_payload)

        document_urls = cast(list[str], d.pop("document_urls", UNSET))

        assistants = cls(
            message=message,
            callback_url=callback_url,
            model_name=model_name,
            system_prompt=system_prompt,
            conversation_id=conversation_id,
            callback_payload=callback_payload,
            document_urls=document_urls,
        )

        assistants.additional_properties = d
        return assistants

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
