from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.recipeschoices import RECIPESCHOICES
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attribute import Attribute


T = TypeVar("T", bound="ExtractionPostIn")


@_attrs_define
class ExtractionPostIn:
    """
    Attributes:
        section_id (UUID): Section ID
        recipe (RECIPESCHOICES):
        attributes (list[Attribute]):
        enduser_prompt (str): User prompt for the entire extraction, appended to the user prompt
        include_pdf_pages_as_images (bool | Unset):  Default: False.
        for_approval (bool | Unset): Whether the extraction results should be marked as pending approval before being
            finalized. Default: False.
    """

    section_id: UUID
    recipe: RECIPESCHOICES
    attributes: list[Attribute]
    enduser_prompt: str
    include_pdf_pages_as_images: bool | Unset = False
    for_approval: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        section_id = str(self.section_id)

        recipe = self.recipe.value

        attributes = []
        for attributes_item_data in self.attributes:
            attributes_item = attributes_item_data.to_dict()
            attributes.append(attributes_item)

        enduser_prompt = self.enduser_prompt

        include_pdf_pages_as_images = self.include_pdf_pages_as_images

        for_approval = self.for_approval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "section_id": section_id,
                "recipe": recipe,
                "attributes": attributes,
                "enduser_prompt": enduser_prompt,
            }
        )
        if include_pdf_pages_as_images is not UNSET:
            field_dict["include_pdf_pages_as_images"] = include_pdf_pages_as_images
        if for_approval is not UNSET:
            field_dict["for_approval"] = for_approval

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attribute import Attribute

        d = dict(src_dict)
        section_id = UUID(d.pop("section_id"))

        recipe = RECIPESCHOICES(d.pop("recipe"))

        attributes = []
        _attributes = d.pop("attributes")
        for attributes_item_data in _attributes:
            attributes_item = Attribute.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        enduser_prompt = d.pop("enduser_prompt")

        include_pdf_pages_as_images = d.pop("include_pdf_pages_as_images", UNSET)

        for_approval = d.pop("for_approval", UNSET)

        extraction_post_in = cls(
            section_id=section_id,
            recipe=recipe,
            attributes=attributes,
            enduser_prompt=enduser_prompt,
            include_pdf_pages_as_images=include_pdf_pages_as_images,
            for_approval=for_approval,
        )

        extraction_post_in.additional_properties = d
        return extraction_post_in

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
