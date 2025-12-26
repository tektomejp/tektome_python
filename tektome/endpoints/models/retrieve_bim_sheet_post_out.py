from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.retrieve_bim_sheet_post_out_data_item_type_1 import RetrieveBimSheetPostOutDataItemType1


T = TypeVar("T", bound="RetrieveBimSheetPostOut")


@_attrs_define
class RetrieveBimSheetPostOut:
    """
    Attributes:
        data (list[RetrieveBimSheetPostOutDataItemType1 | str]):
    """

    data: list[RetrieveBimSheetPostOutDataItemType1 | str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.retrieve_bim_sheet_post_out_data_item_type_1 import RetrieveBimSheetPostOutDataItemType1

        data = []
        for data_item_data in self.data:
            data_item: dict[str, Any] | str
            if isinstance(data_item_data, RetrieveBimSheetPostOutDataItemType1):
                data_item = data_item_data.to_dict()
            else:
                data_item = data_item_data
            data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.retrieve_bim_sheet_post_out_data_item_type_1 import RetrieveBimSheetPostOutDataItemType1

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:

            def _parse_data_item(data: object) -> RetrieveBimSheetPostOutDataItemType1 | str:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_1 = RetrieveBimSheetPostOutDataItemType1.from_dict(data)

                    return data_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(RetrieveBimSheetPostOutDataItemType1 | str, data)

            data_item = _parse_data_item(data_item_data)

            data.append(data_item)

        retrieve_bim_sheet_post_out = cls(
            data=data,
        )

        retrieve_bim_sheet_post_out.additional_properties = d
        return retrieve_bim_sheet_post_out

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
