from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.search_document_result_post_out_result_item import SearchDocumentResultPostOutResultItem


T = TypeVar("T", bound="SearchDocumentResultPostOut")


@_attrs_define
class SearchDocumentResultPostOut:
    """
    Attributes:
        result (list[SearchDocumentResultPostOutResultItem]):
    """

    result: list[SearchDocumentResultPostOutResultItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        result = []
        for result_item_data in self.result:
            result_item = result_item_data.to_dict()
            result.append(result_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "result": result,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_document_result_post_out_result_item import SearchDocumentResultPostOutResultItem

        d = dict(src_dict)
        result = []
        _result = d.pop("result")
        for result_item_data in _result:
            result_item = SearchDocumentResultPostOutResultItem.from_dict(result_item_data)

            result.append(result_item)

        search_document_result_post_out = cls(
            result=result,
        )

        search_document_result_post_out.additional_properties = d
        return search_document_result_post_out

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
