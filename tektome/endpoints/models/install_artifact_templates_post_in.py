from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.duplicate_strategy import DuplicateStrategy
from ..types import UNSET, Unset

T = TypeVar("T", bound="InstallArtifactTemplatesPostIn")


@_attrs_define
class InstallArtifactTemplatesPostIn:
    """
    Attributes:
        group_ids (list[UUID]): List of template group IDs to install
        on_duplicate (DuplicateStrategy | Unset): Controls how duplicate artifact paths are handled during import.
            Default: DuplicateStrategy.SKIP.
    """

    group_ids: list[UUID]
    on_duplicate: DuplicateStrategy | Unset = DuplicateStrategy.SKIP
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_ids = []
        for group_ids_item_data in self.group_ids:
            group_ids_item = str(group_ids_item_data)
            group_ids.append(group_ids_item)

        on_duplicate: str | Unset = UNSET
        if not isinstance(self.on_duplicate, Unset):
            on_duplicate = self.on_duplicate.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "group_ids": group_ids,
            }
        )
        if on_duplicate is not UNSET:
            field_dict["on_duplicate"] = on_duplicate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_ids = []
        _group_ids = d.pop("group_ids")
        for group_ids_item_data in _group_ids:
            group_ids_item = UUID(group_ids_item_data)

            group_ids.append(group_ids_item)

        _on_duplicate = d.pop("on_duplicate", UNSET)
        on_duplicate: DuplicateStrategy | Unset
        if isinstance(_on_duplicate, Unset):
            on_duplicate = UNSET
        else:
            on_duplicate = DuplicateStrategy(_on_duplicate)

        install_artifact_templates_post_in = cls(
            group_ids=group_ids,
            on_duplicate=on_duplicate,
        )

        install_artifact_templates_post_in.additional_properties = d
        return install_artifact_templates_post_in

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
