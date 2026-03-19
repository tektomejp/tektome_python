from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.citations_query_request_order_by import CitationsQueryRequestOrderBy
from ..models.citations_sort_keys import CitationsSortKeys
from ..types import UNSET, Unset

T = TypeVar("T", bound="CitationsQueryRequest")


@_attrs_define
class CitationsQueryRequest:
    """
    Attributes:
        sort_by (CitationsSortKeys | None | Unset):
        order_by (CitationsQueryRequestOrderBy | Unset):  Default: CitationsQueryRequestOrderBy.DESC.
    """

    sort_by: CitationsSortKeys | None | Unset = UNSET
    order_by: CitationsQueryRequestOrderBy | Unset = CitationsQueryRequestOrderBy.DESC
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sort_by: None | str | Unset
        if isinstance(self.sort_by, Unset):
            sort_by = UNSET
        elif isinstance(self.sort_by, CitationsSortKeys):
            sort_by = self.sort_by.value
        else:
            sort_by = self.sort_by

        order_by: str | Unset = UNSET
        if not isinstance(self.order_by, Unset):
            order_by = self.order_by.value

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

        def _parse_sort_by(data: object) -> CitationsSortKeys | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sort_by_type_0 = CitationsSortKeys(data)

                return sort_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CitationsSortKeys | None | Unset, data)

        sort_by = _parse_sort_by(d.pop("sort_by", UNSET))

        _order_by = d.pop("order_by", UNSET)
        order_by: CitationsQueryRequestOrderBy | Unset
        if isinstance(_order_by, Unset):
            order_by = UNSET
        else:
            order_by = CitationsQueryRequestOrderBy(_order_by)

        citations_query_request = cls(
            sort_by=sort_by,
            order_by=order_by,
        )

        citations_query_request.additional_properties = d
        return citations_query_request

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
