from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.operators_type_1 import OperatorsType1

T = TypeVar("T", bound="LawtalkListStringAttributeSchema")


@_attrs_define
class LawtalkListStringAttributeSchema:
    """
    Attributes:
        name (str):
        value (list[str]):
        operator (None | OperatorsType1):
    """

    name: str
    value: list[str]
    operator: None | OperatorsType1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        value = self.value

        operator: None | str
        if isinstance(self.operator, OperatorsType1):
            operator = self.operator.value
        else:
            operator = self.operator

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "value": value,
                "operator": operator,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        value = cast(list[str], d.pop("value"))

        def _parse_operator(data: object) -> None | OperatorsType1:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_operators_type_1 = OperatorsType1(data)

                return componentsschemas_operators_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OperatorsType1, data)

        operator = _parse_operator(d.pop("operator"))

        lawtalk_list_string_attribute_schema = cls(
            name=name,
            value=value,
            operator=operator,
        )

        lawtalk_list_string_attribute_schema.additional_properties = d
        return lawtalk_list_string_attribute_schema

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
