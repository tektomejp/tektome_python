from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template_override_input_schema_properties_type_0 import TemplateOverrideInputSchemaPropertiesType0


T = TypeVar("T", bound="TemplateOverrideInputSchema")


@_attrs_define
class TemplateOverrideInputSchema:
    """
    Attributes:
        required (list[str] | None | Unset):
        properties (None | TemplateOverrideInputSchemaPropertiesType0 | Unset):
    """

    required: list[str] | None | Unset = UNSET
    properties: None | TemplateOverrideInputSchemaPropertiesType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.template_override_input_schema_properties_type_0 import TemplateOverrideInputSchemaPropertiesType0

        required: list[str] | None | Unset
        if isinstance(self.required, Unset):
            required = UNSET
        elif isinstance(self.required, list):
            required = self.required

        else:
            required = self.required

        properties: dict[str, Any] | None | Unset
        if isinstance(self.properties, Unset):
            properties = UNSET
        elif isinstance(self.properties, TemplateOverrideInputSchemaPropertiesType0):
            properties = self.properties.to_dict()
        else:
            properties = self.properties

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if required is not UNSET:
            field_dict["required"] = required
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_override_input_schema_properties_type_0 import TemplateOverrideInputSchemaPropertiesType0

        d = dict(src_dict)

        def _parse_required(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                required_type_0 = cast(list[str], data)

                return required_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        required = _parse_required(d.pop("required", UNSET))

        def _parse_properties(data: object) -> None | TemplateOverrideInputSchemaPropertiesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_0 = TemplateOverrideInputSchemaPropertiesType0.from_dict(data)

                return properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TemplateOverrideInputSchemaPropertiesType0 | Unset, data)

        properties = _parse_properties(d.pop("properties", UNSET))

        template_override_input_schema = cls(
            required=required,
            properties=properties,
        )

        template_override_input_schema.additional_properties = d
        return template_override_input_schema

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
