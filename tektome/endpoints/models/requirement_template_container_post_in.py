from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.requirement_template_status import RequirementTemplateStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="RequirementTemplateContainerPostIn")


@_attrs_define
class RequirementTemplateContainerPostIn:
    """Serializer for Requirement Template.

    Attributes:
        name (str):
        organization_id (UUID):
        description (None | str | Unset):
        public_resources (list[UUID] | Unset):
        status (RequirementTemplateStatus | Unset): Enum for Requirement Template Status. Default:
            RequirementTemplateStatus.DRAFT.
    """

    name: str
    organization_id: UUID
    description: None | str | Unset = UNSET
    public_resources: list[UUID] | Unset = UNSET
    status: RequirementTemplateStatus | Unset = RequirementTemplateStatus.DRAFT
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        organization_id = str(self.organization_id)

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        public_resources: list[str] | Unset = UNSET
        if not isinstance(self.public_resources, Unset):
            public_resources = []
            for public_resources_item_data in self.public_resources:
                public_resources_item = str(public_resources_item_data)
                public_resources.append(public_resources_item)

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "organization_id": organization_id,
            }
        )
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
        name = d.pop("name")

        organization_id = UUID(d.pop("organization_id"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _public_resources = d.pop("public_resources", UNSET)
        public_resources: list[UUID] | Unset = UNSET
        if _public_resources is not UNSET:
            public_resources = []
            for public_resources_item_data in _public_resources:
                public_resources_item = UUID(public_resources_item_data)

                public_resources.append(public_resources_item)

        _status = d.pop("status", UNSET)
        status: RequirementTemplateStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RequirementTemplateStatus(_status)

        requirement_template_container_post_in = cls(
            name=name,
            organization_id=organization_id,
            description=description,
            public_resources=public_resources,
            status=status,
        )

        requirement_template_container_post_in.additional_properties = d
        return requirement_template_container_post_in

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
