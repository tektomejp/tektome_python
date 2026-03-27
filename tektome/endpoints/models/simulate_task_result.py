from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.simulate_task_result_status import SimulateTaskResultStatus

T = TypeVar("T", bound="SimulateTaskResult")


@_attrs_define
class SimulateTaskResult:
    """For demonstration purpose, this should be in /serializers/<same_name_as_this_file>.py

    Attributes:
        status (SimulateTaskResultStatus):
        result (int | None):
    """

    status: SimulateTaskResultStatus
    result: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        result: int | None
        result = self.result

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "result": result,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = SimulateTaskResultStatus(d.pop("status"))

        def _parse_result(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        result = _parse_result(d.pop("result"))

        simulate_task_result = cls(
            status=status,
            result=result,
        )

        simulate_task_result.additional_properties = d
        return simulate_task_result

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
