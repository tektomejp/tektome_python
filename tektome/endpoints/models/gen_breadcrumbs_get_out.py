from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.folder_schema import FolderSchema
    from ..models.gen_breadcrumbs_resource_group_get_out import GenBreadcrumbsResourceGroupGetOut


T = TypeVar("T", bound="GenBreadcrumbsGetOut")


@_attrs_define
class GenBreadcrumbsGetOut:
    """
    Attributes:
        resource_group (GenBreadcrumbsResourceGroupGetOut):
        parents (list[FolderSchema] | None | Unset):
    """

    resource_group: GenBreadcrumbsResourceGroupGetOut
    parents: list[FolderSchema] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_group = self.resource_group.to_dict()

        parents: list[dict[str, Any]] | None | Unset
        if isinstance(self.parents, Unset):
            parents = UNSET
        elif isinstance(self.parents, list):
            parents = []
            for parents_type_0_item_data in self.parents:
                parents_type_0_item = parents_type_0_item_data.to_dict()
                parents.append(parents_type_0_item)

        else:
            parents = self.parents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_group": resource_group,
            }
        )
        if parents is not UNSET:
            field_dict["parents"] = parents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.folder_schema import FolderSchema
        from ..models.gen_breadcrumbs_resource_group_get_out import GenBreadcrumbsResourceGroupGetOut

        d = dict(src_dict)
        resource_group = GenBreadcrumbsResourceGroupGetOut.from_dict(d.pop("resource_group"))

        def _parse_parents(data: object) -> list[FolderSchema] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                parents_type_0 = []
                _parents_type_0 = data
                for parents_type_0_item_data in _parents_type_0:
                    parents_type_0_item = FolderSchema.from_dict(parents_type_0_item_data)

                    parents_type_0.append(parents_type_0_item)

                return parents_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FolderSchema] | None | Unset, data)

        parents = _parse_parents(d.pop("parents", UNSET))

        gen_breadcrumbs_get_out = cls(
            resource_group=resource_group,
            parents=parents,
        )

        gen_breadcrumbs_get_out.additional_properties = d
        return gen_breadcrumbs_get_out

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
