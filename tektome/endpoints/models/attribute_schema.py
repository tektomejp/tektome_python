from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AttributeSchema")


@_attrs_define
class AttributeSchema:
    """
    Attributes:
        id (UUID):
        name (str):
        value (bool | float | int | list[Any] | str):
        operator (str):
        data_type (str):
    """

    id: UUID
    name: str
    value: bool | float | int | list[Any] | str
    operator: str
    data_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        value: bool | float | int | list[Any] | str
        if isinstance(self.value, list):
            value = self.value

        else:
            value = self.value

        operator = self.operator

        data_type = self.data_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "value": value,
                "operator": operator,
                "data_type": data_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        def _parse_value(data: object) -> bool | float | int | list[Any] | str:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_4 = cast(list[Any], data)

                return value_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | float | int | list[Any] | str, data)

        value = _parse_value(d.pop("value"))

        operator = d.pop("operator")

        data_type = d.pop("data_type")

        attribute_schema = cls(
            id=id,
            name=name,
            value=value,
            operator=operator,
            data_type=data_type,
        )

        attribute_schema.additional_properties = d
        return attribute_schema

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
