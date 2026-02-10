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
    from ..models.execute_process_payload_out import ExecuteProcessPayloadOut


T = TypeVar("T", bound="ExecutionGroupProcessesMetadataGetOut")


@_attrs_define
class ExecutionGroupProcessesMetadataGetOut:
    """Serializer for ExecutionGroup metadata details

    Attributes:
        processes (list[ExecuteProcessPayloadOut]):
        created (datetime.datetime):
        updated (datetime.datetime):
        id (None | Unset | UUID):
        memo (None | str | Unset): A description of the purpose of this execution group
        auto_approved_output (bool | Unset): Indicates if the outputs will be auto-approved Default: False.
        start_time (datetime.datetime | None | Unset):
        end_time (datetime.datetime | None | Unset):
    """

    processes: list[ExecuteProcessPayloadOut]
    created: datetime.datetime
    updated: datetime.datetime
    id: None | Unset | UUID = UNSET
    memo: None | str | Unset = UNSET
    auto_approved_output: bool | Unset = False
    start_time: datetime.datetime | None | Unset = UNSET
    end_time: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        processes = []
        for processes_item_data in self.processes:
            processes_item = processes_item_data.to_dict()
            processes.append(processes_item)

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

        auto_approved_output = self.auto_approved_output

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
                "processes": processes,
                "created": created,
                "updated": updated,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if memo is not UNSET:
            field_dict["memo"] = memo
        if auto_approved_output is not UNSET:
            field_dict["auto_approved_output"] = auto_approved_output
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execute_process_payload_out import ExecuteProcessPayloadOut

        d = dict(src_dict)
        processes = []
        _processes = d.pop("processes")
        for processes_item_data in _processes:
            processes_item = ExecuteProcessPayloadOut.from_dict(processes_item_data)

            processes.append(processes_item)

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

        auto_approved_output = d.pop("auto_approved_output", UNSET)

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

        execution_group_processes_metadata_get_out = cls(
            processes=processes,
            created=created,
            updated=updated,
            id=id,
            memo=memo,
            auto_approved_output=auto_approved_output,
            start_time=start_time,
            end_time=end_time,
        )

        execution_group_processes_metadata_get_out.additional_properties = d
        return execution_group_processes_metadata_get_out

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
