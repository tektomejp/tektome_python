from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.json_attribute_schema_request_value import JSONAttributeSchemaRequestValue


T = TypeVar("T", bound="JSONAttributeSchemaRequest")


@_attrs_define
class JSONAttributeSchemaRequest:
    """
    Attributes:
        name (str):
        value (JSONAttributeSchemaRequestValue):
    """

    name: str
    value: JSONAttributeSchemaRequestValue
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        value = self.value.to_dict()

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
        from ..models.json_attribute_schema_request_value import JSONAttributeSchemaRequestValue

        d = dict(src_dict)
        name = d.pop("name")

        value = JSONAttributeSchemaRequestValue.from_dict(d.pop("value"))

        json_attribute_schema_request = cls(
            name=name,
            value=value,
        )

        json_attribute_schema_request.additional_properties = d
        return json_attribute_schema_request

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
