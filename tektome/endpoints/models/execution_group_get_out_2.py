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
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="ExecutionGroupGetOut2")


@_attrs_define
class ExecutionGroupGetOut2:
    """Serializer for ExecutionGroup details

    Attributes:
        created_by (UserMetadata):
        updated_by (UserMetadata):
        launched_by (UserMetadata):
        approvals_count (int):
        executions_count (int):
        created (datetime.datetime):
        updated (datetime.datetime):
        id (None | Unset | UUID):
        memo (None | str | Unset): A description of the purpose of this execution group
        status (str | Unset): The status of the execution group (e.g., Initializing, Running, Completed, Failed)
            Default: 'initializing'.
        start_time (datetime.datetime | None | Unset):
        end_time (datetime.datetime | None | Unset):
    """

    created_by: UserMetadata
    updated_by: UserMetadata
    launched_by: UserMetadata
    approvals_count: int
    executions_count: int
    created: datetime.datetime
    updated: datetime.datetime
    id: None | Unset | UUID = UNSET
    memo: None | str | Unset = UNSET
    status: str | Unset = "initializing"
    start_time: datetime.datetime | None | Unset = UNSET
    end_time: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_by = self.created_by.to_dict()

        updated_by = self.updated_by.to_dict()

        launched_by = self.launched_by.to_dict()

        approvals_count = self.approvals_count

        executions_count = self.executions_count

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        memo: None | str | Unset
        if isinstance(self.memo, Unset):
            memo = UNSET
        else:
            memo = self.memo

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
                "launched_by": launched_by,
                "approvals_count": approvals_count,
                "executions_count": executions_count,
                "created": created,
                "updated": updated,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if memo is not UNSET:
            field_dict["memo"] = memo
        if status is not UNSET:
            field_dict["status"] = status
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)
        created_by = UserMetadata.from_dict(d.pop("created_by"))

        updated_by = UserMetadata.from_dict(d.pop("updated_by"))

        launched_by = UserMetadata.from_dict(d.pop("launched_by"))

        approvals_count = d.pop("approvals_count")

        executions_count = d.pop("executions_count")

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

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

        def _parse_memo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        memo = _parse_memo(d.pop("memo", UNSET))

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

        execution_group_get_out_2 = cls(
            created_by=created_by,
            updated_by=updated_by,
            launched_by=launched_by,
            approvals_count=approvals_count,
            executions_count=executions_count,
            created=created,
            updated=updated,
            id=id,
            memo=memo,
            status=status,
            start_time=start_time,
            end_time=end_time,
        )

        execution_group_get_out_2.additional_properties = d
        return execution_group_get_out_2

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
