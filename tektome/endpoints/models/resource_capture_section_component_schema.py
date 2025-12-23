from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_capture_section_component_schema_positional_text_type_0 import (
        ResourceCaptureSectionComponentSchemaPositionalTextType0,
    )


T = TypeVar("T", bound="ResourceCaptureSectionComponentSchema")


@_attrs_define
class ResourceCaptureSectionComponentSchema:
    """
    Attributes:
        page_number (int):
        created (datetime.datetime):
        updated (datetime.datetime):
        screenshot_file (str):
        bounding_geometry (list[Any]):
        section (UUID):
        id (None | Unset | UUID):
        positional_text (None | ResourceCaptureSectionComponentSchemaPositionalTextType0 | Unset):
        requirement (None | Unset | UUID):
    """

    page_number: int
    created: datetime.datetime
    updated: datetime.datetime
    screenshot_file: str
    bounding_geometry: list[Any]
    section: UUID
    id: None | Unset | UUID = UNSET
    positional_text: None | ResourceCaptureSectionComponentSchemaPositionalTextType0 | Unset = UNSET
    requirement: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.resource_capture_section_component_schema_positional_text_type_0 import (
            ResourceCaptureSectionComponentSchemaPositionalTextType0,
        )

        page_number = self.page_number

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        screenshot_file = self.screenshot_file

        bounding_geometry = self.bounding_geometry

        section = str(self.section)

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        positional_text: dict[str, Any] | None | Unset
        if isinstance(self.positional_text, Unset):
            positional_text = UNSET
        elif isinstance(self.positional_text, ResourceCaptureSectionComponentSchemaPositionalTextType0):
            positional_text = self.positional_text.to_dict()
        else:
            positional_text = self.positional_text

        requirement: None | str | Unset
        if isinstance(self.requirement, Unset):
            requirement = UNSET
        elif isinstance(self.requirement, UUID):
            requirement = str(self.requirement)
        else:
            requirement = self.requirement

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page_number": page_number,
                "created": created,
                "updated": updated,
                "screenshot_file": screenshot_file,
                "bounding_geometry": bounding_geometry,
                "section": section,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if positional_text is not UNSET:
            field_dict["positional_text"] = positional_text
        if requirement is not UNSET:
            field_dict["requirement"] = requirement

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_capture_section_component_schema_positional_text_type_0 import (
            ResourceCaptureSectionComponentSchemaPositionalTextType0,
        )

        d = dict(src_dict)
        page_number = d.pop("page_number")

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        screenshot_file = d.pop("screenshot_file")

        bounding_geometry = cast(list[Any], d.pop("bounding_geometry"))

        section = UUID(d.pop("section"))

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

        def _parse_positional_text(
            data: object,
        ) -> None | ResourceCaptureSectionComponentSchemaPositionalTextType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                positional_text_type_0 = ResourceCaptureSectionComponentSchemaPositionalTextType0.from_dict(data)

                return positional_text_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResourceCaptureSectionComponentSchemaPositionalTextType0 | Unset, data)

        positional_text = _parse_positional_text(d.pop("positional_text", UNSET))

        def _parse_requirement(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                requirement_type_0 = UUID(data)

                return requirement_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        requirement = _parse_requirement(d.pop("requirement", UNSET))

        resource_capture_section_component_schema = cls(
            page_number=page_number,
            created=created,
            updated=updated,
            screenshot_file=screenshot_file,
            bounding_geometry=bounding_geometry,
            section=section,
            id=id,
            positional_text=positional_text,
            requirement=requirement,
        )

        resource_capture_section_component_schema.additional_properties = d
        return resource_capture_section_component_schema

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
