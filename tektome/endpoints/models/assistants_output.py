from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assistants_output_log import AssistantsOutputLog


T = TypeVar("T", bound="AssistantsOutput")


@_attrs_define
class AssistantsOutput:
    """
    Attributes:
        conversation_id (UUID | Unset):
        log (AssistantsOutputLog | Unset):
    """

    conversation_id: UUID | Unset = UNSET
    log: AssistantsOutputLog | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conversation_id: str | Unset = UNSET
        if not isinstance(self.conversation_id, Unset):
            conversation_id = str(self.conversation_id)

        log: dict[str, Any] | Unset = UNSET
        if not isinstance(self.log, Unset):
            log = self.log.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id
        if log is not UNSET:
            field_dict["log"] = log

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.assistants_output_log import AssistantsOutputLog

        d = dict(src_dict)
        _conversation_id = d.pop("conversation_id", UNSET)
        conversation_id: UUID | Unset
        if isinstance(_conversation_id, Unset):
            conversation_id = UNSET
        else:
            conversation_id = UUID(_conversation_id)

        _log = d.pop("log", UNSET)
        log: AssistantsOutputLog | Unset
        if isinstance(_log, Unset):
            log = UNSET
        else:
            log = AssistantsOutputLog.from_dict(_log)

        assistants_output = cls(
            conversation_id=conversation_id,
            log=log,
        )

        assistants_output.additional_properties = d
        return assistants_output

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
