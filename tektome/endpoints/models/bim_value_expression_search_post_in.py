from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BimValueExpressionSearchPostIn")


@_attrs_define
class BimValueExpressionSearchPostIn:
    r"""Input schema for boolean value expression search.

    Attributes:
        query (str): Boolean value expression to search for across all keys. Supports AND, OR, NOT operators,
            parenthesised grouping, wildcards (*), and quoted multi-word values. Examples: "Walls AND NOT Curtain*", "(Door
            OR Window) AND 2100", "value1 AND \"multi word\"". Operator precedence: NOT > AND > OR. Adjacent terms without
            an operator are implicitly ANDed.
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

        bim_value_expression_search_post_in = cls(
            query=query,
        )

        bim_value_expression_search_post_in.additional_properties = d
        return bim_value_expression_search_post_in

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
