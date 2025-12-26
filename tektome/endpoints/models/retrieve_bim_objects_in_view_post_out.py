from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.retrieve_bim_objects_in_view_post_out_data_type_1_item import (
        RetrieveBimObjectsInViewPostOutDataType1Item,
    )


T = TypeVar("T", bound="RetrieveBimObjectsInViewPostOut")


@_attrs_define
class RetrieveBimObjectsInViewPostOut:
    """
    Attributes:
        data (list[RetrieveBimObjectsInViewPostOutDataType1Item] | list[str]):
    """

    data: list[RetrieveBimObjectsInViewPostOutDataType1Item] | list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | list[str]
        if isinstance(self.data, list):
            data = self.data

        else:
            data = []
            for data_type_1_item_data in self.data:
                data_type_1_item = data_type_1_item_data.to_dict()
                data.append(data_type_1_item)

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
        from ..models.retrieve_bim_objects_in_view_post_out_data_type_1_item import (
            RetrieveBimObjectsInViewPostOutDataType1Item,
        )

        d = dict(src_dict)

        def _parse_data(data: object) -> list[RetrieveBimObjectsInViewPostOutDataType1Item] | list[str]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_type_0 = cast(list[str], data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            data_type_1 = []
            _data_type_1 = data
            for data_type_1_item_data in _data_type_1:
                data_type_1_item = RetrieveBimObjectsInViewPostOutDataType1Item.from_dict(data_type_1_item_data)

                data_type_1.append(data_type_1_item)

            return data_type_1

        data = _parse_data(d.pop("data"))

        retrieve_bim_objects_in_view_post_out = cls(
            data=data,
        )

        retrieve_bim_objects_in_view_post_out.additional_properties = d
        return retrieve_bim_objects_in_view_post_out

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
