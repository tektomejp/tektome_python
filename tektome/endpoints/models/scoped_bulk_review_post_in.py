from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.scoped_bulk_review_post_in_action import ScopedBulkReviewPostInAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScopedBulkReviewPostIn")


@_attrs_define
class ScopedBulkReviewPostIn:
    """Scoped bulk review input for reviewing all pending tickets in a scope

    Attributes:
        action (ScopedBulkReviewPostInAction): Action to be performed on the approval tickets.
        is_auto_select_first_candidate (bool | Unset): If True, auto-selects the first candidate for tickets that have
            no selected candidate. Default: False.
    """

    action: ScopedBulkReviewPostInAction
    is_auto_select_first_candidate: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        is_auto_select_first_candidate = self.is_auto_select_first_candidate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
            }
        )
        if is_auto_select_first_candidate is not UNSET:
            field_dict["is_auto_select_first_candidate"] = is_auto_select_first_candidate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = ScopedBulkReviewPostInAction(d.pop("action"))

        is_auto_select_first_candidate = d.pop("is_auto_select_first_candidate", UNSET)

        scoped_bulk_review_post_in = cls(
            action=action,
            is_auto_select_first_candidate=is_auto_select_first_candidate,
        )

        scoped_bulk_review_post_in.additional_properties = d
        return scoped_bulk_review_post_in

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
