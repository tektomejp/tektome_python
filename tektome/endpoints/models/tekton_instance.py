from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.geometry import Geometry
    from ..models.render_material import RenderMaterial
    from ..models.transform import Transform


T = TypeVar("T", bound="TektonInstance")


@_attrs_define
class TektonInstance:
    """
    Attributes:
        geometry (Geometry):
        hash_geometry_material (str):
        transform (list[Transform] | Unset):
        material (None | RenderMaterial | Unset):
    """

    geometry: Geometry
    hash_geometry_material: str
    transform: list[Transform] | Unset = UNSET
    material: None | RenderMaterial | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.render_material import RenderMaterial

        geometry = self.geometry.to_dict()

        hash_geometry_material = self.hash_geometry_material

        transform: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.transform, Unset):
            transform = []
            for transform_item_data in self.transform:
                transform_item = transform_item_data.to_dict()
                transform.append(transform_item)

        material: dict[str, Any] | None | Unset
        if isinstance(self.material, Unset):
            material = UNSET
        elif isinstance(self.material, RenderMaterial):
            material = self.material.to_dict()
        else:
            material = self.material

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "geometry": geometry,
                "hashGeometryMaterial": hash_geometry_material,
            }
        )
        if transform is not UNSET:
            field_dict["transform"] = transform
        if material is not UNSET:
            field_dict["material"] = material

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.geometry import Geometry
        from ..models.render_material import RenderMaterial
        from ..models.transform import Transform

        d = dict(src_dict)
        geometry = Geometry.from_dict(d.pop("geometry"))

        hash_geometry_material = d.pop("hashGeometryMaterial")

        _transform = d.pop("transform", UNSET)
        transform: list[Transform] | Unset = UNSET
        if _transform is not UNSET:
            transform = []
            for transform_item_data in _transform:
                transform_item = Transform.from_dict(transform_item_data)

                transform.append(transform_item)

        def _parse_material(data: object) -> None | RenderMaterial | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                material_type_0 = RenderMaterial.from_dict(data)

                return material_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RenderMaterial | Unset, data)

        material = _parse_material(d.pop("material", UNSET))

        tekton_instance = cls(
            geometry=geometry,
            hash_geometry_material=hash_geometry_material,
            transform=transform,
            material=material,
        )

        tekton_instance.additional_properties = d
        return tekton_instance

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
