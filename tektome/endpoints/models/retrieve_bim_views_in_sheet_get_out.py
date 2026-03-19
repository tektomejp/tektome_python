from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.retrieve_bim_views_in_sheet_get_out_data_item_type_1 import RetrieveBimViewsInSheetGetOutDataItemType1


T = TypeVar("T", bound="RetrieveBimViewsInSheetGetOut")


@_attrs_define
class RetrieveBimViewsInSheetGetOut:
    """
    Attributes:
        data (list[RetrieveBimViewsInSheetGetOutDataItemType1 | str]):
        error (None | str | Unset):
    """

    data: list[RetrieveBimViewsInSheetGetOutDataItemType1 | str]
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.retrieve_bim_views_in_sheet_get_out_data_item_type_1 import (
            RetrieveBimViewsInSheetGetOutDataItemType1,
        )

        data = []
        for data_item_data in self.data:
            data_item: dict[str, Any] | str
            if isinstance(data_item_data, RetrieveBimViewsInSheetGetOutDataItemType1):
                data_item = data_item_data.to_dict()
            else:
                data_item = data_item_data
            data.append(data_item)

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.retrieve_bim_views_in_sheet_get_out_data_item_type_1 import (
            RetrieveBimViewsInSheetGetOutDataItemType1,
        )

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:

            def _parse_data_item(data: object) -> RetrieveBimViewsInSheetGetOutDataItemType1 | str:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_1 = RetrieveBimViewsInSheetGetOutDataItemType1.from_dict(data)

                    return data_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(RetrieveBimViewsInSheetGetOutDataItemType1 | str, data)

            data_item = _parse_data_item(data_item_data)

            data.append(data_item)

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        retrieve_bim_views_in_sheet_get_out = cls(
            data=data,
            error=error,
        )

        retrieve_bim_views_in_sheet_get_out.additional_properties = d
        return retrieve_bim_views_in_sheet_get_out

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
