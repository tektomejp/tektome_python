from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.simple_attribute_type import SimpleAttributeType
from ..models.table_condition_action import TableConditionAction

if TYPE_CHECKING:
    from ..models.cell_coordinate import CellCoordinate


T = TypeVar("T", bound="TableSearchCondition")


@_attrs_define
class TableSearchCondition:
    """Data Model for table conditions. Expect attribute_type to be "table"

    Attributes:
        attribute_name (str): The name of the attribute to filter on
        attribute_type (Literal['table']): The type of the attribute being filtered (table)
        action (TableConditionAction): Allowed actions for table conditions.
            - column_contains (For example: column "age" contains value 30)
            - cell_matches (For example: cell at (column "age", row 0) matches value 30)
        key (CellCoordinate | int | str): The key to filter by (e.g., column name, row index, or cell coordinate)
        value (bool | datetime.date | datetime.datetime | float | int | str):
        value_type (SimpleAttributeType):
    """

    attribute_name: str
    attribute_type: Literal["table"]
    action: TableConditionAction
    key: CellCoordinate | int | str
    value: bool | datetime.date | datetime.datetime | float | int | str
    value_type: SimpleAttributeType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.cell_coordinate import CellCoordinate

        attribute_name = self.attribute_name

        attribute_type = self.attribute_type

        action = self.action.value

        key: dict[str, Any] | int | str
        if isinstance(self.key, CellCoordinate):
            key = self.key.to_dict()
        else:
            key = self.key

        value: bool | float | int | str
        if isinstance(self.value, datetime.date):
            value = self.value.isoformat()
        elif isinstance(self.value, datetime.datetime):
            value = self.value.isoformat()
        else:
            value = self.value

        value_type = self.value_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attribute_name": attribute_name,
                "attribute_type": attribute_type,
                "action": action,
                "key": key,
                "value": value,
                "value_type": value_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cell_coordinate import CellCoordinate

        d = dict(src_dict)
        attribute_name = d.pop("attribute_name")

        attribute_type = cast(Literal["table"], d.pop("attribute_type"))
        if attribute_type != "table":
            raise ValueError(f"attribute_type must match const 'table', got '{attribute_type}'")

        action = TableConditionAction(d.pop("action"))

        def _parse_key(data: object) -> CellCoordinate | int | str:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                key_type_2 = CellCoordinate.from_dict(data)

                return key_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CellCoordinate | int | str, data)

        key = _parse_key(d.pop("key"))

        def _parse_value(data: object) -> bool | datetime.date | datetime.datetime | float | int | str:
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
            return cast(bool | datetime.date | datetime.datetime | float | int | str, data)

        value = _parse_value(d.pop("value"))

        value_type = SimpleAttributeType(d.pop("value_type"))

        table_search_condition = cls(
            attribute_name=attribute_name,
            attribute_type=attribute_type,
            action=action,
            key=key,
            value=value,
            value_type=value_type,
        )

        table_search_condition.additional_properties = d
        return table_search_condition

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
