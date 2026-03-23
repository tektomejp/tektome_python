from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bim_project_v2_index_task_response_status import BimProjectV2IndexTaskResponseStatus

T = TypeVar("T", bound="BimProjectV2IndexTaskResponse")


@_attrs_define
class BimProjectV2IndexTaskResponse:
    """Response schema for BIM project-wide V2 indexing task trigger.

    Attributes:
        process_id (str): Celery task ID used to track indexing status
        status (BimProjectV2IndexTaskResponseStatus): started when a new task was queued, or already_running when an
            active task for this BIM project already exists
    """

    process_id: str
    status: BimProjectV2IndexTaskResponseStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        process_id = self.process_id

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "process_id": process_id,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        process_id = d.pop("process_id")

        status = BimProjectV2IndexTaskResponseStatus(d.pop("status"))

        bim_project_v2_index_task_response = cls(
            process_id=process_id,
            status=status,
        )

        bim_project_v2_index_task_response.additional_properties = d
        return bim_project_v2_index_task_response

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
