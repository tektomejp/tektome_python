from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.supported_dr_model import SupportedDRModel


T = TypeVar("T", bound="GetSupportedDRModelsGetOut")


@_attrs_define
class GetSupportedDRModelsGetOut:
    """
    Attributes:
        supported_models (list[SupportedDRModel]): List of supported deep research models with their web search
            capability.
    """

    supported_models: list[SupportedDRModel]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        supported_models = []
        for supported_models_item_data in self.supported_models:
            supported_models_item = supported_models_item_data.to_dict()
            supported_models.append(supported_models_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "supported_models": supported_models,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.supported_dr_model import SupportedDRModel

        d = dict(src_dict)
        supported_models = []
        _supported_models = d.pop("supported_models")
        for supported_models_item_data in _supported_models:
            supported_models_item = SupportedDRModel.from_dict(supported_models_item_data)

            supported_models.append(supported_models_item)

        get_supported_dr_models_get_out = cls(
            supported_models=supported_models,
        )

        get_supported_dr_models_get_out.additional_properties = d
        return get_supported_dr_models_get_out

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
