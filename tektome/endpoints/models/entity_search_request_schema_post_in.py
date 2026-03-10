from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.entity_type import EntityType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dynamic_entity_search_request import DynamicEntitySearchRequest


T = TypeVar("T", bound="EntitySearchRequestSchemaPostIn")


@_attrs_define
class EntitySearchRequestSchemaPostIn:
    """
    Attributes:
        name (str):
        conditions (DynamicEntitySearchRequest): Search request for entity searches with dynamic conditions.
        description (None | str | Unset):
        entity_type (EntityType | Unset):  Default: EntityType.PROJECT.
    """

    name: str
    conditions: DynamicEntitySearchRequest
    description: None | str | Unset = UNSET
    entity_type: EntityType | Unset = EntityType.PROJECT
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        conditions = self.conditions.to_dict()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        entity_type: str | Unset = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "conditions": conditions,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if entity_type is not UNSET:
            field_dict["entity_type"] = entity_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dynamic_entity_search_request import DynamicEntitySearchRequest

        d = dict(src_dict)
        name = d.pop("name")

        conditions = DynamicEntitySearchRequest.from_dict(d.pop("conditions"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _entity_type = d.pop("entity_type", UNSET)
        entity_type: EntityType | Unset
        if isinstance(_entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = EntityType(_entity_type)

        entity_search_request_schema_post_in = cls(
            name=name,
            conditions=conditions,
            description=description,
            entity_type=entity_type,
        )

        entity_search_request_schema_post_in.additional_properties = d
        return entity_search_request_schema_post_in

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
