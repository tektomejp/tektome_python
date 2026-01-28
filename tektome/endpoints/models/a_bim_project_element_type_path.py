from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bim_element_type_v2_path import BimElementTypeV2Path

T = TypeVar("T", bound="ABimProjectElementTypePath")


@_attrs_define
class ABimProjectElementTypePath:
    """Async path parameters for BIM element operations with project validation.

    Attributes:
        bim_project_id (UUID):
        bim_type (BimElementTypeV2Path): An enumeration representing different BIM (Building Information Modeling)
            element types for V2 API paths.

            Attributes:
                OBJECT (str): Represents a BIM object element type, mapped to the string "bim-object".
                VIEW (str): Represents a BIM view element type, mapped to the string "bim-view".
                SHEET (str): Represents a BIM sheet element type, mapped to the string "bim-sheet".

            Methods:
                resolve_bim_element_class(bim_element):
                    Resolves and returns the corresponding document class for a given BIM element type.
    """

    bim_project_id: UUID
    bim_type: BimElementTypeV2Path
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bim_project_id = str(self.bim_project_id)

        bim_type = self.bim_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bim_project_id": bim_project_id,
                "bim_type": bim_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bim_project_id = UUID(d.pop("bim_project_id"))

        bim_type = BimElementTypeV2Path(d.pop("bim_type"))

        a_bim_project_element_type_path = cls(
            bim_project_id=bim_project_id,
            bim_type=bim_type,
        )

        a_bim_project_element_type_path.additional_properties = d
        return a_bim_project_element_type_path

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
