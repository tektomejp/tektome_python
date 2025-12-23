from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attribute_schema import AttributeSchema
    from ..models.lawtalk_project_organization_schema import LawtalkProjectOrganizationSchema
    from ..models.lawtalk_project_required_schema import LawtalkProjectRequiredSchema


T = TypeVar("T", bound="LawtalkProjectResolversSchema")


@_attrs_define
class LawtalkProjectResolversSchema:
    """
    Attributes:
        lawtalk_attributes (list[AttributeSchema]):
        core_attributes (LawtalkProjectRequiredSchema):
        core_project_id (UUID):
        organization (LawtalkProjectOrganizationSchema):
        created (datetime.datetime):
        updated (datetime.datetime):
        is_external (bool): Is the project external from the organization
        id (None | Unset | UUID):
    """

    lawtalk_attributes: list[AttributeSchema]
    core_attributes: LawtalkProjectRequiredSchema
    core_project_id: UUID
    organization: LawtalkProjectOrganizationSchema
    created: datetime.datetime
    updated: datetime.datetime
    is_external: bool
    id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lawtalk_attributes = []
        for lawtalk_attributes_item_data in self.lawtalk_attributes:
            lawtalk_attributes_item = lawtalk_attributes_item_data.to_dict()
            lawtalk_attributes.append(lawtalk_attributes_item)

        core_attributes = self.core_attributes.to_dict()

        core_project_id = str(self.core_project_id)

        organization = self.organization.to_dict()

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        is_external = self.is_external

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lawtalk_attributes": lawtalk_attributes,
                "core_attributes": core_attributes,
                "core_project_id": core_project_id,
                "organization": organization,
                "created": created,
                "updated": updated,
                "is_external": is_external,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attribute_schema import AttributeSchema
        from ..models.lawtalk_project_organization_schema import LawtalkProjectOrganizationSchema
        from ..models.lawtalk_project_required_schema import LawtalkProjectRequiredSchema

        d = dict(src_dict)
        lawtalk_attributes = []
        _lawtalk_attributes = d.pop("lawtalk_attributes")
        for lawtalk_attributes_item_data in _lawtalk_attributes:
            lawtalk_attributes_item = AttributeSchema.from_dict(lawtalk_attributes_item_data)

            lawtalk_attributes.append(lawtalk_attributes_item)

        core_attributes = LawtalkProjectRequiredSchema.from_dict(d.pop("core_attributes"))

        core_project_id = UUID(d.pop("core_project_id"))

        organization = LawtalkProjectOrganizationSchema.from_dict(d.pop("organization"))

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        is_external = d.pop("is_external")

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

        lawtalk_project_resolvers_schema = cls(
            lawtalk_attributes=lawtalk_attributes,
            core_attributes=core_attributes,
            core_project_id=core_project_id,
            organization=organization,
            created=created,
            updated=updated,
            is_external=is_external,
            id=id,
        )

        lawtalk_project_resolvers_schema.additional_properties = d
        return lawtalk_project_resolvers_schema

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
