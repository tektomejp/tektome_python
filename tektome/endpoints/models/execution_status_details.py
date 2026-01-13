from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExecutionStatusDetails")


@_attrs_define
class ExecutionStatusDetails:
    """Details about execution statuses within an execution group

    Attributes:
        status (str):
        count (int):
        total_executions (int):
    """

    status: str
    count: int
    total_executions: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        count = self.count

        total_executions = self.total_executions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "count": count,
                "total_executions": total_executions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status")

        count = d.pop("count")

        total_executions = d.pop("total_executions")

        execution_status_details = cls(
            status=status,
            count=count,
            total_executions=total_executions,
        )

        execution_status_details.additional_properties = d
        return execution_status_details

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
