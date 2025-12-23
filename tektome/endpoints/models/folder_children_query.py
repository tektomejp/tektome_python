from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.order_by import OrderBy
from ..types import UNSET, Unset

T = TypeVar("T", bound="FolderChildrenQuery")


@_attrs_define
class FolderChildrenQuery:
    """
    Attributes:
        sort_by (str | Unset):  Default: 'name'.
        order_by (None | OrderBy | Unset):  Default: OrderBy.ASCENDING.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 10.
        dataspace_id (None | Unset | UUID):
    """

    sort_by: str | Unset = "name"
    order_by: None | OrderBy | Unset = OrderBy.ASCENDING
    page: int | Unset = 1
    page_size: int | Unset = 10
    dataspace_id: None | Unset | UUID = UNSET
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

        page = self.page

        page_size = self.page_size

        dataspace_id: None | str | Unset
        if isinstance(self.dataspace_id, Unset):
            dataspace_id = UNSET
        elif isinstance(self.dataspace_id, UUID):
            dataspace_id = str(self.dataspace_id)
        else:
            dataspace_id = self.dataspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sort_by is not UNSET:
            field_dict["sort_by"] = sort_by
        if order_by is not UNSET:
            field_dict["order_by"] = order_by
        if page is not UNSET:
            field_dict["page"] = page
        if page_size is not UNSET:
            field_dict["page_size"] = page_size
        if dataspace_id is not UNSET:
            field_dict["dataspace_id"] = dataspace_id

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

        page = d.pop("page", UNSET)

        page_size = d.pop("page_size", UNSET)

        def _parse_dataspace_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dataspace_id_type_0 = UUID(data)

                return dataspace_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        dataspace_id = _parse_dataspace_id(d.pop("dataspace_id", UNSET))

        folder_children_query = cls(
            sort_by=sort_by,
            order_by=order_by,
            page=page,
            page_size=page_size,
            dataspace_id=dataspace_id,
        )

        folder_children_query.additional_properties = d
        return folder_children_query

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
