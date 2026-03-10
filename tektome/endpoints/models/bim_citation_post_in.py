from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attribute_type import AttributeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bim_element_in import BIMElementIn


T = TypeVar("T", bound="BIMCitationPostIn")


@_attrs_define
class BIMCitationPostIn:
    """
    Attributes:
        title (str):
        attribute_type (AttributeType): StrEnum for all available attribute types

            .. warning::
                Do not change the values of this enum, as they are used in the database.
                If you need to add a new attribute type, add a new enum value with a unique name.
        bim_resource_id (UUID): ID of the cited BIM resource.
        bim_elements (list[BIMElementIn]): List of BIM project/object pairs cited as sources.
        keywords (list[str] | Unset):
    """

    title: str
    attribute_type: AttributeType
    bim_resource_id: UUID
    bim_elements: list[BIMElementIn]
    keywords: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        attribute_type = self.attribute_type.value

        bim_resource_id = str(self.bim_resource_id)

        bim_elements = []
        for bim_elements_item_data in self.bim_elements:
            bim_elements_item = bim_elements_item_data.to_dict()
            bim_elements.append(bim_elements_item)

        keywords: list[str] | Unset = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "attribute_type": attribute_type,
                "bim_resource_id": bim_resource_id,
                "bim_elements": bim_elements,
            }
        )
        if keywords is not UNSET:
            field_dict["keywords"] = keywords

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bim_element_in import BIMElementIn

        d = dict(src_dict)
        title = d.pop("title")

        attribute_type = AttributeType(d.pop("attribute_type"))

        bim_resource_id = UUID(d.pop("bim_resource_id"))

        bim_elements = []
        _bim_elements = d.pop("bim_elements")
        for bim_elements_item_data in _bim_elements:
            bim_elements_item = BIMElementIn.from_dict(bim_elements_item_data)

            bim_elements.append(bim_elements_item)

        keywords = cast(list[str], d.pop("keywords", UNSET))

        bim_citation_post_in = cls(
            title=title,
            attribute_type=attribute_type,
            bim_resource_id=bim_resource_id,
            bim_elements=bim_elements,
            keywords=keywords,
        )

        bim_citation_post_in.additional_properties = d
        return bim_citation_post_in

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
