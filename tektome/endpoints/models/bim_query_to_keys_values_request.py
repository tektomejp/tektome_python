from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BimQueryToKeysValuesRequest")


@_attrs_define
class BimQueryToKeysValuesRequest:
    """Schema for validating BIM query input to retrieve key-value embeddings.

    This schema ensures that a query string is provided and non-empty before
    processing BIM key-value embedding requests.

    Attributes:
        query (str): The query string used to search or filter BIM key-value data.

    Raises:
        BimKeyValueError: If the query field is empty or not provided.

        Attributes:
            query (str):
    """

    query: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query")

        bim_query_to_keys_values_request = cls(
            query=query,
        )

        bim_query_to_keys_values_request.additional_properties = d
        return bim_query_to_keys_values_request

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
