from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_ticket_candidate_patch_out_data_snapshot_type_0 import (
        ApprovalTicketCandidatePatchOutDataSnapshotType0,
    )
    from ..models.approval_ticket_candidate_patch_out_instructions import ApprovalTicketCandidatePatchOutInstructions


T = TypeVar("T", bound="ApprovalTicketCandidatePatchOut")


@_attrs_define
class ApprovalTicketCandidatePatchOut:
    """Serializer for ApprovalTicketCandidate details

    Attributes:
        id (None | Unset | UUID):
        instructions (ApprovalTicketCandidatePatchOutInstructions | Unset): The data related to this approval ticket
            candidate. These are the instructions to be performed once reviewed.
        status (str | Unset): The status of the approval ticket Default: 'Unselected'.
        data_snapshot (ApprovalTicketCandidatePatchOutDataSnapshotType0 | None | Unset): Immutable snapshot of the
            reviewed data from the initial to approved changes
    """

    id: None | Unset | UUID = UNSET
    instructions: ApprovalTicketCandidatePatchOutInstructions | Unset = UNSET
    status: str | Unset = "Unselected"
    data_snapshot: ApprovalTicketCandidatePatchOutDataSnapshotType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.approval_ticket_candidate_patch_out_data_snapshot_type_0 import (
            ApprovalTicketCandidatePatchOutDataSnapshotType0,
        )

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

        data_snapshot: dict[str, Any] | None | Unset
        if isinstance(self.data_snapshot, Unset):
            data_snapshot = UNSET
        elif isinstance(self.data_snapshot, ApprovalTicketCandidatePatchOutDataSnapshotType0):
            data_snapshot = self.data_snapshot.to_dict()
        else:
            data_snapshot = self.data_snapshot

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if status is not UNSET:
            field_dict["status"] = status
        if data_snapshot is not UNSET:
            field_dict["data_snapshot"] = data_snapshot

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.approval_ticket_candidate_patch_out_data_snapshot_type_0 import (
            ApprovalTicketCandidatePatchOutDataSnapshotType0,
        )
        from ..models.approval_ticket_candidate_patch_out_instructions import (
            ApprovalTicketCandidatePatchOutInstructions,
        )

        d = dict(src_dict)

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
        instructions: ApprovalTicketCandidatePatchOutInstructions | Unset
        if isinstance(_instructions, Unset):
            instructions = UNSET
        else:
            instructions = ApprovalTicketCandidatePatchOutInstructions.from_dict(_instructions)

        status = d.pop("status", UNSET)

        def _parse_data_snapshot(data: object) -> ApprovalTicketCandidatePatchOutDataSnapshotType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_snapshot_type_0 = ApprovalTicketCandidatePatchOutDataSnapshotType0.from_dict(data)

                return data_snapshot_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApprovalTicketCandidatePatchOutDataSnapshotType0 | None | Unset, data)

        data_snapshot = _parse_data_snapshot(d.pop("data_snapshot", UNSET))

        approval_ticket_candidate_patch_out = cls(
            id=id,
            instructions=instructions,
            status=status,
            data_snapshot=data_snapshot,
        )

        approval_ticket_candidate_patch_out.additional_properties = d
        return approval_ticket_candidate_patch_out

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
