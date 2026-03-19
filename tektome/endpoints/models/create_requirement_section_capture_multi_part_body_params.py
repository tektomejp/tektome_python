from __future__ import annotations

import json
from collections.abc import Mapping
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import File

if TYPE_CHECKING:
    from ..models.create_capture_section_component_post_in import CreateCaptureSectionComponentPostIn


T = TypeVar("T", bound="CreateRequirementSectionCaptureMultiPartBodyParams")


@_attrs_define
class CreateRequirementSectionCaptureMultiPartBodyParams:
    """
    Attributes:
        screenshot_file (File):
        payload (CreateCaptureSectionComponentPostIn):
    """

    screenshot_file: File
    payload: CreateCaptureSectionComponentPostIn
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        screenshot_file = self.screenshot_file.to_tuple()

        payload = self.payload.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "screenshot_file": screenshot_file,
                "payload": payload,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("screenshot_file", self.screenshot_file.to_tuple()))

        files.append(("payload", (None, json.dumps(self.payload.to_dict()).encode(), "application/json")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_capture_section_component_post_in import CreateCaptureSectionComponentPostIn

        d = dict(src_dict)
        screenshot_file = File(payload=BytesIO(d.pop("screenshot_file")))

        payload = CreateCaptureSectionComponentPostIn.from_dict(d.pop("payload"))

        create_requirement_section_capture_multi_part_body_params = cls(
            screenshot_file=screenshot_file,
            payload=payload,
        )

        create_requirement_section_capture_multi_part_body_params.additional_properties = d
        return create_requirement_section_capture_multi_part_body_params

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
