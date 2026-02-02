from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_ticket_candidate_out_data_container import ApprovalTicketCandidateOutDataContainer
    from ..models.approval_ticket_candidate_out_reviewed_data_snapshot_type_0 import (
        ApprovalTicketCandidateOutReviewedDataSnapshotType0,
    )
    from ..models.approval_ticket_get_out import ApprovalTicketGetOut


T = TypeVar("T", bound="ApprovalTicketCandidateOut")


@_attrs_define
class ApprovalTicketCandidateOut:
    """Serializer for ApprovalTicketCandidate details

    Attributes:
        approval_ticket (ApprovalTicketGetOut): Serializer for ApprovalTicket details
        id (None | Unset | UUID):
        data_container (ApprovalTicketCandidateOutDataContainer | Unset): The data related to this approval ticket
            candidate. These are the payload changes proposed for approval
        status (str | Unset): The status of the approval ticket Default: 'Unselected'.
        reviewed_data_snapshot (ApprovalTicketCandidateOutReviewedDataSnapshotType0 | None | Unset): Immutable snapshot
            of the reviewed data captured at reviewed time for audit trail
    """

    approval_ticket: ApprovalTicketGetOut
    id: None | Unset | UUID = UNSET
    data_container: ApprovalTicketCandidateOutDataContainer | Unset = UNSET
    status: str | Unset = "Unselected"
    reviewed_data_snapshot: ApprovalTicketCandidateOutReviewedDataSnapshotType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.approval_ticket_candidate_out_reviewed_data_snapshot_type_0 import (
            ApprovalTicketCandidateOutReviewedDataSnapshotType0,
        )

        approval_ticket = self.approval_ticket.to_dict()

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        data_container: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_container, Unset):
            data_container = self.data_container.to_dict()

        status = self.status

        reviewed_data_snapshot: dict[str, Any] | None | Unset
        if isinstance(self.reviewed_data_snapshot, Unset):
            reviewed_data_snapshot = UNSET
        elif isinstance(self.reviewed_data_snapshot, ApprovalTicketCandidateOutReviewedDataSnapshotType0):
            reviewed_data_snapshot = self.reviewed_data_snapshot.to_dict()
        else:
            reviewed_data_snapshot = self.reviewed_data_snapshot

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "approval_ticket": approval_ticket,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if data_container is not UNSET:
            field_dict["data_container"] = data_container
        if status is not UNSET:
            field_dict["status"] = status
        if reviewed_data_snapshot is not UNSET:
            field_dict["reviewed_data_snapshot"] = reviewed_data_snapshot

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.approval_ticket_candidate_out_data_container import ApprovalTicketCandidateOutDataContainer
        from ..models.approval_ticket_candidate_out_reviewed_data_snapshot_type_0 import (
            ApprovalTicketCandidateOutReviewedDataSnapshotType0,
        )
        from ..models.approval_ticket_get_out import ApprovalTicketGetOut

        d = dict(src_dict)
        approval_ticket = ApprovalTicketGetOut.from_dict(d.pop("approval_ticket"))

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

        _data_container = d.pop("data_container", UNSET)
        data_container: ApprovalTicketCandidateOutDataContainer | Unset
        if isinstance(_data_container, Unset):
            data_container = UNSET
        else:
            data_container = ApprovalTicketCandidateOutDataContainer.from_dict(_data_container)

        status = d.pop("status", UNSET)

        def _parse_reviewed_data_snapshot(
            data: object,
        ) -> ApprovalTicketCandidateOutReviewedDataSnapshotType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                reviewed_data_snapshot_type_0 = ApprovalTicketCandidateOutReviewedDataSnapshotType0.from_dict(data)

                return reviewed_data_snapshot_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApprovalTicketCandidateOutReviewedDataSnapshotType0 | None | Unset, data)

        reviewed_data_snapshot = _parse_reviewed_data_snapshot(d.pop("reviewed_data_snapshot", UNSET))

        approval_ticket_candidate_out = cls(
            approval_ticket=approval_ticket,
            id=id,
            data_container=data_container,
            status=status,
            reviewed_data_snapshot=reviewed_data_snapshot,
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
