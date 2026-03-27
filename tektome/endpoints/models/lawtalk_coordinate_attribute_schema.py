from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.operators import Operators

if TYPE_CHECKING:
    from ..models.coordinate import Coordinate


T = TypeVar("T", bound="LawtalkCoordinateAttributeSchema")


@_attrs_define
class LawtalkCoordinateAttributeSchema:
    """
    Attributes:
        name (str):
        value (Coordinate):
        operator (None | Operators):
    """

    name: str
    value: Coordinate
    operator: None | Operators
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        value = self.value.to_dict()

        operator: None | str
        if isinstance(self.operator, Operators):
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
        from ..models.coordinate import Coordinate

        d = dict(src_dict)
        name = d.pop("name")

        value = Coordinate.from_dict(d.pop("value"))

        def _parse_operator(data: object) -> None | Operators:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_operators_type_1 = Operators(data)

                return componentsschemas_operators_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Operators, data)

        operator = _parse_operator(d.pop("operator"))

        lawtalk_coordinate_attribute_schema = cls(
            name=name,
            value=value,
            operator=operator,
        )

        lawtalk_coordinate_attribute_schema.additional_properties = d
        return lawtalk_coordinate_attribute_schema

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
