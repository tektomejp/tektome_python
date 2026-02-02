from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attribute_citation_schema_out import AttributeCitationSchemaOut
    from ..models.bim_citation_schema_out import BIMCitationSchemaOut
    from ..models.image_citation_schema_out import ImageCitationSchemaOut
    from ..models.pdf_citation_schema_out import PDFCitationSchemaOut
    from ..models.raw_text_citation_schema_out import RawTextCitationSchemaOut


T = TypeVar("T", bound="CitationsSchemaOut")


@_attrs_define
class CitationsSchemaOut:
    """
    Attributes:
        pdf_citations (list[PDFCitationSchemaOut] | None | Unset):
        rawtext_citations (list[RawTextCitationSchemaOut] | None | Unset):
        bim_citations (list[BIMCitationSchemaOut] | None | Unset):
        image_citations (list[ImageCitationSchemaOut] | None | Unset):
        attribute_citations (list[AttributeCitationSchemaOut] | None | Unset):
    """

    pdf_citations: list[PDFCitationSchemaOut] | None | Unset = UNSET
    rawtext_citations: list[RawTextCitationSchemaOut] | None | Unset = UNSET
    bim_citations: list[BIMCitationSchemaOut] | None | Unset = UNSET
    image_citations: list[ImageCitationSchemaOut] | None | Unset = UNSET
    attribute_citations: list[AttributeCitationSchemaOut] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pdf_citations: list[dict[str, Any]] | None | Unset
        if isinstance(self.pdf_citations, Unset):
            pdf_citations = UNSET
        elif isinstance(self.pdf_citations, list):
            pdf_citations = []
            for pdf_citations_type_0_item_data in self.pdf_citations:
                pdf_citations_type_0_item = pdf_citations_type_0_item_data.to_dict()
                pdf_citations.append(pdf_citations_type_0_item)

        else:
            pdf_citations = self.pdf_citations

        rawtext_citations: list[dict[str, Any]] | None | Unset
        if isinstance(self.rawtext_citations, Unset):
            rawtext_citations = UNSET
        elif isinstance(self.rawtext_citations, list):
            rawtext_citations = []
            for rawtext_citations_type_0_item_data in self.rawtext_citations:
                rawtext_citations_type_0_item = rawtext_citations_type_0_item_data.to_dict()
                rawtext_citations.append(rawtext_citations_type_0_item)

        else:
            rawtext_citations = self.rawtext_citations

        bim_citations: list[dict[str, Any]] | None | Unset
        if isinstance(self.bim_citations, Unset):
            bim_citations = UNSET
        elif isinstance(self.bim_citations, list):
            bim_citations = []
            for bim_citations_type_0_item_data in self.bim_citations:
                bim_citations_type_0_item = bim_citations_type_0_item_data.to_dict()
                bim_citations.append(bim_citations_type_0_item)

        else:
            bim_citations = self.bim_citations

        image_citations: list[dict[str, Any]] | None | Unset
        if isinstance(self.image_citations, Unset):
            image_citations = UNSET
        elif isinstance(self.image_citations, list):
            image_citations = []
            for image_citations_type_0_item_data in self.image_citations:
                image_citations_type_0_item = image_citations_type_0_item_data.to_dict()
                image_citations.append(image_citations_type_0_item)

        else:
            image_citations = self.image_citations

        attribute_citations: list[dict[str, Any]] | None | Unset
        if isinstance(self.attribute_citations, Unset):
            attribute_citations = UNSET
        elif isinstance(self.attribute_citations, list):
            attribute_citations = []
            for attribute_citations_type_0_item_data in self.attribute_citations:
                attribute_citations_type_0_item = attribute_citations_type_0_item_data.to_dict()
                attribute_citations.append(attribute_citations_type_0_item)

        else:
            attribute_citations = self.attribute_citations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pdf_citations is not UNSET:
            field_dict["pdf_citations"] = pdf_citations
        if rawtext_citations is not UNSET:
            field_dict["rawtext_citations"] = rawtext_citations
        if bim_citations is not UNSET:
            field_dict["bim_citations"] = bim_citations
        if image_citations is not UNSET:
            field_dict["image_citations"] = image_citations
        if attribute_citations is not UNSET:
            field_dict["attribute_citations"] = attribute_citations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attribute_citation_schema_out import AttributeCitationSchemaOut
        from ..models.bim_citation_schema_out import BIMCitationSchemaOut
        from ..models.image_citation_schema_out import ImageCitationSchemaOut
        from ..models.pdf_citation_schema_out import PDFCitationSchemaOut
        from ..models.raw_text_citation_schema_out import RawTextCitationSchemaOut

        d = dict(src_dict)

        def _parse_pdf_citations(data: object) -> list[PDFCitationSchemaOut] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                pdf_citations_type_0 = []
                _pdf_citations_type_0 = data
                for pdf_citations_type_0_item_data in _pdf_citations_type_0:
                    pdf_citations_type_0_item = PDFCitationSchemaOut.from_dict(pdf_citations_type_0_item_data)

                    pdf_citations_type_0.append(pdf_citations_type_0_item)

                return pdf_citations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PDFCitationSchemaOut] | None | Unset, data)

        pdf_citations = _parse_pdf_citations(d.pop("pdf_citations", UNSET))

        def _parse_rawtext_citations(data: object) -> list[RawTextCitationSchemaOut] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rawtext_citations_type_0 = []
                _rawtext_citations_type_0 = data
                for rawtext_citations_type_0_item_data in _rawtext_citations_type_0:
                    rawtext_citations_type_0_item = RawTextCitationSchemaOut.from_dict(
                        rawtext_citations_type_0_item_data
                    )

                    rawtext_citations_type_0.append(rawtext_citations_type_0_item)

                return rawtext_citations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RawTextCitationSchemaOut] | None | Unset, data)

        rawtext_citations = _parse_rawtext_citations(d.pop("rawtext_citations", UNSET))

        def _parse_bim_citations(data: object) -> list[BIMCitationSchemaOut] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                bim_citations_type_0 = []
                _bim_citations_type_0 = data
                for bim_citations_type_0_item_data in _bim_citations_type_0:
                    bim_citations_type_0_item = BIMCitationSchemaOut.from_dict(bim_citations_type_0_item_data)

                    bim_citations_type_0.append(bim_citations_type_0_item)

                return bim_citations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BIMCitationSchemaOut] | None | Unset, data)

        bim_citations = _parse_bim_citations(d.pop("bim_citations", UNSET))

        def _parse_image_citations(data: object) -> list[ImageCitationSchemaOut] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                image_citations_type_0 = []
                _image_citations_type_0 = data
                for image_citations_type_0_item_data in _image_citations_type_0:
                    image_citations_type_0_item = ImageCitationSchemaOut.from_dict(image_citations_type_0_item_data)

                    image_citations_type_0.append(image_citations_type_0_item)

                return image_citations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ImageCitationSchemaOut] | None | Unset, data)

        image_citations = _parse_image_citations(d.pop("image_citations", UNSET))

        def _parse_attribute_citations(data: object) -> list[AttributeCitationSchemaOut] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attribute_citations_type_0 = []
                _attribute_citations_type_0 = data
                for attribute_citations_type_0_item_data in _attribute_citations_type_0:
                    attribute_citations_type_0_item = AttributeCitationSchemaOut.from_dict(
                        attribute_citations_type_0_item_data
                    )

                    attribute_citations_type_0.append(attribute_citations_type_0_item)

                return attribute_citations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AttributeCitationSchemaOut] | None | Unset, data)

        attribute_citations = _parse_attribute_citations(d.pop("attribute_citations", UNSET))

        citations_schema_out = cls(
            pdf_citations=pdf_citations,
            rawtext_citations=rawtext_citations,
            bim_citations=bim_citations,
            image_citations=image_citations,
            attribute_citations=attribute_citations,
        )

        citations_schema_out.additional_properties = d
        return citations_schema_out

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
