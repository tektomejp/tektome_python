from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RenderMaterial")


@_attrs_define
class RenderMaterial:
    """
    Attributes:
        id (str):
        speckle_type (str):
        opacity (float):
        metalness (float):
        roughness (float):
        diffuse (float):
        emissive (float):
        name (None | str | Unset):
    """

    id: str
    speckle_type: str
    opacity: float
    metalness: float
    roughness: float
    diffuse: float
    emissive: float
    name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        speckle_type = self.speckle_type

        opacity = self.opacity

        metalness = self.metalness

        roughness = self.roughness

        diffuse = self.diffuse

        emissive = self.emissive

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "speckle_type": speckle_type,
                "opacity": opacity,
                "metalness": metalness,
                "roughness": roughness,
                "diffuse": diffuse,
                "emissive": emissive,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        speckle_type = d.pop("speckle_type")

        opacity = d.pop("opacity")

        metalness = d.pop("metalness")

        roughness = d.pop("roughness")

        diffuse = d.pop("diffuse")

        emissive = d.pop("emissive")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        render_material = cls(
            id=id,
            speckle_type=speckle_type,
            opacity=opacity,
            metalness=metalness,
            roughness=roughness,
            diffuse=diffuse,
            emissive=emissive,
            name=name,
        )

        render_material.additional_properties = d
        return render_material

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
