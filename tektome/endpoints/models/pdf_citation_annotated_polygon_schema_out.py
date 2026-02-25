from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PDFCitationAnnotatedPolygonSchemaOut")


@_attrs_define
class PDFCitationAnnotatedPolygonSchemaOut:
    """
    Attributes:
        bounding_geometry (list[Any]):
        page_number (int):
        capture (None | str | Unset):
        id (None | Unset | UUID):
        status (str | Unset): The status of the polygon capture whether the image capture has been generated Default:
            'pending'.
    """

    bounding_geometry: list[Any]
    page_number: int
    capture: None | str | Unset = UNSET
    id: None | Unset | UUID = UNSET
    status: str | Unset = "pending"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bounding_geometry = self.bounding_geometry

        page_number = self.page_number

        capture: None | str | Unset
        if isinstance(self.capture, Unset):
            capture = UNSET
        else:
            capture = self.capture

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bounding_geometry": bounding_geometry,
                "page_number": page_number,
            }
        )
        if capture is not UNSET:
            field_dict["capture"] = capture
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bounding_geometry = cast(list[Any], d.pop("bounding_geometry"))

        page_number = d.pop("page_number")

        def _parse_capture(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        capture = _parse_capture(d.pop("capture", UNSET))

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

        status = d.pop("status", UNSET)

        pdf_citation_annotated_polygon_schema_out = cls(
            bounding_geometry=bounding_geometry,
            page_number=page_number,
            capture=capture,
            id=id,
            status=status,
        )

        pdf_citation_annotated_polygon_schema_out.additional_properties = d
        return pdf_citation_annotated_polygon_schema_out

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
