from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObservabilitySchemaOut")


@_attrs_define
class ObservabilitySchemaOut:
    """
    Attributes:
        created (datetime.datetime):
        updated (datetime.datetime):
        observed_entity (UUID):
        scoping_entity (UUID):
        id (None | Unset | UUID):
        is_viewed (bool | Unset):  Default: False.
    """

    created: datetime.datetime
    updated: datetime.datetime
    observed_entity: UUID
    scoping_entity: UUID
    id: None | Unset | UUID = UNSET
    is_viewed: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created.isoformat()

        updated = self.updated.isoformat()

        observed_entity = str(self.observed_entity)

        scoping_entity = str(self.scoping_entity)

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        is_viewed = self.is_viewed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "updated": updated,
                "observed_entity": observed_entity,
                "scoping_entity": scoping_entity,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if is_viewed is not UNSET:
            field_dict["is_viewed"] = is_viewed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        observed_entity = UUID(d.pop("observed_entity"))

        scoping_entity = UUID(d.pop("scoping_entity"))

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

        is_viewed = d.pop("is_viewed", UNSET)

        observability_schema_out = cls(
            created=created,
            updated=updated,
            observed_entity=observed_entity,
            scoping_entity=scoping_entity,
            id=id,
            is_viewed=is_viewed,
        )

        observability_schema_out.additional_properties = d
        return observability_schema_out

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
