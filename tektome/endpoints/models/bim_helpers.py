from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bim_helpers_bim_helper_elements_item import BIMHelpersBimHelperElementsItem


T = TypeVar("T", bound="BIMHelpers")


@_attrs_define
class BIMHelpers:
    """
    Attributes:
        bim_uuid (str): UUID of the BIM project in which to insert helpers, or alternatively the BIM object UUID
        bim_helper_elements (list[BIMHelpersBimHelperElementsItem]): List of BIM elements created by LLM for the BIM
            project. Use existing BIM objects as references for the JSON schema.
    """

    bim_uuid: str
    bim_helper_elements: list[BIMHelpersBimHelperElementsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bim_uuid = self.bim_uuid

        bim_helper_elements = []
        for bim_helper_elements_item_data in self.bim_helper_elements:
            bim_helper_elements_item = bim_helper_elements_item_data.to_dict()
            bim_helper_elements.append(bim_helper_elements_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bim_uuid": bim_uuid,
                "bim_helper_elements": bim_helper_elements,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bim_helpers_bim_helper_elements_item import BIMHelpersBimHelperElementsItem

        d = dict(src_dict)
        bim_uuid = d.pop("bim_uuid")

        bim_helper_elements = []
        _bim_helper_elements = d.pop("bim_helper_elements")
        for bim_helper_elements_item_data in _bim_helper_elements:
            bim_helper_elements_item = BIMHelpersBimHelperElementsItem.from_dict(bim_helper_elements_item_data)

            bim_helper_elements.append(bim_helper_elements_item)

        bim_helpers = cls(
            bim_uuid=bim_uuid,
            bim_helper_elements=bim_helper_elements,
        )

        bim_helpers.additional_properties = d
        return bim_helpers

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
