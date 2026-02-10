from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_review_post_in_action import BulkReviewPostInAction

T = TypeVar("T", bound="BulkReviewPostIn")


@_attrs_define
class BulkReviewPostIn:
    """
    Attributes:
        approval_ids (list[UUID]): List of Approval Ticket IDs to be approved or rejected.
        action (BulkReviewPostInAction): Action to be performed on the approval tickets.
    """

    approval_ids: list[UUID]
    action: BulkReviewPostInAction
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        approval_ids = []
        for approval_ids_item_data in self.approval_ids:
            approval_ids_item = str(approval_ids_item_data)
            approval_ids.append(approval_ids_item)

        action = self.action.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "approval_ids": approval_ids,
                "action": action,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        approval_ids = []
        _approval_ids = d.pop("approval_ids")
        for approval_ids_item_data in _approval_ids:
            approval_ids_item = UUID(approval_ids_item_data)

            approval_ids.append(approval_ids_item)

        action = BulkReviewPostInAction(d.pop("action"))

        bulk_review_post_in = cls(
            approval_ids=approval_ids,
            action=action,
        )

        bulk_review_post_in.additional_properties = d
        return bulk_review_post_in

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
