from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.coordinate import Coordinate


T = TypeVar("T", bound="PolygonAttributeSchemaIn")


@_attrs_define
class PolygonAttributeSchemaIn:
    """
    Attributes:
        name (str):
        value (list[Coordinate]):
    """

    name: str
    value: list[Coordinate]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        value = []
        for componentsschemas_polygon_item_data in self.value:
            componentsschemas_polygon_item = componentsschemas_polygon_item_data.to_dict()
            value.append(componentsschemas_polygon_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.coordinate import Coordinate

        d = dict(src_dict)
        name = d.pop("name")

        value = []
        _value = d.pop("value")
        for componentsschemas_polygon_item_data in _value:
            componentsschemas_polygon_item = Coordinate.from_dict(componentsschemas_polygon_item_data)

            value.append(componentsschemas_polygon_item)

        polygon_attribute_schema_in = cls(
            name=name,
            value=value,
        )

        polygon_attribute_schema_in.additional_properties = d
        return polygon_attribute_schema_in

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
