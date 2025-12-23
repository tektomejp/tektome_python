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
    from ..models.requirement_resource_capture_section_component_schema_positional_text_type_0 import (
        RequirementResourceCaptureSectionComponentSchemaPositionalTextType0,
    )


T = TypeVar("T", bound="RequirementResourceCaptureSectionComponentSchema")


@_attrs_define
class RequirementResourceCaptureSectionComponentSchema:
    """
    Attributes:
        screenshot_file (str):
        page_width (float):
        page_height (float):
        page_number (int):
        created (datetime.datetime):
        updated (datetime.datetime):
        bounding_geometry (list[Any]):
        id (None | Unset | UUID):
        positional_text (None | RequirementResourceCaptureSectionComponentSchemaPositionalTextType0 | Unset):
        requirement (None | Unset | UUID):
    """

    screenshot_file: str
    page_width: float
    page_height: float
    page_number: int
    created: datetime.datetime
    updated: datetime.datetime
    bounding_geometry: list[Any]
    id: None | Unset | UUID = UNSET
    positional_text: None | RequirementResourceCaptureSectionComponentSchemaPositionalTextType0 | Unset = UNSET
    requirement: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.requirement_resource_capture_section_component_schema_positional_text_type_0 import (
            RequirementResourceCaptureSectionComponentSchemaPositionalTextType0,
        )

        screenshot_file = self.screenshot_file

        page_width = self.page_width

        page_height = self.page_height

        page_number = self.page_number

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        bounding_geometry = self.bounding_geometry

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
        elif isinstance(self.positional_text, RequirementResourceCaptureSectionComponentSchemaPositionalTextType0):
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
                "screenshot_file": screenshot_file,
                "page_width": page_width,
                "page_height": page_height,
                "page_number": page_number,
                "created": created,
                "updated": updated,
                "bounding_geometry": bounding_geometry,
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
        from ..models.requirement_resource_capture_section_component_schema_positional_text_type_0 import (
            RequirementResourceCaptureSectionComponentSchemaPositionalTextType0,
        )

        d = dict(src_dict)
        screenshot_file = d.pop("screenshot_file")

        page_width = d.pop("page_width")

        page_height = d.pop("page_height")

        page_number = d.pop("page_number")

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        bounding_geometry = cast(list[Any], d.pop("bounding_geometry"))

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
        ) -> None | RequirementResourceCaptureSectionComponentSchemaPositionalTextType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                positional_text_type_0 = RequirementResourceCaptureSectionComponentSchemaPositionalTextType0.from_dict(
                    data
                )

                return positional_text_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RequirementResourceCaptureSectionComponentSchemaPositionalTextType0 | Unset, data)

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

        requirement_resource_capture_section_component_schema = cls(
            screenshot_file=screenshot_file,
            page_width=page_width,
            page_height=page_height,
            page_number=page_number,
            created=created,
            updated=updated,
            bounding_geometry=bounding_geometry,
            id=id,
            positional_text=positional_text,
            requirement=requirement,
        )

        requirement_resource_capture_section_component_schema.additional_properties = d
        return requirement_resource_capture_section_component_schema

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
