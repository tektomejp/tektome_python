from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SupportedDRModel")


@_attrs_define
class SupportedDRModel:
    """
    Attributes:
        model_name (str): Name of the deep research model.
        supports_web_search (bool): Indicates if the model supports web search functionality.
    """

    model_name: str
    supports_web_search: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_name = self.model_name

        supports_web_search = self.supports_web_search

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model_name": model_name,
                "supports_web_search": supports_web_search,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model_name = d.pop("model_name")

        supports_web_search = d.pop("supports_web_search")

        supported_dr_model = cls(
            model_name=model_name,
            supports_web_search=supports_web_search,
        )

        supported_dr_model.additional_properties = d
        return supported_dr_model

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
