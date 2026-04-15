from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.llm_messages_response_content_item import LLMMessagesResponseContentItem
    from ..models.llm_usage_response import LLMUsageResponse


T = TypeVar("T", bound="LLMMessagesResponse")


@_attrs_define
class LLMMessagesResponse:
    """
    Attributes:
        id (str):
        type_ (str):
        role (str):
        content (list[LLMMessagesResponseContentItem]):
        model (str):
        usage (LLMUsageResponse):
        stop_reason (None | str | Unset):
        stop_sequence (None | str | Unset):
    """

    id: str
    type_: str
    role: str
    content: list[LLMMessagesResponseContentItem]
    model: str
    usage: LLMUsageResponse
    stop_reason: None | str | Unset = UNSET
    stop_sequence: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        role = self.role

        content = []
        for content_item_data in self.content:
            content_item = content_item_data.to_dict()
            content.append(content_item)

        model = self.model

        usage = self.usage.to_dict()

        stop_reason: None | str | Unset
        if isinstance(self.stop_reason, Unset):
            stop_reason = UNSET
        else:
            stop_reason = self.stop_reason

        stop_sequence: None | str | Unset
        if isinstance(self.stop_sequence, Unset):
            stop_sequence = UNSET
        else:
            stop_sequence = self.stop_sequence

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "role": role,
                "content": content,
                "model": model,
                "usage": usage,
            }
        )
        if stop_reason is not UNSET:
            field_dict["stop_reason"] = stop_reason
        if stop_sequence is not UNSET:
            field_dict["stop_sequence"] = stop_sequence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.llm_messages_response_content_item import LLMMessagesResponseContentItem
        from ..models.llm_usage_response import LLMUsageResponse

        d = dict(src_dict)
        id = d.pop("id")

        type_ = d.pop("type")

        role = d.pop("role")

        content = []
        _content = d.pop("content")
        for content_item_data in _content:
            content_item = LLMMessagesResponseContentItem.from_dict(content_item_data)

            content.append(content_item)

        model = d.pop("model")

        usage = LLMUsageResponse.from_dict(d.pop("usage"))

        def _parse_stop_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stop_reason = _parse_stop_reason(d.pop("stop_reason", UNSET))

        def _parse_stop_sequence(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stop_sequence = _parse_stop_sequence(d.pop("stop_sequence", UNSET))

        llm_messages_response = cls(
            id=id,
            type_=type_,
            role=role,
            content=content,
            model=model,
            usage=usage,
            stop_reason=stop_reason,
            stop_sequence=stop_sequence,
        )

        llm_messages_response.additional_properties = d
        return llm_messages_response

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
