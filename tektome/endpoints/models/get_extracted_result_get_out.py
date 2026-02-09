from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attribute_extraction_status_choices import AttributeExtractionStatusChoices

T = TypeVar("T", bound="GetExtractedResultGetOut")


@_attrs_define
class GetExtractedResultGetOut:
    """
    Attributes:
        extraction_status (AttributeExtractionStatusChoices):
        value (Any | None): The extracted value of the attribute.
        error_message (None | str): The optional error message
        reasoning (None | str): The optional reasoning behind the extracted value.
        cited_attributes (list[UUID]): The IDs of the cited attributes used for extraction.
        cited_pdf_resource_ids (list[UUID]): The PDF resource IDs cited by the attribute.
        cited_raw_text_ids (list[UUID]): The raw text resource IDs cited by the attribute.
        cited_bim_project_ids (list[UUID]): The BIM project IDs cited by the attribute.
        cited_image_resource_ids (list[UUID]): The image resource IDs cited by the attribute.
    """

    extraction_status: AttributeExtractionStatusChoices
    value: Any | None
    error_message: None | str
    reasoning: None | str
    cited_attributes: list[UUID]
    cited_pdf_resource_ids: list[UUID]
    cited_raw_text_ids: list[UUID]
    cited_bim_project_ids: list[UUID]
    cited_image_resource_ids: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extraction_status = self.extraction_status.value

        value: Any | None
        value = self.value

        error_message: None | str
        error_message = self.error_message

        reasoning: None | str
        reasoning = self.reasoning

        cited_attributes = []
        for cited_attributes_item_data in self.cited_attributes:
            cited_attributes_item = str(cited_attributes_item_data)
            cited_attributes.append(cited_attributes_item)

        cited_pdf_resource_ids = []
        for cited_pdf_resource_ids_item_data in self.cited_pdf_resource_ids:
            cited_pdf_resource_ids_item = str(cited_pdf_resource_ids_item_data)
            cited_pdf_resource_ids.append(cited_pdf_resource_ids_item)

        cited_raw_text_ids = []
        for cited_raw_text_ids_item_data in self.cited_raw_text_ids:
            cited_raw_text_ids_item = str(cited_raw_text_ids_item_data)
            cited_raw_text_ids.append(cited_raw_text_ids_item)

        cited_bim_project_ids = []
        for cited_bim_project_ids_item_data in self.cited_bim_project_ids:
            cited_bim_project_ids_item = str(cited_bim_project_ids_item_data)
            cited_bim_project_ids.append(cited_bim_project_ids_item)

        cited_image_resource_ids = []
        for cited_image_resource_ids_item_data in self.cited_image_resource_ids:
            cited_image_resource_ids_item = str(cited_image_resource_ids_item_data)
            cited_image_resource_ids.append(cited_image_resource_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "extraction_status": extraction_status,
                "value": value,
                "error_message": error_message,
                "reasoning": reasoning,
                "cited_attributes": cited_attributes,
                "cited_pdf_resource_ids": cited_pdf_resource_ids,
                "cited_raw_text_ids": cited_raw_text_ids,
                "cited_bim_project_ids": cited_bim_project_ids,
                "cited_image_resource_ids": cited_image_resource_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        extraction_status = AttributeExtractionStatusChoices(d.pop("extraction_status"))

        def _parse_value(data: object) -> Any | None:
            if data is None:
                return data
            return cast(Any | None, data)

        value = _parse_value(d.pop("value"))

        def _parse_error_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error_message = _parse_error_message(d.pop("error_message"))

        def _parse_reasoning(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reasoning = _parse_reasoning(d.pop("reasoning"))

        cited_attributes = []
        _cited_attributes = d.pop("cited_attributes")
        for cited_attributes_item_data in _cited_attributes:
            cited_attributes_item = UUID(cited_attributes_item_data)

            cited_attributes.append(cited_attributes_item)

        cited_pdf_resource_ids = []
        _cited_pdf_resource_ids = d.pop("cited_pdf_resource_ids")
        for cited_pdf_resource_ids_item_data in _cited_pdf_resource_ids:
            cited_pdf_resource_ids_item = UUID(cited_pdf_resource_ids_item_data)

            cited_pdf_resource_ids.append(cited_pdf_resource_ids_item)

        cited_raw_text_ids = []
        _cited_raw_text_ids = d.pop("cited_raw_text_ids")
        for cited_raw_text_ids_item_data in _cited_raw_text_ids:
            cited_raw_text_ids_item = UUID(cited_raw_text_ids_item_data)

            cited_raw_text_ids.append(cited_raw_text_ids_item)

        cited_bim_project_ids = []
        _cited_bim_project_ids = d.pop("cited_bim_project_ids")
        for cited_bim_project_ids_item_data in _cited_bim_project_ids:
            cited_bim_project_ids_item = UUID(cited_bim_project_ids_item_data)

            cited_bim_project_ids.append(cited_bim_project_ids_item)

        cited_image_resource_ids = []
        _cited_image_resource_ids = d.pop("cited_image_resource_ids")
        for cited_image_resource_ids_item_data in _cited_image_resource_ids:
            cited_image_resource_ids_item = UUID(cited_image_resource_ids_item_data)

            cited_image_resource_ids.append(cited_image_resource_ids_item)

        get_extracted_result_get_out = cls(
            extraction_status=extraction_status,
            value=value,
            error_message=error_message,
            reasoning=reasoning,
            cited_attributes=cited_attributes,
            cited_pdf_resource_ids=cited_pdf_resource_ids,
            cited_raw_text_ids=cited_raw_text_ids,
            cited_bim_project_ids=cited_bim_project_ids,
            cited_image_resource_ids=cited_image_resource_ids,
        )

        get_extracted_result_get_out.additional_properties = d
        return get_extracted_result_get_out

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
