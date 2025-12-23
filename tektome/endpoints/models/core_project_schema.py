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
    from ..models.core_project_required_schema import CoreProjectRequiredSchema
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="CoreProjectSchema")


@_attrs_define
class CoreProjectSchema:
    """
    Attributes:
        core_attributes (CoreProjectRequiredSchema):
        created_by (None | UserMetadata):
        updated_by (None | UserMetadata):
        created (datetime.datetime):
        updated (datetime.datetime):
        id (None | Unset | UUID):
    """

    core_attributes: CoreProjectRequiredSchema
    created_by: None | UserMetadata
    updated_by: None | UserMetadata
    created: datetime.datetime
    updated: datetime.datetime
    id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_metadata import UserMetadata

        core_attributes = self.core_attributes.to_dict()

        created_by: dict[str, Any] | None
        if isinstance(self.created_by, UserMetadata):
            created_by = self.created_by.to_dict()
        else:
            created_by = self.created_by

        updated_by: dict[str, Any] | None
        if isinstance(self.updated_by, UserMetadata):
            updated_by = self.updated_by.to_dict()
        else:
            updated_by = self.updated_by

        created = self.created.isoformat()

        updated = self.updated.isoformat()

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
                "core_attributes": core_attributes,
                "created_by": created_by,
                "updated_by": updated_by,
                "created": created,
                "updated": updated,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.core_project_required_schema import CoreProjectRequiredSchema
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)
        core_attributes = CoreProjectRequiredSchema.from_dict(d.pop("core_attributes"))

        def _parse_created_by(data: object) -> None | UserMetadata:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                created_by_type_0 = UserMetadata.from_dict(data)

                return created_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UserMetadata, data)

        created_by = _parse_created_by(d.pop("created_by"))

        def _parse_updated_by(data: object) -> None | UserMetadata:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                updated_by_type_0 = UserMetadata.from_dict(data)

                return updated_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UserMetadata, data)

        updated_by = _parse_updated_by(d.pop("updated_by"))

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

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

        core_project_schema = cls(
            core_attributes=core_attributes,
            created_by=created_by,
            updated_by=updated_by,
            created=created,
            updated=updated,
            id=id,
        )

        core_project_schema.additional_properties = d
        return core_project_schema

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
