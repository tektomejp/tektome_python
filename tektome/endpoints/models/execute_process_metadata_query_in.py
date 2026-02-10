from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.execute_metadata_kind import ExecuteMetadataKind

T = TypeVar("T", bound="ExecuteProcessMetadataQueryIn")


@_attrs_define
class ExecuteProcessMetadataQueryIn:
    """
    Attributes:
        kind (ExecuteMetadataKind):
        model_entity_ids (list[UUID]):
    """

    kind: ExecuteMetadataKind
    model_entity_ids: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        model_entity_ids = []
        for model_entity_ids_item_data in self.model_entity_ids:
            model_entity_ids_item = str(model_entity_ids_item_data)
            model_entity_ids.append(model_entity_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "model_entity_ids": model_entity_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = ExecuteMetadataKind(d.pop("kind"))

        model_entity_ids = []
        _model_entity_ids = d.pop("model_entity_ids")
        for model_entity_ids_item_data in _model_entity_ids:
            model_entity_ids_item = UUID(model_entity_ids_item_data)

            model_entity_ids.append(model_entity_ids_item)

        execute_process_metadata_query_in = cls(
            kind=kind,
            model_entity_ids=model_entity_ids,
        )

        execute_process_metadata_query_in.additional_properties = d
        return execute_process_metadata_query_in

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
