from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="TableCell")


@_attrs_define
class TableCell:
    """A cell in a table, identified by its column name and holding a value.

    Attributes:
        column (str):
        value (bool | datetime.date | datetime.datetime | float | int | None | str):
    """

    column: str
    value: bool | datetime.date | datetime.datetime | float | int | None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        column = self.column

        value: bool | float | int | None | str
        if isinstance(self.value, datetime.date):
            value = self.value.isoformat()
        elif isinstance(self.value, datetime.datetime):
            value = self.value.isoformat()
        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "column": column,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        column = d.pop("column")

        def _parse_value(data: object) -> bool | datetime.date | datetime.datetime | float | int | None | str:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_date_time_type_type_0 = isoparse(data).date()

                return componentsschemas_date_time_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_date_time_type_type_1 = isoparse(data)

                return componentsschemas_date_time_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | datetime.date | datetime.datetime | float | int | None | str, data)

        value = _parse_value(d.pop("value"))

        table_cell = cls(
            column=column,
            value=value,
        )

        table_cell.additional_properties = d
        return table_cell

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
