from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_bulk_review_request_action import CreateBulkReviewRequestAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateBulkReviewRequest")


@_attrs_define
class CreateBulkReviewRequest:
    """
    Attributes:
        approval_ids (list[UUID]): List of Approval Ticket IDs to be approved or rejected.
        action (CreateBulkReviewRequestAction): Action to be performed on the approval tickets.
        is_auto_select_first_candidate (bool | Unset): True - Auto-selects the first candidate for tickets that have no
            selected candidate Default: True.
    """

    approval_ids: list[UUID]
    action: CreateBulkReviewRequestAction
    is_auto_select_first_candidate: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        approval_ids = []
        for approval_ids_item_data in self.approval_ids:
            approval_ids_item = str(approval_ids_item_data)
            approval_ids.append(approval_ids_item)

        action = self.action.value

        is_auto_select_first_candidate = self.is_auto_select_first_candidate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "approval_ids": approval_ids,
                "action": action,
            }
        )
        if is_auto_select_first_candidate is not UNSET:
            field_dict["is_auto_select_first_candidate"] = is_auto_select_first_candidate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        approval_ids = []
        _approval_ids = d.pop("approval_ids")
        for approval_ids_item_data in _approval_ids:
            approval_ids_item = UUID(approval_ids_item_data)

            approval_ids.append(approval_ids_item)

        action = CreateBulkReviewRequestAction(d.pop("action"))

        is_auto_select_first_candidate = d.pop("is_auto_select_first_candidate", UNSET)

        create_bulk_review_request = cls(
            approval_ids=approval_ids,
            action=action,
            is_auto_select_first_candidate=is_auto_select_first_candidate,
        )

        create_bulk_review_request.additional_properties = d
        return create_bulk_review_request

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
