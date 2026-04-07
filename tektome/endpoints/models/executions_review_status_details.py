from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.execution_review_status import ExecutionReviewStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionsReviewStatusDetails")


@_attrs_define
class ExecutionsReviewStatusDetails:
    """Details about execution review statuses within an execution group

    Attributes:
        pending_count (int):
        reviewed_count (int):
        not_required_count (int):
        rejected_count (int):
        status (ExecutionReviewStatus | None | Unset):
    """

    pending_count: int
    reviewed_count: int
    not_required_count: int
    rejected_count: int
    status: ExecutionReviewStatus | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pending_count = self.pending_count

        reviewed_count = self.reviewed_count

        not_required_count = self.not_required_count

        rejected_count = self.rejected_count

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, ExecutionReviewStatus):
            status = self.status.value
        else:
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pending_count": pending_count,
                "reviewed_count": reviewed_count,
                "not_required_count": not_required_count,
                "rejected_count": rejected_count,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pending_count = d.pop("pending_count")

        reviewed_count = d.pop("reviewed_count")

        not_required_count = d.pop("not_required_count")

        rejected_count = d.pop("rejected_count")

        def _parse_status(data: object) -> ExecutionReviewStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = ExecutionReviewStatus(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExecutionReviewStatus | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        executions_review_status_details = cls(
            pending_count=pending_count,
            reviewed_count=reviewed_count,
            not_required_count=not_required_count,
            rejected_count=rejected_count,
            status=status,
        )

        executions_review_status_details.additional_properties = d
        return executions_review_status_details

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
