from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BIMElementRequest")


@_attrs_define
class BIMElementRequest:
    """
    Attributes:
        bim_project_id (UUID):
        bim_object_id (None | str | Unset):
    """

    bim_project_id: UUID
    bim_object_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bim_project_id = str(self.bim_project_id)

        bim_object_id: None | str | Unset
        if isinstance(self.bim_object_id, Unset):
            bim_object_id = UNSET
        else:
            bim_object_id = self.bim_object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bim_project_id": bim_project_id,
            }
        )
        if bim_object_id is not UNSET:
            field_dict["bim_object_id"] = bim_object_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bim_project_id = UUID(d.pop("bim_project_id"))

        def _parse_bim_object_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bim_object_id = _parse_bim_object_id(d.pop("bim_object_id", UNSET))

        bim_element_request = cls(
            bim_project_id=bim_project_id,
            bim_object_id=bim_object_id,
        )

        bim_element_request.additional_properties = d
        return bim_element_request

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
