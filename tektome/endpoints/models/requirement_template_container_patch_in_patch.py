from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.requirement_template_status import RequirementTemplateStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="RequirementTemplateContainerPatchInPatch")


@_attrs_define
class RequirementTemplateContainerPatchInPatch:
    """
    Attributes:
        name (None | str | Unset):
        description (None | str | Unset):
        public_resources (list[UUID] | None | Unset):
        status (None | RequirementTemplateStatus | Unset):
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    public_resources: list[UUID] | None | Unset = UNSET
    status: None | RequirementTemplateStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        public_resources: list[str] | None | Unset
        if isinstance(self.public_resources, Unset):
            public_resources = UNSET
        elif isinstance(self.public_resources, list):
            public_resources = []
            for public_resources_type_0_item_data in self.public_resources:
                public_resources_type_0_item = str(public_resources_type_0_item_data)
                public_resources.append(public_resources_type_0_item)

        else:
            public_resources = self.public_resources

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, RequirementTemplateStatus):
            status = self.status.value
        else:
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if public_resources is not UNSET:
            field_dict["public_resources"] = public_resources
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_public_resources(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                public_resources_type_0 = []
                _public_resources_type_0 = data
                for public_resources_type_0_item_data in _public_resources_type_0:
                    public_resources_type_0_item = UUID(public_resources_type_0_item_data)

                    public_resources_type_0.append(public_resources_type_0_item)

                return public_resources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        public_resources = _parse_public_resources(d.pop("public_resources", UNSET))

        def _parse_status(data: object) -> None | RequirementTemplateStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = RequirementTemplateStatus(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RequirementTemplateStatus | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        requirement_template_container_patch_in_patch = cls(
            name=name,
            description=description,
            public_resources=public_resources,
            status=status,
        )

        requirement_template_container_patch_in_patch.additional_properties = d
        return requirement_template_container_patch_in_patch

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
