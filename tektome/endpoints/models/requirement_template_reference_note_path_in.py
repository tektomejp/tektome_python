from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RequirementTemplateReferenceNotePathIn")


@_attrs_define
class RequirementTemplateReferenceNotePathIn:
    """Path parameters for Requirement Template operations.

    Attributes:
        reference_note_template_id (UUID):
    """

    reference_note_template_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reference_note_template_id = str(self.reference_note_template_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reference_note_template_id": reference_note_template_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reference_note_template_id = UUID(d.pop("reference_note_template_id"))

        requirement_template_reference_note_path_in = cls(
            reference_note_template_id=reference_note_template_id,
        )

        requirement_template_reference_note_path_in.additional_properties = d
        return requirement_template_reference_note_path_in

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
