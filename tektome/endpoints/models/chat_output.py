from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_output_log import ChatOutputLog


T = TypeVar("T", bound="ChatOutput")


@_attrs_define
class ChatOutput:
    """
    Attributes:
        message (str):
        message_id (UUID | Unset):
        conversation_id (UUID | Unset):
        log (ChatOutputLog | Unset):
        document_messages (list[Any] | Unset):
        used_file_ids (list[Any] | Unset):
    """

    message: str
    message_id: UUID | Unset = UNSET
    conversation_id: UUID | Unset = UNSET
    log: ChatOutputLog | Unset = UNSET
    document_messages: list[Any] | Unset = UNSET
    used_file_ids: list[Any] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        message_id: str | Unset = UNSET
        if not isinstance(self.message_id, Unset):
            message_id = str(self.message_id)

        conversation_id: str | Unset = UNSET
        if not isinstance(self.conversation_id, Unset):
            conversation_id = str(self.conversation_id)

        log: dict[str, Any] | Unset = UNSET
        if not isinstance(self.log, Unset):
            log = self.log.to_dict()

        document_messages: list[Any] | Unset = UNSET
        if not isinstance(self.document_messages, Unset):
            document_messages = self.document_messages

        used_file_ids: list[Any] | Unset = UNSET
        if not isinstance(self.used_file_ids, Unset):
            used_file_ids = self.used_file_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
            }
        )
        if message_id is not UNSET:
            field_dict["message_id"] = message_id
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id
        if log is not UNSET:
            field_dict["log"] = log
        if document_messages is not UNSET:
            field_dict["document_messages"] = document_messages
        if used_file_ids is not UNSET:
            field_dict["used_file_ids"] = used_file_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_output_log import ChatOutputLog

        d = dict(src_dict)
        message = d.pop("message")

        _message_id = d.pop("message_id", UNSET)
        message_id: UUID | Unset
        if isinstance(_message_id, Unset):
            message_id = UNSET
        else:
            message_id = UUID(_message_id)

        _conversation_id = d.pop("conversation_id", UNSET)
        conversation_id: UUID | Unset
        if isinstance(_conversation_id, Unset):
            conversation_id = UNSET
        else:
            conversation_id = UUID(_conversation_id)

        _log = d.pop("log", UNSET)
        log: ChatOutputLog | Unset
        if isinstance(_log, Unset):
            log = UNSET
        else:
            log = ChatOutputLog.from_dict(_log)

        document_messages = cast(list[Any], d.pop("document_messages", UNSET))

        used_file_ids = cast(list[Any], d.pop("used_file_ids", UNSET))

        chat_output = cls(
            message=message,
            message_id=message_id,
            conversation_id=conversation_id,
            log=log,
            document_messages=document_messages,
            used_file_ids=used_file_ids,
        )

        chat_output.additional_properties = d
        return chat_output

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
