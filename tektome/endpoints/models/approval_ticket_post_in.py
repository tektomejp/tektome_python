from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.approval_category_types import ApprovalCategoryTypes

if TYPE_CHECKING:
    from ..models.candidate_item import CandidateItem


T = TypeVar("T", bound="ApprovalTicketPostIn")


@_attrs_define
class ApprovalTicketPostIn:
    """Serializer for creating an ApprovalTicket

    Attributes:
        category (ApprovalCategoryTypes):
        candidates (list[CandidateItem]):
    """

    category: ApprovalCategoryTypes
    candidates: list[CandidateItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category.value

        candidates = []
        for candidates_item_data in self.candidates:
            candidates_item = candidates_item_data.to_dict()
            candidates.append(candidates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "candidates": candidates,
            }
        )

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

        approval_ticket_post_in = cls(
            category=category,
            candidates=candidates,
        )

        approval_ticket_post_in.additional_properties = d
        return approval_ticket_post_in

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
