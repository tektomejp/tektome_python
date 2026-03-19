from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.resource_get_many_schema_post_out_items import ResourceGetManySchemaPostOutItems


T = TypeVar("T", bound="ResourceGetManySchemaPostOut")


@_attrs_define
class ResourceGetManySchemaPostOut:
    """
    Attributes:
        items (ResourceGetManySchemaPostOutItems):
    """

    items: ResourceGetManySchemaPostOutItems
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items = self.items.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_get_many_schema_post_out_items import ResourceGetManySchemaPostOutItems

        d = dict(src_dict)
        items = ResourceGetManySchemaPostOutItems.from_dict(d.pop("items"))

        resource_get_many_schema_post_out = cls(
            items=items,
        )

        resource_get_many_schema_post_out.additional_properties = d
        return resource_get_many_schema_post_out

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
