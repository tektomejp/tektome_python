from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attribute_type import AttributeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateRawTextCitationRequest")


@_attrs_define
class CreateRawTextCitationRequest:
    """Raw text citation input schema.

    Attributes:
        attribute_type (AttributeType): Enumeration of supported attribute types.
        resource_id (UUID): ID of the cited RawText resource.
        title (None | str | Unset):
        overlay_html (None | str | Unset):
        keywords (list[str] | Unset):
    """

    attribute_type: AttributeType
    resource_id: UUID
    title: None | str | Unset = UNSET
    overlay_html: None | str | Unset = UNSET
    keywords: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attribute_type = self.attribute_type.value

        resource_id = str(self.resource_id)

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attribute_type": attribute_type,
                "resource_id": resource_id,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if overlay_html is not UNSET:
            field_dict["overlay_html"] = overlay_html
        if keywords is not UNSET:
            field_dict["keywords"] = keywords

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attribute_type = AttributeType(d.pop("attribute_type"))

        resource_id = UUID(d.pop("resource_id"))

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

        create_raw_text_citation_request = cls(
            attribute_type=attribute_type,
            resource_id=resource_id,
            title=title,
            overlay_html=overlay_html,
            keywords=keywords,
        )

        create_raw_text_citation_request.additional_properties = d
        return create_raw_text_citation_request

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
