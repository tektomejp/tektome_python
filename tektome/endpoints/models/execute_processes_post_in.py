from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execute_process_post_in import ExecuteProcessPostIn


T = TypeVar("T", bound="ExecuteProcessesPostIn")


@_attrs_define
class ExecuteProcessesPostIn:
    """
    Attributes:
        processes (list[ExecuteProcessPostIn]):
        auto_approved_output (bool | Unset):  Default: False.
        memo (None | str | Unset):
    """

    processes: list[ExecuteProcessPostIn]
    auto_approved_output: bool | Unset = False
    memo: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        processes = []
        for processes_item_data in self.processes:
            processes_item = processes_item_data.to_dict()
            processes.append(processes_item)

        auto_approved_output = self.auto_approved_output

        memo: None | str | Unset
        if isinstance(self.memo, Unset):
            memo = UNSET
        else:
            memo = self.memo

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "processes": processes,
            }
        )
        if auto_approved_output is not UNSET:
            field_dict["auto_approved_output"] = auto_approved_output
        if memo is not UNSET:
            field_dict["memo"] = memo

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execute_process_post_in import ExecuteProcessPostIn

        d = dict(src_dict)
        processes = []
        _processes = d.pop("processes")
        for processes_item_data in _processes:
            processes_item = ExecuteProcessPostIn.from_dict(processes_item_data)

            processes.append(processes_item)

        auto_approved_output = d.pop("auto_approved_output", UNSET)

        def _parse_memo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        memo = _parse_memo(d.pop("memo", UNSET))

        execute_processes_post_in = cls(
            processes=processes,
            auto_approved_output=auto_approved_output,
            memo=memo,
        )

        execute_processes_post_in.additional_properties = d
        return execute_processes_post_in

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
