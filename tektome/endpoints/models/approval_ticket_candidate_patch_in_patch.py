from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.approval_candidate_status import ApprovalCandidateStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.candidate_item import CandidateItem


T = TypeVar("T", bound="ApprovalTicketCandidatePatchInPatch")


@_attrs_define
class ApprovalTicketCandidatePatchInPatch:
    """
    Attributes:
        status (ApprovalCandidateStatus | None | Unset):
        data_container (CandidateItem | None | Unset):
    """

    status: ApprovalCandidateStatus | None | Unset = UNSET
    data_container: CandidateItem | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.candidate_item import CandidateItem

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, ApprovalCandidateStatus):
            status = self.status.value
        else:
            status = self.status

        data_container: dict[str, Any] | None | Unset
        if isinstance(self.data_container, Unset):
            data_container = UNSET
        elif isinstance(self.data_container, CandidateItem):
            data_container = self.data_container.to_dict()
        else:
            data_container = self.data_container

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if data_container is not UNSET:
            field_dict["data_container"] = data_container

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.candidate_item import CandidateItem

        d = dict(src_dict)

        def _parse_status(data: object) -> ApprovalCandidateStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = ApprovalCandidateStatus(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApprovalCandidateStatus | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_data_container(data: object) -> CandidateItem | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_container_type_0 = CandidateItem.from_dict(data)

                return data_container_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CandidateItem | None | Unset, data)

        data_container = _parse_data_container(d.pop("data_container", UNSET))

        approval_ticket_candidate_patch_in_patch = cls(
            status=status,
            data_container=data_container,
        )

        approval_ticket_candidate_patch_in_patch.additional_properties = d
        return approval_ticket_candidate_patch_in_patch

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
