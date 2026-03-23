from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionAttributeMetadata")


@_attrs_define
class ExecutionAttributeMetadata:
    """Schema for execution attribute.

    Attributes:
        model_entity_ids (list[UUID] | Unset): The UUID of the entity model. Can either be a project or resource model.
    """

    model_entity_ids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_entity_ids: list[str] | Unset = UNSET
        if not isinstance(self.model_entity_ids, Unset):
            model_entity_ids = []
            for model_entity_ids_item_data in self.model_entity_ids:
                model_entity_ids_item = str(model_entity_ids_item_data)
                model_entity_ids.append(model_entity_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if model_entity_ids is not UNSET:
            field_dict["model_entity_ids"] = model_entity_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _model_entity_ids = d.pop("model_entity_ids", UNSET)
        model_entity_ids: list[UUID] | Unset = UNSET
        if _model_entity_ids is not UNSET:
            model_entity_ids = []
            for model_entity_ids_item_data in _model_entity_ids:
                model_entity_ids_item = UUID(model_entity_ids_item_data)

                model_entity_ids.append(model_entity_ids_item)

        execution_attribute_metadata = cls(
            model_entity_ids=model_entity_ids,
        )

        execution_attribute_metadata.additional_properties = d
        return execution_attribute_metadata

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
