from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataspace_search_request_query_in_target_entity import DataspaceSearchRequestQueryInTargetEntity


T = TypeVar("T", bound="DataspaceSearchRequestQueryIn")


@_attrs_define
class DataspaceSearchRequestQueryIn:
    """Query parameters for search request endpoints

    Attributes:
        target_entity (DataspaceSearchRequestQueryInTargetEntity | Unset): Target entity type to search (project or
            resource)
        page (int | Unset): Page number for pagination Default: 1.
        page_size (int | Unset): Page size for pagination Default: 30.
    """

    target_entity: DataspaceSearchRequestQueryInTargetEntity | Unset = UNSET
    page: int | Unset = 1
    page_size: int | Unset = 30
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_entity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target_entity, Unset):
            target_entity = self.target_entity.to_dict()

        page = self.page

        page_size = self.page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target_entity is not UNSET:
            field_dict["target_entity"] = target_entity
        if page is not UNSET:
            field_dict["page"] = page
        if page_size is not UNSET:
            field_dict["page_size"] = page_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataspace_search_request_query_in_target_entity import DataspaceSearchRequestQueryInTargetEntity

        d = dict(src_dict)
        _target_entity = d.pop("target_entity", UNSET)
        target_entity: DataspaceSearchRequestQueryInTargetEntity | Unset
        if isinstance(_target_entity, Unset):
            target_entity = UNSET
        else:
            target_entity = DataspaceSearchRequestQueryInTargetEntity.from_dict(_target_entity)

        page = d.pop("page", UNSET)

        page_size = d.pop("page_size", UNSET)

        dataspace_search_request_query_in = cls(
            target_entity=target_entity,
            page=page,
            page_size=page_size,
        )

        dataspace_search_request_query_in.additional_properties = d
        return dataspace_search_request_query_in

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
