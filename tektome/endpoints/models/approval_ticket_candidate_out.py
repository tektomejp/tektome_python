from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_ticket_candidate_out_instructions import ApprovalTicketCandidateOutInstructions
    from ..models.attribute_data_snapshot import AttributeDataSnapshot
    from ..models.file_data_snapshot import FileDataSnapshot


T = TypeVar("T", bound="ApprovalTicketCandidateOut")


@_attrs_define
class ApprovalTicketCandidateOut:
    """Serializer for ApprovalTicketCandidate details

    Attributes:
        serialized_review_data (AttributeDataSnapshot | FileDataSnapshot | None | Unset):
        id (None | Unset | UUID):
        instructions (ApprovalTicketCandidateOutInstructions | Unset): The data related to this approval ticket
            candidate. These are the instructions to be performed once reviewed.
        status (str | Unset): The status of the approval ticket Default: 'Unselected'.
    """

    serialized_review_data: AttributeDataSnapshot | FileDataSnapshot | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    instructions: ApprovalTicketCandidateOutInstructions | Unset = UNSET
    status: str | Unset = "Unselected"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.attribute_data_snapshot import AttributeDataSnapshot
        from ..models.file_data_snapshot import FileDataSnapshot

        serialized_review_data: dict[str, Any] | None | Unset
        if isinstance(self.serialized_review_data, Unset):
            serialized_review_data = UNSET
        elif isinstance(self.serialized_review_data, AttributeDataSnapshot):
            serialized_review_data = self.serialized_review_data.to_dict()
        elif isinstance(self.serialized_review_data, FileDataSnapshot):
            serialized_review_data = self.serialized_review_data.to_dict()
        else:
            serialized_review_data = self.serialized_review_data

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        instructions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.instructions, Unset):
            instructions = self.instructions.to_dict()

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if serialized_review_data is not UNSET:
            field_dict["serialized_review_data"] = serialized_review_data
        if id is not UNSET:
            field_dict["id"] = id
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.approval_ticket_candidate_out_instructions import ApprovalTicketCandidateOutInstructions
        from ..models.attribute_data_snapshot import AttributeDataSnapshot
        from ..models.file_data_snapshot import FileDataSnapshot

        d = dict(src_dict)

        def _parse_serialized_review_data(data: object) -> AttributeDataSnapshot | FileDataSnapshot | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                serialized_review_data_type_0 = AttributeDataSnapshot.from_dict(data)

                return serialized_review_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                serialized_review_data_type_1 = FileDataSnapshot.from_dict(data)

                return serialized_review_data_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AttributeDataSnapshot | FileDataSnapshot | None | Unset, data)

        serialized_review_data = _parse_serialized_review_data(d.pop("serialized_review_data", UNSET))

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

        _instructions = d.pop("instructions", UNSET)
        instructions: ApprovalTicketCandidateOutInstructions | Unset
        if isinstance(_instructions, Unset):
            instructions = UNSET
        else:
            instructions = ApprovalTicketCandidateOutInstructions.from_dict(_instructions)

        status = d.pop("status", UNSET)

        approval_ticket_candidate_out = cls(
            serialized_review_data=serialized_review_data,
            id=id,
            instructions=instructions,
            status=status,
        )

        approval_ticket_candidate_out.additional_properties = d
        return approval_ticket_candidate_out

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
