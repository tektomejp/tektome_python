from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.order_by import OrderBy
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataspaceEntityListQuery")


@_attrs_define
class DataspaceEntityListQuery:
    """Schema for querying projects in a dataspace.

    Attributes:
        sort_by (str | Unset):  Default: 'name'.
        order_by (None | OrderBy | Unset):  Default: OrderBy.ASCENDING.
    """

    sort_by: str | Unset = "name"
    order_by: None | OrderBy | Unset = OrderBy.ASCENDING
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sort_by = self.sort_by

        order_by: None | str | Unset
        if isinstance(self.order_by, Unset):
            order_by = UNSET
        elif isinstance(self.order_by, OrderBy):
            order_by = self.order_by.value
        else:
            order_by = self.order_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sort_by is not UNSET:
            field_dict["sort_by"] = sort_by
        if order_by is not UNSET:
            field_dict["order_by"] = order_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sort_by = d.pop("sort_by", UNSET)

        def _parse_order_by(data: object) -> None | OrderBy | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                order_by_type_0 = OrderBy(data)

                return order_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OrderBy | Unset, data)

        order_by = _parse_order_by(d.pop("order_by", UNSET))

        dataspace_entity_list_query = cls(
            sort_by=sort_by,
            order_by=order_by,
        )

        dataspace_entity_list_query.additional_properties = d
        return dataspace_entity_list_query

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
