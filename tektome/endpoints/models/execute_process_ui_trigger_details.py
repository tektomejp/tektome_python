from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.process_type_choices import ProcessTypeChoices
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecuteProcessUITriggerDetails")


@_attrs_define
class ExecuteProcessUITriggerDetails:
    """Validation schema for UI trigger details in individual process execution payload. This can either be Resource or
    Project

        Attributes:
            id (UUID):
            name (str):
            type_ (None | ProcessTypeChoices | Unset):
    """

    id: UUID
    name: str
    type_: None | ProcessTypeChoices | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, ProcessTypeChoices):
            type_ = self.type_.value
        else:
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        def _parse_type_(data: object) -> None | ProcessTypeChoices | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_0 = ProcessTypeChoices(data)

                return type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProcessTypeChoices | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        execute_process_ui_trigger_details = cls(
            id=id,
            name=name,
            type_=type_,
        )

        execute_process_ui_trigger_details.additional_properties = d
        return execute_process_ui_trigger_details

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
