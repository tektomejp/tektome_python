from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.recipeschoices import RECIPESCHOICES
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attribute import Attribute


T = TypeVar("T", bound="CreateExtractionRequest")


@_attrs_define
class CreateExtractionRequest:
    """
    Attributes:
        section_id (UUID): Section ID
        recipe (RECIPESCHOICES):
        attributes (list[Attribute]):
        enduser_prompt (str): User prompt for the entire extraction, appended to the user prompt
        include_pdf_pages_as_images (bool | Unset):  Default: False.
        for_approval (bool | Unset): Whether the extraction results should be marked as pending approval before being
            finalized. Default: False.
        execution_id (None | Unset | UUID): The execution ID to associate LLM usage with, when triggered from a
            dataspace execution.
    """

    section_id: UUID
    recipe: RECIPESCHOICES
    attributes: list[Attribute]
    enduser_prompt: str
    include_pdf_pages_as_images: bool | Unset = False
    for_approval: bool | Unset = False
    execution_id: None | Unset | UUID = UNSET
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

        execution_id: None | str | Unset
        if isinstance(self.execution_id, Unset):
            execution_id = UNSET
        elif isinstance(self.execution_id, UUID):
            execution_id = str(self.execution_id)
        else:
            execution_id = self.execution_id

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
        if execution_id is not UNSET:
            field_dict["execution_id"] = execution_id

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

        def _parse_execution_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                execution_id_type_0 = UUID(data)

                return execution_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        execution_id = _parse_execution_id(d.pop("execution_id", UNSET))

        create_extraction_request = cls(
            section_id=section_id,
            recipe=recipe,
            attributes=attributes,
            enduser_prompt=enduser_prompt,
            include_pdf_pages_as_images=include_pdf_pages_as_images,
            for_approval=for_approval,
            execution_id=execution_id,
        )

        create_extraction_request.additional_properties = d
        return create_extraction_request

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
