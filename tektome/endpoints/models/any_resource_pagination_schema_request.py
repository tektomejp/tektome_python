from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnyResourcePaginationSchemaRequest")


@_attrs_define
class AnyResourcePaginationSchemaRequest:
    """Query schema for resource-scoped endpoints with bounded pagination.

    Includes:
    - `resource_id` existence validation from `AnyResourceSchemaIn`
    - `page` and `page_size` bounds validation from `BoundedPaginationQueryIn`

        Attributes:
            resource_id (UUID):
            page (int | Unset):  Default: 1.
            page_size (int | Unset):  Default: 100.
    """

    resource_id: UUID
    page: int | Unset = 1
    page_size: int | Unset = 100
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_id = str(self.resource_id)

        page = self.page

        page_size = self.page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_id": resource_id,
            }
        )
        if page is not UNSET:
            field_dict["page"] = page
        if page_size is not UNSET:
            field_dict["page_size"] = page_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_id = UUID(d.pop("resource_id"))

        page = d.pop("page", UNSET)

        page_size = d.pop("page_size", UNSET)

        any_resource_pagination_schema_request = cls(
            resource_id=resource_id,
            page=page,
            page_size=page_size,
        )

        any_resource_pagination_schema_request.additional_properties = d
        return any_resource_pagination_schema_request

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
