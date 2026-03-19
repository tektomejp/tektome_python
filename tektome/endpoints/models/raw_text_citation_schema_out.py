from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="RawTextCitationSchemaOut")


@_attrs_define
class RawTextCitationSchemaOut:
    """
    Attributes:
        id (UUID):
        title (str):
        attribute_content_type (str):
        attribute_object_id (UUID):
        created (datetime.datetime):
        updated (datetime.datetime):
        created_by (UserMetadata):
        updated_by (UserMetadata):
        highlights (list[str]):
        resource_id (UUID):
    """

    id: UUID
    title: str
    attribute_content_type: str
    attribute_object_id: UUID
    created: datetime.datetime
    updated: datetime.datetime
    created_by: UserMetadata
    updated_by: UserMetadata
    highlights: list[str]
    resource_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        title = self.title

        attribute_content_type = self.attribute_content_type

        attribute_object_id = str(self.attribute_object_id)

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        created_by = self.created_by.to_dict()

        updated_by = self.updated_by.to_dict()

        highlights = self.highlights

        resource_id = str(self.resource_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "attribute_content_type": attribute_content_type,
                "attribute_object_id": attribute_object_id,
                "created": created,
                "updated": updated,
                "created_by": created_by,
                "updated_by": updated_by,
                "highlights": highlights,
                "resource_id": resource_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        title = d.pop("title")

        attribute_content_type = d.pop("attribute_content_type")

        attribute_object_id = UUID(d.pop("attribute_object_id"))

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        created_by = UserMetadata.from_dict(d.pop("created_by"))

        updated_by = UserMetadata.from_dict(d.pop("updated_by"))

        highlights = cast(list[str], d.pop("highlights"))

        resource_id = UUID(d.pop("resource_id"))

        raw_text_citation_schema_out = cls(
            id=id,
            title=title,
            attribute_content_type=attribute_content_type,
            attribute_object_id=attribute_object_id,
            created=created,
            updated=updated,
            created_by=created_by,
            updated_by=updated_by,
            highlights=highlights,
            resource_id=resource_id,
        )

        raw_text_citation_schema_out.additional_properties = d
        return raw_text_citation_schema_out

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
