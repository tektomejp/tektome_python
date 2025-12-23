from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.entity_type import EntityType

if TYPE_CHECKING:
    from ..models.entity_search_result_hit import EntitySearchResultHit


T = TypeVar("T", bound="EntitySearchResult")


@_attrs_define
class EntitySearchResult:
    """Model for entity search result

    Attributes:
        entity_type (EntityType):
        total (int): The total number of hits
        hits (list[EntitySearchResultHit]): The list of search hits
    """

    entity_type: EntityType
    total: int
    hits: list[EntitySearchResultHit]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity_type = self.entity_type.value

        total = self.total

        hits = []
        for hits_item_data in self.hits:
            hits_item = hits_item_data.to_dict()
            hits.append(hits_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entity_type": entity_type,
                "total": total,
                "hits": hits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_search_result_hit import EntitySearchResultHit

        d = dict(src_dict)
        entity_type = EntityType(d.pop("entity_type"))

        total = d.pop("total")

        hits = []
        _hits = d.pop("hits")
        for hits_item_data in _hits:
            hits_item = EntitySearchResultHit.from_dict(hits_item_data)

            hits.append(hits_item)

        entity_search_result = cls(
            entity_type=entity_type,
            total=total,
            hits=hits,
        )

        entity_search_result.additional_properties = d
        return entity_search_result

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
