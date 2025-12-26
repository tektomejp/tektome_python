from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bim_trim_query_item import BimTrimQueryItem


T = TypeVar("T", bound="BimBatchTrimElementRequestPostIn")


@_attrs_define
class BimBatchTrimElementRequestPostIn:
    """Schema for batch BIM element retrieval with trimming request

    Attributes:
        ids (list[str]): List of BIM element IDs to retrieve
        trim_query (BimTrimQueryItem):
    """

    ids: list[str]
    trim_query: BimTrimQueryItem
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ids = self.ids

        trim_query = self.trim_query.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ids": ids,
                "trim_query": trim_query,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bim_trim_query_item import BimTrimQueryItem

        d = dict(src_dict)
        ids = cast(list[str], d.pop("ids"))

        trim_query = BimTrimQueryItem.from_dict(d.pop("trim_query"))

        bim_batch_trim_element_request_post_in = cls(
            ids=ids,
            trim_query=trim_query,
        )

        bim_batch_trim_element_request_post_in.additional_properties = d
        return bim_batch_trim_element_request_post_in

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
