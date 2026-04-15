from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_tier import ModelTier
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.llm_messages_request_messages_item import LLMMessagesRequestMessagesItem
    from ..models.llm_messages_request_metadata_type_0 import LLMMessagesRequestMetadataType0
    from ..models.llm_messages_request_system_type_1_item import LLMMessagesRequestSystemType1Item
    from ..models.llm_messages_request_tool_choice_type_0 import LLMMessagesRequestToolChoiceType0
    from ..models.llm_messages_request_tools_type_0_item import LLMMessagesRequestToolsType0Item


T = TypeVar("T", bound="LLMMessagesRequest")


@_attrs_define
class LLMMessagesRequest:
    """
    Attributes:
        model (ModelTier):
        messages (list[LLMMessagesRequestMessagesItem]):
        system (list[LLMMessagesRequestSystemType1Item] | None | str | Unset):
        max_tokens (int | Unset):  Default: 4096.
        temperature (float | None | Unset):
        top_p (float | None | Unset):
        top_k (int | None | Unset):
        tools (list[LLMMessagesRequestToolsType0Item] | None | Unset):
        tool_choice (LLMMessagesRequestToolChoiceType0 | None | str | Unset):
        metadata (LLMMessagesRequestMetadataType0 | None | Unset):
        stop_sequences (list[str] | None | Unset):
    """

    model: ModelTier
    messages: list[LLMMessagesRequestMessagesItem]
    system: list[LLMMessagesRequestSystemType1Item] | None | str | Unset = UNSET
    max_tokens: int | Unset = 4096
    temperature: float | None | Unset = UNSET
    top_p: float | None | Unset = UNSET
    top_k: int | None | Unset = UNSET
    tools: list[LLMMessagesRequestToolsType0Item] | None | Unset = UNSET
    tool_choice: LLMMessagesRequestToolChoiceType0 | None | str | Unset = UNSET
    metadata: LLMMessagesRequestMetadataType0 | None | Unset = UNSET
    stop_sequences: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.llm_messages_request_metadata_type_0 import LLMMessagesRequestMetadataType0
        from ..models.llm_messages_request_tool_choice_type_0 import LLMMessagesRequestToolChoiceType0

        model = self.model.value

        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()
            messages.append(messages_item)

        system: list[dict[str, Any]] | None | str | Unset
        if isinstance(self.system, Unset):
            system = UNSET
        elif isinstance(self.system, list):
            system = []
            for system_type_1_item_data in self.system:
                system_type_1_item = system_type_1_item_data.to_dict()
                system.append(system_type_1_item)

        else:
            system = self.system

        max_tokens = self.max_tokens

        temperature: float | None | Unset
        if isinstance(self.temperature, Unset):
            temperature = UNSET
        else:
            temperature = self.temperature

        top_p: float | None | Unset
        if isinstance(self.top_p, Unset):
            top_p = UNSET
        else:
            top_p = self.top_p

        top_k: int | None | Unset
        if isinstance(self.top_k, Unset):
            top_k = UNSET
        else:
            top_k = self.top_k

        tools: list[dict[str, Any]] | None | Unset
        if isinstance(self.tools, Unset):
            tools = UNSET
        elif isinstance(self.tools, list):
            tools = []
            for tools_type_0_item_data in self.tools:
                tools_type_0_item = tools_type_0_item_data.to_dict()
                tools.append(tools_type_0_item)

        else:
            tools = self.tools

        tool_choice: dict[str, Any] | None | str | Unset
        if isinstance(self.tool_choice, Unset):
            tool_choice = UNSET
        elif isinstance(self.tool_choice, LLMMessagesRequestToolChoiceType0):
            tool_choice = self.tool_choice.to_dict()
        else:
            tool_choice = self.tool_choice

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, LLMMessagesRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        stop_sequences: list[str] | None | Unset
        if isinstance(self.stop_sequences, Unset):
            stop_sequences = UNSET
        elif isinstance(self.stop_sequences, list):
            stop_sequences = self.stop_sequences

        else:
            stop_sequences = self.stop_sequences

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
                "messages": messages,
            }
        )
        if system is not UNSET:
            field_dict["system"] = system
        if max_tokens is not UNSET:
            field_dict["max_tokens"] = max_tokens
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if top_p is not UNSET:
            field_dict["top_p"] = top_p
        if top_k is not UNSET:
            field_dict["top_k"] = top_k
        if tools is not UNSET:
            field_dict["tools"] = tools
        if tool_choice is not UNSET:
            field_dict["tool_choice"] = tool_choice
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if stop_sequences is not UNSET:
            field_dict["stop_sequences"] = stop_sequences

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.llm_messages_request_messages_item import LLMMessagesRequestMessagesItem
        from ..models.llm_messages_request_metadata_type_0 import LLMMessagesRequestMetadataType0
        from ..models.llm_messages_request_system_type_1_item import LLMMessagesRequestSystemType1Item
        from ..models.llm_messages_request_tool_choice_type_0 import LLMMessagesRequestToolChoiceType0
        from ..models.llm_messages_request_tools_type_0_item import LLMMessagesRequestToolsType0Item

        d = dict(src_dict)
        model = ModelTier(d.pop("model"))

        messages = []
        _messages = d.pop("messages")
        for messages_item_data in _messages:
            messages_item = LLMMessagesRequestMessagesItem.from_dict(messages_item_data)

            messages.append(messages_item)

        def _parse_system(data: object) -> list[LLMMessagesRequestSystemType1Item] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                system_type_1 = []
                _system_type_1 = data
                for system_type_1_item_data in _system_type_1:
                    system_type_1_item = LLMMessagesRequestSystemType1Item.from_dict(system_type_1_item_data)

                    system_type_1.append(system_type_1_item)

                return system_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LLMMessagesRequestSystemType1Item] | None | str | Unset, data)

        system = _parse_system(d.pop("system", UNSET))

        max_tokens = d.pop("max_tokens", UNSET)

        def _parse_temperature(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        temperature = _parse_temperature(d.pop("temperature", UNSET))

        def _parse_top_p(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        top_p = _parse_top_p(d.pop("top_p", UNSET))

        def _parse_top_k(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        top_k = _parse_top_k(d.pop("top_k", UNSET))

        def _parse_tools(data: object) -> list[LLMMessagesRequestToolsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tools_type_0 = []
                _tools_type_0 = data
                for tools_type_0_item_data in _tools_type_0:
                    tools_type_0_item = LLMMessagesRequestToolsType0Item.from_dict(tools_type_0_item_data)

                    tools_type_0.append(tools_type_0_item)

                return tools_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LLMMessagesRequestToolsType0Item] | None | Unset, data)

        tools = _parse_tools(d.pop("tools", UNSET))

        def _parse_tool_choice(data: object) -> LLMMessagesRequestToolChoiceType0 | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tool_choice_type_0 = LLMMessagesRequestToolChoiceType0.from_dict(data)

                return tool_choice_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LLMMessagesRequestToolChoiceType0 | None | str | Unset, data)

        tool_choice = _parse_tool_choice(d.pop("tool_choice", UNSET))

        def _parse_metadata(data: object) -> LLMMessagesRequestMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = LLMMessagesRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LLMMessagesRequestMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_stop_sequences(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                stop_sequences_type_0 = cast(list[str], data)

                return stop_sequences_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        stop_sequences = _parse_stop_sequences(d.pop("stop_sequences", UNSET))

        llm_messages_request = cls(
            model=model,
            messages=messages,
            system=system,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
            tools=tools,
            tool_choice=tool_choice,
            metadata=metadata,
            stop_sequences=stop_sequences,
        )

        llm_messages_request.additional_properties = d
        return llm_messages_request

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
