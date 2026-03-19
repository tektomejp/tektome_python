from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bim_key_value_search_item_post_out_result import BimKeyValueSearchItemPostOutResult


T = TypeVar("T", bound="BimKeyValueSearchItemPostOut")


@_attrs_define
class BimKeyValueSearchItemPostOut:
    """Schema for a single key-value search result.

    Attributes:
        id (str):
        result (BimKeyValueSearchItemPostOutResult):
    """

    id: str
    result: BimKeyValueSearchItemPostOutResult
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        result = self.result.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "result": result,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bim_key_value_search_item_post_out_result import BimKeyValueSearchItemPostOutResult

        d = dict(src_dict)
        id = d.pop("id")

        result = BimKeyValueSearchItemPostOutResult.from_dict(d.pop("result"))

        bim_key_value_search_item_post_out = cls(
            id=id,
            result=result,
        )

        bim_key_value_search_item_post_out.additional_properties = d
        return bim_key_value_search_item_post_out

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
