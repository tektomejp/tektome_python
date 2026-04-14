from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attribute_type import AttributeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bim_annotation_request import BIMAnnotationRequest
    from ..models.bim_element_request import BIMElementRequest
    from ..models.create_bim_citation_request_resolved_element_map import CreateBIMCitationRequestResolvedElementMap


T = TypeVar("T", bound="CreateBIMCitationRequest")


@_attrs_define
class CreateBIMCitationRequest:
    """
    Attributes:
        attribute_type (AttributeType): Enumeration of supported attribute types.
        bim_resource_id (UUID): ID of the cited BIM resource.
        bim_elements (list[BIMElementRequest]): List of BIM project/object pairs cited as sources.
        title (None | str | Unset):
        overlay_html (None | str | Unset):
        keywords (list[str] | Unset):
        bim_annotations (list[BIMAnnotationRequest] | Unset): List of standalone BIM objects to annotate on this
            citation.
        resolved_element_map (CreateBIMCitationRequestResolvedElementMap | Unset):
    """

    attribute_type: AttributeType
    bim_resource_id: UUID
    bim_elements: list[BIMElementRequest]
    title: None | str | Unset = UNSET
    overlay_html: None | str | Unset = UNSET
    keywords: list[str] | Unset = UNSET
    bim_annotations: list[BIMAnnotationRequest] | Unset = UNSET
    resolved_element_map: CreateBIMCitationRequestResolvedElementMap | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attribute_type = self.attribute_type.value

        bim_resource_id = str(self.bim_resource_id)

        bim_elements = []
        for bim_elements_item_data in self.bim_elements:
            bim_elements_item = bim_elements_item_data.to_dict()
            bim_elements.append(bim_elements_item)

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        overlay_html: None | str | Unset
        if isinstance(self.overlay_html, Unset):
            overlay_html = UNSET
        else:
            overlay_html = self.overlay_html

        keywords: list[str] | Unset = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords

        bim_annotations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bim_annotations, Unset):
            bim_annotations = []
            for bim_annotations_item_data in self.bim_annotations:
                bim_annotations_item = bim_annotations_item_data.to_dict()
                bim_annotations.append(bim_annotations_item)

        resolved_element_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resolved_element_map, Unset):
            resolved_element_map = self.resolved_element_map.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attribute_type": attribute_type,
                "bim_resource_id": bim_resource_id,
                "bim_elements": bim_elements,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if overlay_html is not UNSET:
            field_dict["overlay_html"] = overlay_html
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if bim_annotations is not UNSET:
            field_dict["bim_annotations"] = bim_annotations
        if resolved_element_map is not UNSET:
            field_dict["resolved_element_map"] = resolved_element_map

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bim_annotation_request import BIMAnnotationRequest
        from ..models.bim_element_request import BIMElementRequest
        from ..models.create_bim_citation_request_resolved_element_map import CreateBIMCitationRequestResolvedElementMap

        d = dict(src_dict)
        attribute_type = AttributeType(d.pop("attribute_type"))

        bim_resource_id = UUID(d.pop("bim_resource_id"))

        bim_elements = []
        _bim_elements = d.pop("bim_elements")
        for bim_elements_item_data in _bim_elements:
            bim_elements_item = BIMElementRequest.from_dict(bim_elements_item_data)

            bim_elements.append(bim_elements_item)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_overlay_html(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        overlay_html = _parse_overlay_html(d.pop("overlay_html", UNSET))

        keywords = cast(list[str], d.pop("keywords", UNSET))

        _bim_annotations = d.pop("bim_annotations", UNSET)
        bim_annotations: list[BIMAnnotationRequest] | Unset = UNSET
        if _bim_annotations is not UNSET:
            bim_annotations = []
            for bim_annotations_item_data in _bim_annotations:
                bim_annotations_item = BIMAnnotationRequest.from_dict(bim_annotations_item_data)

                bim_annotations.append(bim_annotations_item)

        _resolved_element_map = d.pop("resolved_element_map", UNSET)
        resolved_element_map: CreateBIMCitationRequestResolvedElementMap | Unset
        if isinstance(_resolved_element_map, Unset):
            resolved_element_map = UNSET
        else:
            resolved_element_map = CreateBIMCitationRequestResolvedElementMap.from_dict(_resolved_element_map)

        create_bim_citation_request = cls(
            attribute_type=attribute_type,
            bim_resource_id=bim_resource_id,
            bim_elements=bim_elements,
            title=title,
            overlay_html=overlay_html,
            keywords=keywords,
            bim_annotations=bim_annotations,
            resolved_element_map=resolved_element_map,
        )

        create_bim_citation_request.additional_properties = d
        return create_bim_citation_request

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
