from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionStatusCountDetails")


@_attrs_define
class ExecutionStatusCountDetails:
    """Counts of executions by status within an execution group

    Attributes:
        pending_count (int | Unset):  Default: 0.
        in_progress_count (int | Unset):  Default: 0.
        completed_count (int | Unset):  Default: 0.
        failed_count (int | Unset):  Default: 0.
        auto_approved_count (int | Unset):  Default: 0.
        cancelled_count (int | Unset):  Default: 0.
    """

    pending_count: int | Unset = 0
    in_progress_count: int | Unset = 0
    completed_count: int | Unset = 0
    failed_count: int | Unset = 0
    auto_approved_count: int | Unset = 0
    cancelled_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pending_count = self.pending_count

        in_progress_count = self.in_progress_count

        completed_count = self.completed_count

        failed_count = self.failed_count

        auto_approved_count = self.auto_approved_count

        cancelled_count = self.cancelled_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pending_count is not UNSET:
            field_dict["pending_count"] = pending_count
        if in_progress_count is not UNSET:
            field_dict["in_progress_count"] = in_progress_count
        if completed_count is not UNSET:
            field_dict["completed_count"] = completed_count
        if failed_count is not UNSET:
            field_dict["failed_count"] = failed_count
        if auto_approved_count is not UNSET:
            field_dict["auto_approved_count"] = auto_approved_count
        if cancelled_count is not UNSET:
            field_dict["cancelled_count"] = cancelled_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pending_count = d.pop("pending_count", UNSET)

        in_progress_count = d.pop("in_progress_count", UNSET)

        completed_count = d.pop("completed_count", UNSET)

        failed_count = d.pop("failed_count", UNSET)

        auto_approved_count = d.pop("auto_approved_count", UNSET)

        cancelled_count = d.pop("cancelled_count", UNSET)

        execution_status_count_details = cls(
            pending_count=pending_count,
            in_progress_count=in_progress_count,
            completed_count=completed_count,
            failed_count=failed_count,
            auto_approved_count=auto_approved_count,
            cancelled_count=cancelled_count,
        )

        execution_status_count_details.additional_properties = d
        return execution_status_count_details

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
