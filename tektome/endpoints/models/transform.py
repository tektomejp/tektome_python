from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Transform")


@_attrs_define
class Transform:
    """
    Attributes:
        id (str):
        speckle_type (str):
        matrix (list[float]):
    """

    id: str
    speckle_type: str
    matrix: list[float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        speckle_type = self.speckle_type

        matrix = self.matrix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "speckle_type": speckle_type,
                "matrix": matrix,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        speckle_type = d.pop("speckle_type")

        matrix = cast(list[float], d.pop("matrix"))

        transform = cls(
            id=id,
            speckle_type=speckle_type,
            matrix=matrix,
        )

        transform.additional_properties = d
        return transform

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
