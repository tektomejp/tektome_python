from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution_process_get_out import ExecutionProcessGetOut
    from ..models.executions_review_status_details import ExecutionsReviewStatusDetails
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="ExecutionsGetOut")


@_attrs_define
class ExecutionsGetOut:
    """Serializer for retrieving executions details along with related metadata.

    Attributes:
        created_by (UserMetadata):
        updated_by (UserMetadata):
        approvals_count (int):
        processes_details (list[ExecutionProcessGetOut]):
        review_status (ExecutionsReviewStatusDetails): Details about execution review statuses within an execution group
        execution_group (UUID): The execution group this execution belongs to
        created (datetime.datetime):
        updated (datetime.datetime):
        memo (None | str | Unset):
        id (None | Unset | UUID):
        summary (None | str | Unset): A brief summary of the tickets from the execution
        launched_by (None | Unset | UUID): The user who launched this execution
        status (str | Unset): The status of the execution (e.g., pending, completed, failed) Default: 'pending'.
        start_time (datetime.datetime | None | Unset):
        end_time (datetime.datetime | None | Unset):
    """

    created_by: UserMetadata
    updated_by: UserMetadata
    approvals_count: int
    processes_details: list[ExecutionProcessGetOut]
    review_status: ExecutionsReviewStatusDetails
    execution_group: UUID
    created: datetime.datetime
    updated: datetime.datetime
    memo: None | str | Unset = UNSET
    id: None | Unset | UUID = UNSET
    summary: None | str | Unset = UNSET
    launched_by: None | Unset | UUID = UNSET
    status: str | Unset = "pending"
    start_time: datetime.datetime | None | Unset = UNSET
    end_time: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_by = self.created_by.to_dict()

        updated_by = self.updated_by.to_dict()

        approvals_count = self.approvals_count

        processes_details = []
        for processes_details_item_data in self.processes_details:
            processes_details_item = processes_details_item_data.to_dict()
            processes_details.append(processes_details_item)

        review_status = self.review_status.to_dict()

        execution_group = str(self.execution_group)

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        memo: None | str | Unset
        if isinstance(self.memo, Unset):
            memo = UNSET
        else:
            memo = self.memo

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        summary: None | str | Unset
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        launched_by: None | str | Unset
        if isinstance(self.launched_by, Unset):
            launched_by = UNSET
        elif isinstance(self.launched_by, UUID):
            launched_by = str(self.launched_by)
        else:
            launched_by = self.launched_by

        status = self.status

        start_time: None | str | Unset
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        elif isinstance(self.start_time, datetime.datetime):
            start_time = self.start_time.isoformat()
        else:
            start_time = self.start_time

        end_time: None | str | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_by": created_by,
                "updated_by": updated_by,
                "approvals_count": approvals_count,
                "processes_details": processes_details,
                "review_status": review_status,
                "execution_group": execution_group,
                "created": created,
                "updated": updated,
            }
        )
        if memo is not UNSET:
            field_dict["memo"] = memo
        if id is not UNSET:
            field_dict["id"] = id
        if summary is not UNSET:
            field_dict["summary"] = summary
        if launched_by is not UNSET:
            field_dict["launched_by"] = launched_by
        if status is not UNSET:
            field_dict["status"] = status
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_process_get_out import ExecutionProcessGetOut
        from ..models.executions_review_status_details import ExecutionsReviewStatusDetails
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)
        created_by = UserMetadata.from_dict(d.pop("created_by"))

        updated_by = UserMetadata.from_dict(d.pop("updated_by"))

        approvals_count = d.pop("approvals_count")

        processes_details = []
        _processes_details = d.pop("processes_details")
        for processes_details_item_data in _processes_details:
            processes_details_item = ExecutionProcessGetOut.from_dict(processes_details_item_data)

            processes_details.append(processes_details_item)

        review_status = ExecutionsReviewStatusDetails.from_dict(d.pop("review_status"))

        execution_group = UUID(d.pop("execution_group"))

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        def _parse_memo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        memo = _parse_memo(d.pop("memo", UNSET))

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary = _parse_summary(d.pop("summary", UNSET))

        def _parse_launched_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                launched_by_type_0 = UUID(data)

                return launched_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        launched_by = _parse_launched_by(d.pop("launched_by", UNSET))

        status = d.pop("status", UNSET)

        def _parse_start_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_time_type_0 = isoparse(data)

                return start_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_time = _parse_start_time(d.pop("start_time", UNSET))

        def _parse_end_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_type_0 = isoparse(data)

                return end_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_time = _parse_end_time(d.pop("end_time", UNSET))

        executions_get_out = cls(
            created_by=created_by,
            updated_by=updated_by,
            approvals_count=approvals_count,
            processes_details=processes_details,
            review_status=review_status,
            execution_group=execution_group,
            created=created,
            updated=updated,
            memo=memo,
            id=id,
            summary=summary,
            launched_by=launched_by,
            status=status,
            start_time=start_time,
            end_time=end_time,
        )

        executions_get_out.additional_properties = d
        return executions_get_out

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
