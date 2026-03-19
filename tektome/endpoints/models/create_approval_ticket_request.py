from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.approval_category_types import ApprovalCategoryTypes
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.candidate_item import CandidateItem


T = TypeVar("T", bound="CreateApprovalTicketRequest")


@_attrs_define
class CreateApprovalTicketRequest:
    """Serializer for creating an ApprovalTicket

    Attributes:
        category (ApprovalCategoryTypes):
        candidates (list[CandidateItem]):
        should_wait (bool | Unset): Mark the ticket to indicate that the caller intends to wait for the approval result
            before proceeding with execution Default: False.
        requested_approval_count (int | None | Unset):
    """

    category: ApprovalCategoryTypes
    candidates: list[CandidateItem]
    should_wait: bool | Unset = False
    requested_approval_count: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category.value

        candidates = []
        for candidates_item_data in self.candidates:
            candidates_item = candidates_item_data.to_dict()
            candidates.append(candidates_item)

        should_wait = self.should_wait

        requested_approval_count: int | None | Unset
        if isinstance(self.requested_approval_count, Unset):
            requested_approval_count = UNSET
        else:
            requested_approval_count = self.requested_approval_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "candidates": candidates,
            }
        )
        if should_wait is not UNSET:
            field_dict["should_wait"] = should_wait
        if requested_approval_count is not UNSET:
            field_dict["requested_approval_count"] = requested_approval_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.candidate_item import CandidateItem

        d = dict(src_dict)
        category = ApprovalCategoryTypes(d.pop("category"))

        candidates = []
        _candidates = d.pop("candidates")
        for candidates_item_data in _candidates:
            candidates_item = CandidateItem.from_dict(candidates_item_data)

            candidates.append(candidates_item)

        should_wait = d.pop("should_wait", UNSET)

        def _parse_requested_approval_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        requested_approval_count = _parse_requested_approval_count(d.pop("requested_approval_count", UNSET))

        create_approval_ticket_request = cls(
            category=category,
            candidates=candidates,
            should_wait=should_wait,
            requested_approval_count=requested_approval_count,
        )

        create_approval_ticket_request.additional_properties = d
        return create_approval_ticket_request

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
